"""Write the entry image for news-image-20261118.

The picture itself is authored offline and committed beside this file: a
front-page plate for Wednesday 18 November 2026, the day three leaders met in
Beijing while Iranian missiles reached Kuwait and Bahrain. This program only
copies it to /output/entry.png, byte for byte, so two runs write the same file
and no network, clock or random source is touched.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    source = HERE / "entry.png"
    target = OUT / "entry.png"
    if target.exists() and target.samefile(source):
        return
    shutil.copyfile(source, target)


if __name__ == "__main__":
    main()
