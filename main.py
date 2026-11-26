#!/usr/bin/env python3
"""The World Today — 27 November — entry for Sum up 27 November's world news in one image on make.fun.

Copies the news collage art.jpg byte-for-byte to the output entry.png
and verifies it with SHA-256.
"""

import hashlib
import os
import shutil

ART_SHA256 = "a8191ec3a31a845dd92d04071fc09fc24606c083ad8848db7dc17b2de07bff4e"


def main() -> None:
    src = os.path.join(os.path.dirname(__file__), "art.jpg")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    data = open(dst, "rb").read()
    digest = hashlib.sha256(data).hexdigest()
    assert digest == ART_SHA256, digest
    print("entry.png written (%d bytes, sha256 %s...)" % (len(data), digest[:12]))


if __name__ == "__main__":
    main()
