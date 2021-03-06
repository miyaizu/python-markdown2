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

    text2 = """
```
$ echo '[link](http://example)' | markdown2 -x nofollow
<p><a rel="nofollow" href="http://example">link</a></p>
```
"""

    text3 = """
# aaaa

aaaa

## aaaaa

```
#include <aaa>

aaaa
```

aaaa

----

aaaaaa
aaaaaaaaaa
aaa`aaaaaa`aaaaaaaa

* a
* a
* a

aaaaa*aaaa*aaaaa
"""

    md = markdown2.markdown(text3,
            extras={
                "fenced-code-blocks": True,
                "wiki-tables": True,
                "hard-wrap": True,
                "rid-code-tag": True,
                #"cancel-code-sanitize": True,
                "html-classes": {
                    "pre": "test"
                    },
                })
    print md


if __name__ == "__main__":
    main()

