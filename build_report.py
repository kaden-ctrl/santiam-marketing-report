#!/usr/bin/env python3
"""Build the Santiam social report.

Injects the real Santiam Hospital & Clinics logo SVG into the template, then
encodes every non-ASCII character as a numeric HTML entity.

Why the entity pass: an Artifact is wrapped in a <head> we don't control, so we
can't declare <meta charset>. If the page is ever interpreted as Latin-1, raw
UTF-8 bytes render as mojibake ("â€"" instead of an em dash). Numeric entities
are encoding-independent. It is safe to apply this to the <script> block too,
because every string in it is written through innerHTML / insertAdjacentHTML,
so the entities are decoded as HTML at insertion time.
"""
import pathlib

root = pathlib.Path(__file__).parent
logo = (root / 'assets' / 'logo-inline.svg').read_text().strip()
tpl = (root / 'report_template.html').read_text()

html = tpl.replace('<!--LOGO-->', logo)
ascii_html = html.encode('ascii', 'xmlcharrefreplace').decode('ascii')

out = root / 'santiam-social-report.html'
out.write_text(ascii_html)

non_ascii = sum(1 for c in html if ord(c) > 127)
print('wrote %s (%d bytes, %d non-ASCII chars escaped)'
      % (out.name, len(ascii_html), non_ascii))
