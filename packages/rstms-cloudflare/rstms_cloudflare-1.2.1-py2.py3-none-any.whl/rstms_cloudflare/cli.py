"""Console script for rstms_cloudflare."""

import sys
from pathlib import Path

import click
import click.core

from .cloudflare import API
from .exception_handler import ExceptionHandler
from .shell import _shell_completion
from .version import __timestamp__, __version__

header = f"{__name__.split('.')[0]} v{__version__} {__timestamp__}"


def _ehandler(ctx, option, debug):
    ctx.obj = dict(ehandler=ExceptionHandler(debug))
    ctx.obj["debug"] = debug


@click.group(name="cloudflare")
@click.version_option(message=header)
@click.option("-d", "--debug", is_eager=True, is_flag=True, callback=_ehandler, help="debug mode")
@click.option(
    "--shell-completion",
    is_flag=False,
    flag_value="[auto]",
    callback=_shell_completion,
    help="configure shell completion",
)
@click.option("-q", "--quiet", is_flag=True)
@click.option("-r", "--raw", is_flag=True)
@click.option("-t", "--token", envvar="CLOUDFLARE_AUTH_TOKEN")
@click.option("-j", "--json", is_flag=True)
@click.option("-o", "--output", type=click.Path(writable=True, dir_okay=False, path_type=Path), help="output file")
@click.option("-i", "--id", "include_id", is_flag=True, help="include record ID in output")
@click.pass_context
def cli(ctx, debug, shell_completion, token, json, quiet, raw, include_id, output):
    if output:
        func = output.write_text
    else:
        func = click.echo
    ctx.obj = API(token=token, json=json, quiet=quiet, raw=raw, include_id=include_id, output_function=func)


@cli.command
@click.argument("domain", required=False)
@click.pass_obj
def dump(api, domain):
    """Output API data for one or all domains"""
    data = {}
    zones = api.get_zones()
    for zone in zones:
        if domain in [None, zone["name"]]:
            data[zone["name"]] = api.get_zone_records(zone["name"])
    if domain:
        if not data:
            raise ValueError(f"unknown domain: '{domain}'")

    api.json = True
    api.output(data)
    sys.exit(0 if data else -1)


def process_filter(arg, opt, name):
    if arg and opt:
        if arg == opt:
            opt = None
        else:
            raise RuntimeError(f"{name} option conflicts with argument")
    return arg or opt


@cli.command
@click.option("--delete", "delete_records", is_flag=True, help="delete selected records")
@click.option("--update-content", help="update selected record content")
@click.option("--update-ttl", type=int, help="update selected record TTL")
@click.option("--update-weight", type=int, help="update selected record weight")
@click.option("--update-priority", type=int, help="update selected record priority")
@click.option("--update-port", type=int, help="update selected record port")
@click.option("-t", "--type", "filter_type", type=click.Choice(API.RECORD_TYPES + ["ID"]))
@click.option("-h", "--host", "filter_host", help="match host or /regex/")
@click.option("-c", "--content", "filter_content", help="match content or /regex/")
@click.option("-p", "--priority", type=int, help="filter by MX priority")
@click.option("-w", "--weight", type=int)
@click.argument("domain")
@click.argument("type", type=click.Choice(API.RECORD_TYPES + ["ID"]), required=False)
@click.argument("host", required=False)
@click.argument("content", required=False)
@click.pass_obj
def records(
    api,
    domain,
    type,
    host,
    content,
    weight,
    filter_type,
    filter_host,
    filter_content,
    delete_records,
    priority,
    update_content,
    update_ttl,
    update_priority,
    update_weight,
    update_port,
):
    """select domain records"""

    if domain is None:
        domain = api.domain

    type = process_filter(type, filter_type, "type")
    host = process_filter(host, filter_host, "host")
    content = process_filter(content, filter_content, "content")

    records = api.select_records(domain, type, host, content, priority, weight)

    if delete_records:
        records = api.delete_records(domain, records)
    elif update_content or update_ttl or update_priority or update_weight:
        for record in records:
            if update_content:
                record["content"] = update_content
            if update_ttl:
                record["ttl"] = update_ttl
            if update_priority:
                if record["type"] == "SRV":
                    record["data"]["priority"] = update_priority
                elif record["type"] == "MX":
                    record["priority"] = update_priority
                else:
                    raise RuntimeError(f"priority unsuppported for record type {record['type']}")
            if update_weight:
                if record["type"] == "SRV":
                    record["data"]["weight"] = update_weight
                else:
                    raise RuntimeError(f"weight unsuppported for record type {record['type']}")
            if update_port:
                if record["type"] == "SRV":
                    record["data"]["port"] = update_port
                else:
                    raise RuntimeError(f"port unsuppported for record type {record['type']}")
        records = api.update_records(domain, records)
    else:
        records = api.format_records(records)

    api.output(records)
    if api.json:
        ret = 0
    else:
        ret = 0 if records else -1
    sys.exit(ret)


