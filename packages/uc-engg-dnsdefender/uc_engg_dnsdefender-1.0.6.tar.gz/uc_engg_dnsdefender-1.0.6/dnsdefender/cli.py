#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import sys
import site
import click

# Ensure Python finds the installed package
site.addsitedir(sys.path[0])

from .__init__ import __version__
import dnsdefender.scan
import dnsdefender.utils
import dnsdefender.cloudFlare
import dnsdefender.aws

LOGGING_LEVELS = {
    0: logging.NOTSET,
    1: logging.ERROR,
    2: logging.WARN,
    3: logging.INFO,
    4: logging.DEBUG,
}

class Info(object):
    """An information object to pass data between CLI functions."""
    def __init__(self):
        """Create a new instance."""
        self.verbose: int = 0

pass_info = click.make_pass_decorator(Info, ensure=True)

@click.group()
@click.option("--verbose", "-v", count=True, help="Enable verbose output.")
@pass_info
def cli(info: Info, verbose: int):
    """Run dnsdefender."""
    if verbose > 0:
        logging.basicConfig(
            level=LOGGING_LEVELS.get(verbose, logging.DEBUG)
        )
        click.echo(
            click.style(
                f"Verbose logging enabled. (LEVEL={logging.getLogger().getEffectiveLevel()})",
                fg="yellow",
            )
        )
    info.verbose = verbose

cli.add_command(dnsdefender.scan.cli, "scan")

@cli.command()
def version():
    """Get the library version."""
    click.echo(click.style(f"{__version__}", bold=True))
