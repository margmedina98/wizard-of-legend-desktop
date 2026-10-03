"""Wizard of Legend Desktop — Local Windows and macOS helper for Wizard of Legend data paths, config and export caches, and export folders."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='wizard_of_legend_desktop',
        description='Local Windows and macOS helper for Wizard of Legend data paths, config and export caches, and export folders.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Wizard of Legend Desktop')
    print('Find the Wizard of Legend folder fast and keep a local spare.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
