#!/usr/bin/env python
# coding: utf-8


import sys
import os

sys.path.insert(0, os.path.expanduser("~/local_program/python-markdown2/lib"))
import markdown2


def main():
    text = """
# test

test test
test test `test` test test

```
#include <string>
```

* 1
* 2
* 3

test

    #include <iostream>
    #include <stdio>

    int main() {
        return 0;
    }


test
"""

    md = markdown2.markdown(text,
            extras={
                "fenced-code-blocks": True,
                "wiki-tables": True,
                "hard-wrap": True,
                "rid-code-tag": True,
                #"cancel-code-sanitize": True,
                "html-classes": {
                    "pre": "aho"
                    },
                })
    print md


if __name__ == "__main__":
    main()

