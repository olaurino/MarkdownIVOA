#!/usr/bin/env python

"""
Pandoc filter to allow interpolation of metadata fields
into a document.  %{fields} will be replaced by the field's
value, assuming it is of the type MetaInlines or MetaString.
"""

from pandocfilters import *
from datetime import date
import re
import sys

TODAY = date.today()
TODAY_CODE = TODAY.strftime("%Y%m%d")


class NameUrlItem(object):
    def __init__(self, spec):
        self.name = stringify(spec['c'][self._key]['c'])
        try:
            self.url = stringify(spec['c']['url']['c'])
        except KeyError:
            self.url = None

    def html(self):
        if (self.url):
            template = "<a href='{url}'>{name}</a>"
        else:
            template = "{name}"
        return template.format(name=self.name, url=self.url)


class Version(NameUrlItem):
    def __init__(self, spec):
        self._key = 'ver'
        NameUrlItem.__init__(self, spec)


class Author(NameUrlItem):
    def __init__(self, spec):
        self._key = 'name'
        NameUrlItem.__init__(self, spec)


class HtmlHeaderRenderer(object):
    def __init__(self, meta):
        self._meta = meta

    def render(self):
        return [
                self._ivoa(),
                self._title(),
                self._version(),
                self._type(),
                self._docmeta(),
                ]

    def _ivoa(self):
        block = None
        with open('ivoa_block.html') as f:
            block = f.read()
        return self._raw(block)

    def _title(self):
        title = self._get_meta('title', "Title")
        return Header(1, ("",(),()), [Str(title)])

    def _version(self):
        version = self._get_meta('version', "0.1")
        return self._raw("<div id='versionstatement'>Version {}</div>".format(version))

    def _people(self, key='author', the_class=Author):
        authors = self._get_meta(key, [], False)
        content = ""
        for author_spec in authors:
            author = the_class(author_spec)
            template = "<li class='{}'>{}</li>\n"
            content += template.format(key, author.html())
        return content

    def _authors(self):
        return self._people()

    def _editors(self):
        return self._people('editor')

    def _previous_versions(self):
        return self._people('previousVersion', Version)

    def _type(self):
        doc_type = self._get_meta('type', 'WD', True)
        doc_date = self._get_meta('date', TODAY, True)
        try:
            with open(doc_type+".txt", 'r') as f:
                title = f.read()
        except:
            title = "UNKNOWN TYPE: " + doc_type
        content = "<div id='dateline'>{}<span id='docdate'>{}</span></div>".format(title, doc_date)
        return self._raw(content)

    def _docmeta(self):
        template = """
<dl id="docmeta">
<dt>Working Group</dt><dd id="ivoagroup">{group}</dd>
<dt>This Version</dt><dd><a class="currentlink"
href="http://www.ivoa.net/documents/{name}/{datecode}">
http://www.ivoa.net/documents/{name}/{datecode}</a></dd>
<dt>Latest Version</dt>
<dd><a class="latestlink"
href="http://www.ivoa.net/documents/{name}">
http://www.ivoa.net/documents/{name}</a></dd>
<dt>Previous
Versions</dt><dd><ul class="previousversions">{previousVersions}</dd>
<dt>Author(s)</dt><dd><ul class="authors">{authors}</ul></dd>
<dt>Editor(s)</dt><dd><ul class="editors">{editors}</ul></dd>
        """
        meta = {}
        meta['group'] = self._get_meta("group", "No Working Group")
        meta['name'] = self._get_meta("name", "default")
        meta['datecode'] = self._get_meta("dateCode", TODAY_CODE)
        meta['previousVersions'] = self._previous_versions()
        meta['authors'] = self._authors()
        meta['editors'] = self._editors()
        return self._raw(template.format(**meta))


    def type_desc(self):
        doc_type = self._get_meta('type', 'WD')
        try:
            with open(doc_type+"_description.txt", 'r') as f:
                description = f.read()
        except:
            description = "UKNOWN DESCRIPTION FOR TYPE: " + doc_type

        return RawBlock("html", "<h2>Status of this Document</h2>\n"+"<p id=statusdecl><em>"+description+"</em></p>")

    def _get_meta(self, key, default="", string=True):
        try:
            value = self._meta.get(key, {})['c']
            if string:
                value = stringify(value)
        except:
            value = default
        return value

    def _raw(self, content):
        return RawBlock("html", content)


def header(spec):
    return stringify(spec[2]).lower()


def render(format, meta):
    if format == 'html' or format == 'html5':
        return HtmlHeaderRenderer(meta).render()


def metavars(key, value, format, meta):
    if key == 'Header' and header(value) == 'header':
        return render(format, meta)
    if key == 'Header' and header(value) == 'abstract':
        h2 = Header(2, attributes({}), [Str("Abstract")])
        par = Para([Str(stringify(meta.get('abstract')))])
        status = HtmlHeaderRenderer(meta).type_desc()
        return Div(attributes({'class':"abstract"}), [h2, par, status])

if __name__ == "__main__":
    toJSONFilter(metavars)
