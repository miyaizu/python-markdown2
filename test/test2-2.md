## python-markdown2 2.1.0

- ["nofollow" extra, issue #74, pull #104] Add `rel="nofollow"` support (mostly by https://github.com/cdman):

---

    $ echo '[link](http://example)' | markdown2 -x nofollow
    <p><a rel="nofollow" href="http://example">link</a></p>

---

Limitation: This *can* add a duplicate 'rel' attribute to raw HTML links
in the input.
