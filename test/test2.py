#!/usr/bin/env python
# coding: utf-8


import sys
import os

sys.path.insert(0, os.path.expanduser("~/local_program/python-markdown2/lib"))
import markdown2


def main():
    text = "# test\n\ntest test\ntest test `test` test test\n\n```\n#include <string>\n```\n\n* 1\n* 2\n* 3"
    md = markdown2.markdown(text,
            extras={
                "fenced-code-blocks": True,
                "wiki-tables": True,
                "hard-wrap": True,
                "rid-code-tag": True,
                "html-classes": {
                    "pre": "aho"
                    },
                })
    print md


if __name__ == "__main__":
    main()