@cli.command
@click.pass_obj
def domains(api):
    """output registered domains"""
    zones = [zone["name"] for zone in api.get_zones()]
    if not api.json:
        zones = "\n".join(zones)
    api.output(zones)
    sys.exit(0 if zones else -1)


@cli.command
@click.argument("domain")
@click.pass_obj
def zone(api, domain):
    """output zone file"""

    zone_id = api.get_zone_id(domain)
    api.json = False
    api.output(api.client.zones.dns_records.export(zone_id))
    sys.exit(0)


@cli.command
@click.argument("domain")
@click.argument("type", type=click.Choice(API.RECORD_TYPES))
@click.argument("host")
@click.argument("content")
@click.option("-t", "--ttl", type=int, default=60)
@click.option("-p", "--priority", type=int, default=10)
@click.option("-w", "--weight", type=int, default=5)
@click.option("-P", "--port", type=int)
@click.pass_obj
def add(api, domain, type, host, content, ttl, priority, weight, port):
    """add a new record"""

    if type in ["A", "CNAME", "TXT", "AAAA"]:
        priority = None
        weight = None
        port = None
    elif type == "MX":
        weight = None
        port = None
    elif type == "SRV":
        if port is None:
            raise ValueError("port is required for SRV record")
    else:
        raise ValueError(f"Unsupported record type '{type}'")
    added = api.add_record(domain, type, host, content, ttl, priority, weight, port)
    api.output(added)
    sys.exit(0)


@cli.command
@click.option("-p", "--priority", type=int)
@click.option("-w", "--weight", type=int)
@click.argument("domain")
@click.argument("type", type=click.Choice(API.RECORD_TYPES + ["ID"]))
@click.argument("host")
@click.argument("content", required=False)
@click.pass_obj
def delete(api, domain, type, host, content, priority, weight):
    """delete matching record"""
    selected = api.select_records(domain, type, host, content, priority, weight)
    deleted = api.delete_records(domain, selected)
    api.output(deleted)
    sys.exit(0 if deleted else -1)


@cli.command
@click.option("-p", "--priority", type=int, help="record selection priority")
@click.option("-w", "--weight", type=int, help="record selection weight")
@click.option("-t", "--ttl", type=int, help="record selection ttl")
@click.argument("domain")
@click.argument("type", type=click.Choice(API.RECORD_TYPES + ["ID"]))
@click.argument("host")
@click.argument("content", required=False)
@click.option("--update-ttl", type=int, help="update selected record TTL")
@click.option("--update-weight", type=int, help="update selected record weight")
@click.option("--update-priority", type=int, help="update selected record priority")
@click.option("--update-content", help="update selected record content")
@click.pass_obj
def update(
    api, domain, type, host, content, priority, ttl, weight, update_content, update_ttl, update_priority, update_weight
):
    """update matching record content"""
    selected = api.select_records(domain, type, host, content, priority, weight)
    for record in selected:
        if update_content:
            record["content"] = update_content
        if record["type"] == "MX":
            if update_priority:
                record["priority"] = update_priority
        if record["type"] == "SRV":
            if update_priority:
                record["data"]["priority"] = update_priority
            if update_weight:
                record["data"]["weight"] = update_weight
            if update_content:
                record["data"]["target"] = update_content
        if update_ttl:
            record["ttl"] = update_ttl
    updated = api.update_records(domain, selected)
    api.output(updated)
    sys.exit(0 if updated else -1)


if __name__ == "__main__":
    sys.exit(cli())
