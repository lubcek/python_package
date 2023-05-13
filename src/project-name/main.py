#!/usr/bin/env python3

"""Module with main CLI interface."""

import argparse
import sys

from . import command

def main():
    try:
        command.execute()
    except:
        print("Fatal: error", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
