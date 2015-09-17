import argparse
from amdfix import fixer


def main():
    """
    We operate in two modes.

    1. file mode: single file input, single output. Both can be "-", meaning
       std*.
    2. dir mode: convert whole directory. Takes source and destination folders.
    """
    parser = argparse.ArgumentParser(description='fix AMD files.')
    parser.add_argument(
        "--dir", action="store_true", default=False,
        help="Use directory mode, default if file mode."
    )
    parser.add_argument(
        "source", metavar="SOURCE", help="Source file or directory."
    )
    parser.add_argument(
        "destination", metavar="DESTINATION",
        help="Destination file or directory."
    )

    args = parser.parse_args()

    if args.dir:
        fixer.fix_dir(src=args.source, dst=args.destination)
    else:
        fixer.fix_file(src=args.source, dst=args.destination)
