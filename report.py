"""
Accept stdout from https://gitlab.com/stalker314314/gtfs-osm-validator
and add some markdown formatting.
"""

import argparse
import re
from datetime import datetime


STOPWORDS_RE = (
    #re.compile('Processing OSM route (\d+)'),
    re.compile('OSM is missing route (\d+)'),
    re.compile('Route master name in OSM'),
)
RELATIONS = (
    re.compile('(.* [(])(\d+)([)].*)'),
    re.compile('(.* route )(\d+)( .*)'),
    re.compile('(.* OSM master route )(\d+)( .*)'),
    re.compile('(.* for route )(\d+)( .*)'),
    re.compile('(.* for route master )(\d+)( .*)'),
)

def add_rel_link_to_row(row: str) -> str:
    for _ in STOPWORDS_RE:
        if _.search(row):
            return row  # unchanged

    for relation in RELATIONS:
        m = relation.fullmatch(row)
        if m:
            pre, rel, post = m.groups()
            return f'{pre}[{rel}](http://openstreetmap.org/relation/{rel}){post}'

    return row # unchanged


OSM_TAG_RE = re.compile('(\w+:\w+)')
def add_tag_link_to_row(row: str) -> str:
    return OSM_TAG_RE.sub("[\\1](https://wiki.openstreetmap.org/wiki/Key:\\1)", row)


COLOUR_RE = re.compile("(#[0-9a-fA-F]{6})")

def add_colour_swatch_to_row(row: str) -> str:
    return COLOUR_RE.sub('`\\1`', row)  # Note: GFM renderer add a coloured dot


WARNING_RE = re.compile('(.*) ([A-Z]+): (.*)')

def highlight_warnings(row: str) -> str:
    return WARNING_RE.sub("\\1 **\\2**: \\3", row)


INDENTED_ROW = re.compile('^( *)  ([^ ].*)$')

def format_markdown(row: str) -> str:
    if row.startswith('Processing '):
        return f'\n# {row}\n'  # heading

    if row.startswith('  Processing '):
        return f'\n## {row}\n'  # subheading

    if not row.startswith(' '):
        return f'\n{row}'  # junk

    return INDENTED_ROW.sub("\\1* \\2", row)



def main():

    p = argparse.ArgumentParser()
    p.add_argument("--read", type=argparse.FileType('r'))
    p.add_argument("--write", type=argparse.FileType('wb'))
    n = p.parse_args()

    for row in n.read.readlines():
        output_row = row.rstrip()
        for fn in (
            add_rel_link_to_row,
            add_tag_link_to_row,
            add_colour_swatch_to_row,
            format_markdown,
            highlight_warnings,

        ):
            output_row = fn(output_row)

        n.write.write(output_row + '\n')

    n.write.write(f"\n\n*Last updated {datetime.now().isoformat()}*\n")


if __name__ == '__main__':
    main()