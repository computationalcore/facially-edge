#!/usr/bin/env python3

import argparse
import sys

from exitstatus import ExitStatus

from facially.lib import generate


def parse_args() -> argparse.Namespace:
    """Parse user command line arguments."""
    parser = argparse.ArgumentParser(description='Print a Hello ARGUMENT message.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-s',
                        type=str,
                        required=True,
                        help='The input string to be printed.')
    return parser.parse_args()


def main() -> ExitStatus:
    """Accept arguments from the user, and display Hello ARGUMENT"""
    args = parse_args()

    print(generate(args.n))
    return ExitStatus.success


# Allow the script to be run standalone (useful during development in PyCharm).
if __name__ == '__main__':
    sys.exit(main())
