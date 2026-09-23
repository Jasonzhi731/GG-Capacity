"""Build index.html (GitHub Pages) from page.html (Artifact source).

page.html is authored for claude.ai Artifacts (no <!doctype>/<head>/<body>;
the Artifact host wraps it). This script wraps it into a standalone document
and injects the Google tag. Run after every edit to page.html:

    python build.py
"""
from pathlib import Path

ROOT = Path(__file__).parent
GTAG_ID = "G-YSTEFHDCGG"

GTAG = f"""<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GTAG_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GTAG_ID}');
</script>"""

# Mirrors the small reset the Artifact skeleton provides.
RESET = """<style>
:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
body{margin:0}img{max-width:100%}[hidden]{display:none!important}
</style>"""


def main() -> None:
    src = (ROOT / "page.html").read_text(encoding="utf-8")
    marker = '<div class="wrap">'
    head, sep, body = src.partition(marker)
    if not sep:
        raise SystemExit(f"marker {marker!r} not found in page.html")
    out = (
        "<!doctype html>\n<html lang=\"zh-Hant-TW\">\n<head>\n"
        "<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
        f"{GTAG}\n{RESET}\n{head.strip()}\n</head>\n<body>\n{marker}{body.rstrip()}\n</body>\n</html>\n"
    )
    (ROOT / "index.html").write_text(out, encoding="utf-8", newline="\n")
    print(f"index.html written ({len(out):,} chars)")


if __name__ == "__main__":
    main()
