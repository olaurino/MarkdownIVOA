#
#  Copyright (C) 2017  Smithsonian Astrophysical Observatory
#
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

"""
Panflute filter for jovial DSL processing
"""

import os
import traceback
from collections import namedtuple

import panflute as pf


DEFAULT_FILENAME = "non_existent"


def render(filename):
    if not os.path.isfile(filename):
        if filename == DEFAULT_FILENAME:
            content = "No filename provided. Please add `file: <filename>` to your YAML block"
        else:
            content = "File not found: {}".format(filename)
    else:
        try:
            content = pf.shell(["jovial", "-i", filename]).decode("utf-8")
        except IOError:
            content = traceback.format_exc()
    return content


def get_attributes(options):
    attributes = namedtuple("Attributes", "filename classes caption ident")

    return attributes(
        filename=options.get('file', DEFAULT_FILENAME),
        classes=options.get('classes', []) + ['xml', ],
        caption=options.get('caption', ""),
        ident=options.get('id', ""),
    )


def fenced_action(options, data, element, doc):
    attrs = get_attributes(options)

    content = render(attrs.filename)

    code = pf.CodeBlock(content,
                        classes=attrs.classes,
                        attributes={"caption": attrs.caption},
                        identifier=attrs.ident)
    return code


def main(doc=None):
    return pf.run_filter(pf.yaml_filter, tag='vodsl', function=fenced_action,
                         doc=doc)


if __name__ == '__main__':
    main()
