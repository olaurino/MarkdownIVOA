#!/usr/bin/env python

"""
Panflute filter to include external files in fenced YAML code blocks
"""
import os

import panflute as pf


def fenced_action(options, data, element, doc):
    # We'll only run this for CodeBlock elements of class 'include'
    file = options.get('file')
    classes = options.get('classes', [])
    caption = options.get('caption', "")
    ident = options.get('id', "")

    if not os.path.isfile(file):
        raise FileNotFoundError(file)

    with open(file, 'r', encoding="utf-8") as f:
        content = f.read()

    code = pf.CodeBlock(content, classes=classes, attributes={"caption": caption}, identifier=ident)
    return code


def main(doc=None):
    return pf.run_filter(pf.yaml_filter, tag='include', function=fenced_action,
                         doc=doc)


if __name__ == '__main__':
    main()
