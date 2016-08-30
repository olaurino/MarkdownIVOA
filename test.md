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

**
Throughout the document we will refer to some real or example Data Models.
Please remember that such models have been designed to be fairly simple,
yet complex enough to illustrate all the possible constructs that this
specification covers. They are not to be intended as actual DMs, nor,
by any means, this specification suggests their adoption by the IVOA or by
users and or Data Providers. In some cases we refer to actual DMs in order
to provide an idea of how this specification relates to real life cases
involving actual DMs.
**

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
In this section we list all legal mapping patterns that can be used to express
how instances of VO-DML-defined types are represented in a VOTable and the
possible roles they play. It defines which VOTable elements can be annotated
with `<VODML>` elements described in [@sec:mapping], what restrictions
there are and how to interpret the annotation.

The organization of the following sections is based on the different VO-DML
concepts that can be represented. Each of these subsections contains
sub-subsections which represent the different possible ways the concept may be
encountered in a VOTable and discuss rules and constraints on those annotations.
We start with `Model`, and then we discuss value types (`PrimitiveType`,
`Enumeration`, and `DataType`) and `Attribute`s. Then `ObjectType` and the
relationships, `Composition` (collection), `Reference`, and `Inheritance`
(extends). `Package` is not mapped: none of the use cases required this element
to be actually mapped to a VOTable instance.

Each subsection contains a concise, formal description of a mapping pattern,
according to a simple *grammar* described in [@sec:regexp] ... \todo{TBC}

For example the pattern expression:

--------------------------------------------------------------------------------
{GROUP G| G $\in$ TABLE & G/VODML/TYPE $\Rightarrow$ **ObjectType**
  & G/VODML/ROLE = NULL}

--------------------------------------------------------------------------------

Defines the pattern: `GROUP` directly under a `TABLE`, with `VODML/TYPE` element
identifying an `ObjectType` and without `VODML/ROLE` element. For example

----------------------------------------------------------
{GROUP|VODML/TYPE='vo-dml:Model' $\Rightarrow$ **Model**}

----------------------------------------------------------

implies the `GROUP` with `VODML/TYPE` set to `vo-dml:Model` is mapped to a
`Model`. \todo{See  whether we should define a list of
all the legal mapping patterns in  an Appendix.}

Some comments on how we refer to VOTable and VO-DML elements \todo{redundant
with text above in section ...}

  * When referring to VOTable elements we will use the notation by which these
elements will occur in VOTable documents, i.e. in general *all caps*, e.g.
`GROUP`, `FIELD`, (though `FIELDref`).
  * When referring to rows in a `TABLE` element in a
VOTable, we will use `TR`, when referring to individual cells, `TD`. Even though
such elements only appear in the `TABLEDATA` serialization of a `TABLE`. When
referring to a column in the `TABLE` we will use `FIELD`, also if we do
not intend the actual `FIELD` element annotating the column.
  * When referring to an `XML` attribute on a VOTable element we will prefix it
  with a `@`, e.g. `@id`, `@ref`.
  * References to VO-DML elements will be capitalized and **bold face**, using
their `VO-DML/XSD` type definitions. E.g. `ObjectType`, `Attribute`.
Some mapping solutions require a reference to a `GROUP` defined elsewhere in the
same VOTable.
We refer to such a construct as a `GROUPref`, which is not an element of the
current VOTable standard (v1.3). It refers to a `GROUP` with a `@ref` attribute,
which must always identify another `GROUP` in the same document. The target
`GROUP` must have an `@id` attribute. In cases where this is important we will
indicate that this combination is to be interpreted as a `GROUPref`.

## Model ##

### Model declaration: `GROUP` in `VOTABLE` ###

Pattern expression:

--------------------------------------------------------------------------------
{GROUP G| G $\in$ VOTABLE & G/VODML/TYPE="vo-dml:Model"}

--------------------------------------------------------------------------------

A GROUP element with VODML element identifying a Model and placed directly under
the root VOTABLE element indicates that the corresponding VO-DML model is used
in VODML associations.

Restrictions:

  * `GROUP` element representing a VO-DML Model must exist directly under
  `VOTABLE` Each such `GROUP` **MUST** have a VODML element with
  `VODML/TYPE="vo-dml:Model"`, no `VODML/ROLE`
  * **MUST** have child `PARAM`
  element with `VODML/ROLE="vo-dml:Model.identifier"` and `@value` the URI of
  the VO-DML document representing the model. `@name` is irrelevant,
  `@datatype="char"` and `arraysize="*"`. This annotation allows clients to
  discover whether a particular model is used in the document, the prefix of
  the `vodmlrefs` in the document, and to resolve the Model to its VO-DML
  description. The URI **MUST** be a `IVORN` for models registered in a VO
  registry.
  * **SHOULD** have child `PARAM` element with `VODML/ROLE="vo-dml:Model.url"`
  and `@value` the URL of the VO-DML document representing the model.
  `@name` is irrelevant, `@datatype="char"` and `arraysize="*"`. This is a
  convenient shortcut for the resolution of the URI. Data providers should make
  sure the URL is not broken. Clients should make sure that they fall back to
  resolving the URI if the URL is broken.
  * **MUST** have child PARAM element with `VODML/ROLE="vo-dml:Model.name"`
  and `@value` the name of the Model, which also works as the `vodmlref` prefix
  (see [@sec:mapping]). `@name` is irrelevant, `@datatype="char"` and
  `arraysize="*"`. The `@value` attribute **MUST** have the same value as the
  name of the Model in the VO-DML/XML document defining it.

```{include="code/model.xml" caption="Model example" .xml}
Model.xml example
```

## ObjectType ##
See also [@sec:composition] for more patterns regarding serialisation of
**`ObjectType`** instances.

### Standalone root **`ObjectType`**: direct `GROUP` ###

Pattern expression:

--------------------------------------------------------------------------------
{GROUP G| G $\subset$ RESOURCE & G $\not\subset$ TABLE & G $\not\subset$
  GROUP[VODML] & G/VODML/TYPE $\Rightarrow$ **`ObjectType`** &
  G/VODML/ROLE = NULL}

--------------------------------------------------------------------------------

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
