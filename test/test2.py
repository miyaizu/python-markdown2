#!/usr/bin/env python
# coding: utf-8


import sys
import os

sys.path.insert(0, os.path.expanduser("~/local_program/python-markdown2/lib"))
import markdown2


def main():
    md = markdown2.markdown("# test\n\n```\nimport sys\n```\n\n* 1\n* 2\n* 3", extras={ "fenced-code-blocks": None })
    print md


if __name__ == "__main__":
    main()

