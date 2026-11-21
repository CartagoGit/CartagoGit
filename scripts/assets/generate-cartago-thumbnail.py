#!/usr/bin/env python3
"""Generate a compact base64 rendering of the Cartago globe for small buttons.

The source SVG is 290 KB of vector detail. Inside a 30-pixel button that
detail is invisible and the base64 would be enormous, so it is rasterised
once at 128 px and embedded. The big mark shown in the README keeps the
original vector file.
"""
import base64
import io
import pathlib
import sys

sys.path.insert(0, "/tmp/svgvenv/lib/python3.10/site-packages")
import cairosvg  # noqa: E402
from PIL import Image  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = ROOT / "assets" / "projects" / "cartago.svg"
OUT = ROOT / "assets" / "projects" / "cartago-128.png"


def main() -> None:
    png = cairosvg.svg2png(url=str(SRC), output_width=128, output_height=128)
    img = Image.open(io.BytesIO(png)).convert("RGBA")
    # Quantise to keep the file small; the globe has smooth gradients but at
    # 128 px and inside a button, 128 colours is indistinguishable.
    img = img.quantize(colors=128, method=Image.Quantize.FASTOCTREE).convert("RGBA")
    buf = io.BytesIO()
    img.save(buf, format="PNG", optimize=True)
    OUT.write_bytes(buf.getvalue())
    print(f"wrote {OUT.relative_to(ROOT)} ({len(buf.getvalue())} bytes)")


main()
