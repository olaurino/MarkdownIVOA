% Lightweight markup languages
% Omar Laurino
% $\today$

Markdown
========

  * simple, *natural* syntax
  * ubiquituous
    * wikis, stack exchange, github, etc.
  * human- and machine- readable

However:

  * not standardized (MD *flavors*)
  * not extensible
  * lacks semantics

ReStructuredText
================

  * standardized
  * extensible
  * suitable for multi-page docs

However:

  * complex syntax
  * extensibility requires complex python manipulation
  * rendering requires complex builds

AsciiDoc
========

   * simple, *natural* syntax
   * complex, extensible architecture:
     * addresses all sorts of complex documents

However:

   * toolchain not mature:
     * PDF support is $\alpha$

Comparison
==========

--------------------------------------------------------------------------------
Markup            Toolchain       Programming     Notes
Language                          Language
---------------  -------------    --------------  ------------------------------
Markdown          pandoc           Haskell         Can write filters with
                                                   simple Python functions

ReST              sphinx           Python

AsciiDoc          AsciiDoctor      Ruby            No robust PDF support

--------------------------------------------------------------------------------
