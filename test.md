Introduction
============

Data providers put a lot of effort in organizing and maintaining metadata that
precisely describes their data files. This information is invaluable for users
and for software developers that provide users with user-friendly VO-enabled
applications. For example, such metadata can characterize the different axes of
the reference system in which the data is expressed, or the history of a
measurement, like the publication where the measurement was drawn from, the
calibration type, and so forth. In order to be interoperable, this metadata
must refer to some Data Model that is known to all parties: the IVOA defines
and maintains such standardized Data Models that describe astronomical data in
an abstract, interoperable way.

In order to enable such interoperable, extensible, portable annotation of data
files, one needs:

  i.  A language to unambiguously and efficiently describe Data Models and their
elements' identificators [@vodml].
  i.  Pointers linking a specific piece of information (data or metadata) to the
Data Model element it represents.^[This used to be the assumed role of the
`@utype` attribute in VOTable and for example TAP. This document introduces the
new `<VODML>` element for this purpose in VOTable, as agreed on in interop
meeting in Banff, 2014.]
  i.  A mapping specification that unambiguously describes the mapping
strategies that lead to faithful representations of Data Model instances in a
specific format.

Without a consistent language for describing Data Models there can be no
interoperability, both between them, reuse of models by models, or in their use
in other specifications. Such a language must be expressive and formal enough
to enable the serialization of data types of growing complexity and the
development of reusable, extensible software components and libraries that can
make the technological uptake of the VO standards seamless and scalable.
\todo{Rewrite this section, needs more on needs of data models per se,
and formal spec so that one can point into it in standardised fashion}

For serializations to non-standard representations one needs to map the
abstract Data Model to a particular format meta-model. For instance, the
VOTable format defines `RESOURCE`s, `TABLE`s, `PARAM`s, `FIELD`s, and so forth, and
provides explicit attributes such as units, `UCD`s, and `utypes`: in order to
represent instances of a Data Model, one needs to define an unambiguous mapping
between these meta-model elements and the Data Model language, so to make it
possible for software to be able to parse a file according to its Data Model
and to Data Providers to mark up their data products.

While one might argue that a standard for portable, interoperable Data Model
representation would have been required before one could think about such a
mapping, we are specifying it only at a later stage. In particular several
different interpretations of `UTYPE`s have been proposed and used.
^[See [@usages]] This
specification aims to resolve this ambiguity.

TODO
====
\listoftodos

Bibliography
============
