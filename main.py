"""Write the entry image for news-image-20261118.

The picture is a front page for Wednesday 18 November 2026 - the day Xi met
Trump on the tarmac in Shenzhen, the US struck Qeshm Island and Iran answered
Kuwait and Bahrain, and Grand Theft Auto VI was called a masterpiece by the
critics. It is drawn by ``build_plate.py`` and committed here as a PNG; this
program copies those exact bytes to /output/entry.png so that both runs of the
entry write the same file. No network, no clock, no random source.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
IMAGE = HERE / "entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1024 * 1024


def check_plate() -> None:
    """Fail loudly if the committed picture would not pass the sealed gate."""
    data = IMAGE.read_bytes()
    if not data.startswith(PNG_MAGIC):
        raise SystemExit("entry.png is not a PNG")
    if len(data) > MAX_BYTES:
        raise SystemExit("entry.png is larger than 1 MiB")


def main() -> None:
    check_plate()
    OUT.mkdir(parents=True, exist_ok=True)
    target = OUT / "entry.png"
    shutil.copyfile(IMAGE, target)


if __name__ == "__main__":
    main()
