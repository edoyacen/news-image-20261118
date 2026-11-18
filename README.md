# The world in one picture — 18 November 2026

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/edoyacen/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/edoyacen/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

An entry for [make.fun's](https://make.fun) `news-image-20261118` bounty
([bounty page](https://make.fun/bounty/news-image-20261118)): one image that
sums up Wednesday 18 November 2026's world news.

The day had two stories above all others:

- **Beijing.** Donald Trump, Xi Jinping and Vladimir Putin shared a stage at the
  APEC summit in China, with a Philippines trade deal announced alongside.
- **The Gulf.** Iran attacked Kuwait and Bahrain after US strikes on an island in
  the Strait of Hormuz, widening the war over the Strait.

The plate gives those two the top half. Beneath them: Democrats nominating Hakeem
Jeffries for Speaker with the Alaska seat flipping the Senate to 56–44; Nvidia's
sales soaring while the board keeps Huang out and Waymo pulls its robotaxis off
US freeways; and critics calling GTA 6 a masterpiece hours before its launch.

## How it is made

The picture is authored as an SVG page and rendered to a 1024×1024 PNG offline.
`main.py` copies `entry.png` to `/output/entry.png` with `shutil.copyfile`: no
network, no clock, no randomness, so two runs write identical bytes.

    MAKEFUN_OUTPUT_DIR=out python3 main.py

## Files

- `main.py` — copies the image to the output directory
- `entry.png` — the image, 1024×1024, 215 KiB
- `LICENSE` — MIT

Licensed MIT.
