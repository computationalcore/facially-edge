#!/usr/bin/env python3

import argparse
import sys

from exitstatus import ExitStatus

from facially.lib import generate


def parse_args(parse_this=None) -> argparse.Namespace:
    """Parse user command line arguments."""
    parser = argparse.ArgumentParser(description='Print a Hello ARGUMENT message.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-s',
                        type=str,
                        required=True,
                        help='The input string to be printed.')
    return parser.parse_args(parse_this)


def main(args=None) -> ExitStatus:
    """Accept arguments and display a 'Hello ARGUMENT' """
    if not args:
        args = parse_args()
    else:
        args = parse_args(args)

    print(generate(args.s))
    return ExitStatus.success


# Allow the script to be run standalone (useful during development in PyCharm).
if __name__ == '__main__':
    sys.exit(main())
