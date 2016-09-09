Goals
=====

This project aims at providing IVOA authors and editors with
a versatile tool to edit and collaborate on IVOA documents.

The goals could be summarized as follows:

  * enable documents to be properly versioned and authored concurrently;
  * adopt a lightweight markup language, thus focusing on the content rather
  than on the presentation;
  * require as few dependencies as possible;
  * be cross-platform;
  * produce high-quality typesetting renderings of the same master document in
  different formats.

Comparison with IVOATex
=======================

This project reuses IVOATex [@ivoatex] facilities as much as possible. The
motivation for departing from IvoaTex itself significantly, however, is that
some IVOA authors do not perceive authoring LaTex documents as an option.

A potential solution could have been to create `pandoc` templates that would
render Markdown as `IVOATex` latex files to be compiled with `IVOATex` itself.

However, this would have not provided much control over the rendering of the
contents, at least without adding `pandoc`-specific complexity. Moreover, this
would have increased the number of dependencies required to produce outputs,
which is already significant in `IVOATex`. Finally, It is easy enough to adapt
`IVOATex` to a bunch of templates for `pandoc`, while reducing the complexity of
the system.

Dependencies
============

In order to edit files you only need a text editor and whatever source control
system is required by your collaboration.

In order to build `html` documents only [`pandoc`](http://pandoc.org)
is required. It is also recommended to install the
[`pandoc cross-ref`](https://github.com/lierdakil/pandoc-crossref) filter.

`Pandoc` is open source and available for Linux, OSX, and Windows.

The `cross-ref` filter is available as source code and can be built from
sources. For Windows, pre-compiled binaries are available.

More advanced filters require a `Python` interpreter to run. These filters
allow to:

  * include external source files.
  * build complete documents with `IVOA` style.

Finally, if a `latex` distribution is installed, `PDF` documents can be
produced.

**NOTE**: On Windows, it should be possible to install all dependencies as
native packages with regular installers. It is also possible to build many
if not all the dependencies from sources, if desired.

The project is currently in an early development stage, so the user
interface is simple and not necessarily pretty. That will come with time.

Working without any dependencies
================================

A Markdown file is a text document, you can edit with any text editor.

Being a markup language, albeit a lightweight one, you might want to make sure
you are using the correct syntax. Any reasonably advanced text editor or
Integrated Development Environment currently supports Markdown syntax
highligthing and previews.

If the text editor does not support such previews, one can use browser
extensions that render Markdown files.

Some text editors, like `vim` and `emacs`, have add-ons that allow users to
preview Markdown through the browser: they render the file to `html` using
default templates and they instruct the browser to display them.

Limitations
-----------

In this mode you cannot get a full rendering of the specific `pandoc` Markdown
flavor, let alone run special filters defined in this project or use the
IVOA-specific `pandoc` templates.

However, we are trying to make sure that we remain as faithful as possible
to Markdown, so that any special features (e.g. `TODO` lists) are rendered in a
meaningful way in generic Markdown-to-`html` previews.

As described in the following sections, a document is usually made of a metadata
file and of one or more files with the actual content. One limitation while
working

One of the goals of this project is to allow IVOA documents to be written
and collaborated upon while focusing on the content only, without worrying
about the presentation. In other terms, authors should able to edit an IVOA
document without any dependencies and using a lightweight markup language.

The metadata header
===================

In the following sections we will assume your document is split in two files.
While this is not required, i.e. you might have a single file with all the info,
it is the most portable[^note:port] solution and we recommend it.

The first file contains the metadata about your document, including references
you mean to cite and the abstract. The metadata file for the document you are
currently reading, for example, is called `README.yaml`.

The second file contains the content itself. For this document, this file is
called `README.md`. Note that you can concatenate any number of files.

The metadata header

[^note:port]: portable in the sense that not all editors and renderers will
treat the metadata block in a nice way, since the metadata block is a
`pandoc`-specific feature.

Simple `HTML` output
====================

If one has `pandoc` installed, it is easy to produce `html` outputs that
are rather close to the final format of a published IVOA document, with few
limitations explained [below](#sec:simple-limitations).

By running the master Markdown document through the `pandoc` command one gets
the following advantages:

  * specific `pandoc` features (e.g. cross-references, table of
    contents, etc.) can be used and correctly rendered.
  * all metadata is used, including the abstract (see following sections).
  * rendering is very close to that of a published IVOA document

In order to make the translation process as easy and portable as possible, we
provide some batch scripts for different platforms. If you have a Windows
system, you can use the `.bat` files in a native shell (`cmd` or `powershell`).
If you have a *nix system (including OSX and Linux), you can use the `.sh`
commands in a terminal.

**NOTE**: you might also have a Windows system with an emulation platform
(`cygwin`) or native non-`POSIX` shells like `Git Bash` or `MinGW/MSys`
installed, you can use the `.sh` commands on Windows as well.

Installation
------------

### pandoc ###

Rendering
---------

From a command line terminal, you can produce the *simple* `html` rendering by
typing, from within the project's folder:

~~~
 C:\MinGW\msys\1.0\home\Omar\pandocIvoa> .\bin\simple.bat README.yaml README.md
 $ ./bin/simple.sh README.yaml README.md
~~~

If you open a browser window and point it to the `output/simple.html` file you
will see the `html` rendering of the file. Note that many features are actually
enabled. For instance, you should see the references listed at the end of the
document, citations should be hot links to the references section, and similarly
footnotes should be properly rendered as hot link superscript numbers pointing
to footnotes at the bottom of the document. Another link should get you back
from a footnote to its reference.

Limitations {#sec:simple-limitations}
-----------

The `simple` mode assumes there are no other dependencies available other than
`pandoc` itself. So, advanced features described in the following section are
not properly rendered.

Full `HTML` output
==================

This mode allows to take full advantage of some advanced features defined in
some `pandoc` extensions and in *ad hoc* filters defined in this project.

Installation
------------

Python needs to be installed and available in the terminal used to
produce the documents. This should be easily achieved on all platforms.

**TODO**: At this point, only Python 2.7 has been tested, but we must test
Python 3 is supported.

Optionally, in order to use smart cross references, the `pandoc-crossref` needs
to be installed. On Windows, binaries are available on the [project's
repository] (https://github.com/lierdakil/pandoc-crossref/releases). On all
platforms, it can be built from sources, which requires the installation of the
[Haskell Platform](https://www.haskell.org/platform/).

References
==========
