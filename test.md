\todo{Add document History}

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

Any standard trying to reconcile these very different usages must take them
into account and make the transition from the current usages to the new
standard as seamless as possible. For this reason, this document also shows how
the current `UTYPE`s usages can be seamlessly integrated with the new scheme, so
to minimize the transition effort.

As a matter of fact, existing files and services can be made compliant
according to this specification by simply adding annotations and keeping the
old ones. So they do not need to change them in such a way that would
necessarily make them incompatible with existing software. 

Several sections of this document are utterly informative: in particular, the
appendices provide more information about the impact of this specification to
the current and future IVOA practices.

This specification describes how to represent Data Model instances using the
VOTable schema. This representation uses the `<VODML>` element introduced for
this purpose in VOTable v1.4 [@votable1.4] and the structure of the VOTable meta-model
elements to indicate how instances of data models are stored in VOTable
documents. We show many examples and give a complete listing of allowed mapping
patterns.

In sections [@sec:motivation] to [@sec:examples] we give an introduction to why
and how the VODML elements can
be used to hold pointers into the data models and several examples that
illustrate the mapping.

[@Sec:normative] is a rigorous listing of all valid annotations, and the normative
part of the specification. [@Sec:absences] describes what patterns and usages this
specification does not cover; moreover, it describes how legacy and custom
`@utypes` can be treated in this specification's framework: as such, this section
actually describes the transition from the current usages and this
specification. [@Sec:others] describes ideas on how this specification might be used
for annotating other tabular formats, and how to generalize it to other, more
structured data serialization formats.

The appendices contain additional material: [@sec:annotations] describes the VODML
annotation element that was added to the VOTable schema to support this mapping
specification. [@Sec:clients] describes different types of client software and how
they could deal with VOTables annotated according to the current specification.
[@Sec:regexp] defines a set-based "language" for expressing mapping patterns in a
more formal manner. [@Sec:faq] tries to answer some frequently asked
questions.

Use Cases {#usecases}
=========

The need for a mapping language {#sec:motivation}
===============================

Mapping with the `<VODML>` element {#sec:mapping}
==================================

General information about this spec {#sec:general}
===================================

Examples: Mapping VO-DML => VOTable {#sec:examples}
===================================

Patterns for annotating VOTable [NORMATIVE] {#sec:normative}
===========================================

Notable Absences {#sec:absences}
================

Serializing to other file formats {#sec:others}
=================================

\appendix

The VODML annotation elements in the VOTable schema {#sec:annotations}
===================================================

Growing complexity: naive, advanced, and guru clients {#sec:clients}
=====================================================

Regular expressions for mapping {#sec:regexp}
===============================

Frequently Asked Questions {#sec:faq}
==========================

\listoftodos

Bibliography
============
