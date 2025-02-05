"""Cloudflare API Client"""

import json
import os
import re

import CloudFlare


class API:

    RECORD_TYPES = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT", "SRV", "LOC", "SSHFP", "CAA", "TLSA"]
    MAX_ZONES = 128

    def __init__(self, token=None, json=False, quiet=False, raw=False, include_id=False, output_function=None):
        token = token or os.environ["CLOUDFLARE_AUTH_TOKEN"]
        self.client = CloudFlare.CloudFlare(token=token)
        self.json = json
        self.raw = raw
        self.quiet = quiet
        self.include_id = include_id
        self.output_function = output_function or print

    def output(self, data):
        if self.quiet:
            return
        if self.json:
            data = json.dumps(data, indent=2)
        elif not data:
            return
        self.output_function(data)

    def get_zones(self):
        return self.client.zones.get(params={"per_page": self.MAX_ZONES})

    def get_zone_id(self, domain):
        zones = self.get_zones()
        for z in zones:
            if z["name"] == domain:
                return z["id"]
        raise ValueError(f"unknown domain {domain}")

    def get_zone_records(self, domain):
        records = {}
        zone_id = self.get_zone_id(domain)
        records = self.client.zones.dns_records.get(zone_id, params={"per_page": self.MAX_ZONES})
        return records

    def parse_host(self, name, domain):
        if name in ["@", domain]:
            name = domain
        else:
            name = ".".join([name, domain])
        name = name.strip(".")
        return name

    def delete_records(self, domain, records):
        deleted = [self.delete_record(domain, record) for record in records]
        if self.json:
            return deleted
        else:
            return "\n".join(deleted)

    def delete_record(self, domain, record):
        record_id = record["id"]
        zone_id = self.get_zone_id(domain)
        ret = self.client.zones.dns_records.delete(zone_id, record_id)
        if self.json:
            return ret
        else:
            return ret["id"]

    def add_record(self, domain, type, host, content, ttl=None, priority=None, weight=None, port=None):
        zone_id = self.get_zone_id(domain)
        host = self.parse_host(host, domain)
        record = dict(type=type, name=host, content=content, ttl=ttl)
        if type == "MX":
            record["priority"] = priority or 0
        elif type == "SRV":
            record["data"] = dict(
                port=port or 0, priority=priority or 0, target=record.pop("content"), weight=weight or 1
            )
        ret = self.client.zones.dns_records.post(zone_id, data=record)
        if self.json:
            return ret
        else:
            return ret["id"]

    def update_records(self, domain, records):
        updated = [self.update_record(domain, record) for record in records]
        if self.json:
            return updated
        else:
            return "\n".join(updated)

    def update_record(self, domain, record):
        dns_record_id = record["id"]
        zone_id = self.get_zone_id(domain)
        update = dict(
            name=record["name"],
            type=record["type"],
            content=record["content"],
            ttl=record["ttl"],
            proxied=record["proxied"],
        )
        ret = self.client.zones.dns_records.patch(zone_id, dns_record_id, data=update)

        if self.json:
            return ret
        else:
            return ret["id"]

    def format_host(self, record):
        domain = record["zone_name"]
        host = record["name"]
        if host.endswith(domain):
            host = host[: -1 - len(domain)]
        if not host:
            host = "@"
        return host

    def format_record(self, record):
        if self.json:
            if self.raw:
                out = record
            else:
                out = dict(
                    domain=record["zone_name"],
                    name=self.format_host(record),
                    content=record["content"],
                    type=record["type"],
                    ttl=record["ttl"],
                    priority=record.get("priority", None),
                )
                if record["type"] == "MX":
                    out["priority"] = record["priority"]
                if self.include_id:
                    out["id"] = record["id"]
        else:
            out = ""
            if self.include_id:
                out += f"{record['id']} "
            out += f"{record['type']} "
            if record["type"] == "MX":
                out += f"{record['priority']} "
            if record["type"] == "TXT":
                content = '"' + record["content"] + '"'
            else:
                content = record["content"]
            out += f"{record['name']} {content} {record['ttl']}"
        return out

    def format_records(self, records):
        formatted = [self.format_record(r) for r in records]
        if self.json:
            if self.include_id and not self.raw:
                formatted = {record["id"]: record for record in formatted}
                [record.pop("id") for record in formatted.values()]
            return formatted
        else:
            return "\n".join(formatted)

    def is_selected(self, pattern, text):
        if pattern is None:
            return True
        elif pattern.startswith("/"):
            return bool(re.match(pattern.strip("/"), text))
        else:
            return pattern == text

    def select_records(self, domain, type=None, host=None, content=None, priority=None):

        if host and type != "ID" and not host.startswith("/"):
            host = self.parse_host(host, domain)

        records = self.get_zone_records(domain)

        selected = []

        if type == "ID":
            for record in records:
                if host == record["id"]:
                    return [record]
            return []

        for record in records:
            if not self.is_selected(type, record["type"]):
                continue
            if not self.is_selected(host, record["name"]):
                continue
            if not self.is_selected(content, record["content"]):
                continue
            if record["type"] == "MX":
                if priority is not None:
                    if int(priority) != int(record["priority"]):
                        continue
            selected.append(record)

        return selected
