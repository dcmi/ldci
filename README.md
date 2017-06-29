### Linked Data Competency Index

This is the back-end repository used to generate a [documentation website](https://dcmi.github.io/ldci/) for the Linked Data Competency Index.  The website also supports the maintenance of the index by crowdsourcing.

Processes not covered in the website:

@@@ Running the Python script to generate the Markdown version of the index.  Assumes Python 3.
A simple Python script now generates a Markdown file [12] from the JSON
source.  This gets converted by the MkDocs static site generator into
HTML [3].

@@@ Running [mkdocs](http://mkdocs.org) to generate and push the website from Markdown sources. Link to installation.

@@@ Using the ASN Editor to make changes to the competency index.

@@@ [Clarify with Joseph!] Mechanism by which Joseph is informed of changes to the [master JSON file]( index so that the ASN website can be updated.

https://github.com/dcmi/ldci/blob/master/docs/D2695955_to_md.py

https://github.com/dcmi/ldci/blob/master/docs/D2695955.json

https://github.com/dcmi/ldci/blob/master/docs/Makefile

http://rdf.tools
    => click on ASN


----------------------------------------------------------------------
ASN Editor with Github backend (Joseph)

Joseph pictured the ultimate workflow, using Github, as follows: that a
standards owner like DCMI would host the JSON file on Github; users would
download the file, use the ASN editor to make changes, and issue a pull request
for approval.  He agreed that the JSON pull request (the diff showing changes
made) could be difficult to read, especially if someone were to move blocks of
RDF around.  As he points out, however, we could always pull the JSON back into
the ASN editor and view everything through its nice interface.

Joseph: And for getting the data ultimately up into the ASN system, that's a
completely separate workflow -- something we would need to discuss.  If you
were just working with the raw RDF output, you could dump them into a triple
store and expose it, if that's what you wanted to do, or in another system of
record.  Going up into the ASN is a bit more rigorous -- we would need to
discuss what that may look like.  Think of this as a scratchpad for working
with the raw data.

* Go to http://rdf.tools => _ASN_ => _Configure_ => _Load ASN File_ => _Choose existing file_ => [click on D2695955.json].  The editor displays green if the JSON file has parsed correctly.
    * _Describe_ tab: metadata about the index.
    * _Create_ tab: where the index is edited.
        * Clicking on a node (on the right) will populate the corresponding values (on the left)
        * The order of items can also be changed by moving things around on the right
* Under _Create_ tab, make edits, then press _Submit_ => _Download_ => _Download RDF_ => _Save_
    * RDF comes back out with the same filename.

Note: In the JSON/RDF-Resource-centric (RDF/JSON) format, the original
identifier (URI) is the main JSON entity, and it will have several objects.  On
import into the ASN editor, existing URIs are retained.  The order of
statements in the JSON file is retained.  All new statements are added using
UUID values -- RDF entities are are only created in the RDF context of this app
and have not (yet) been given a fully qualified, Web-resolvable identifier.
For example, a competency I added to the index was assigned the identifier
`urn:uuid:05f5c661-16df-40be-8743-47b72dc8a255`.  The modified version of 
the JSON file can always be re-loaded and re-edited in the ASN editor.

2. Configure => "load ASN File".  
   => Can grab your local JSON/RDF-RC (RDF/JSON) file
      In this case: 'D283321.json' -- would simulate your master file in Github.
      It's just raw JSON representation of Competency Index. 
      If it displays green, it's good (i.e., has parsed correctly).
      Loads properties of Competency Framework.
      There are more tabs: licensing, rights, etc...

    "Describe" tab: metadata about the CI itself
    "Create" tab: where you get into the actual taxonomy - individual nodes
        Clicking on a node will populate the values on the left-hand side
        Can move things around on the right.

    Then "Download" to get RDF data back out.  RDF comes back out of the system 
    with the same filename as went in.  

3. In the JSON/RDF-Resource-centric (RDF/JSON) format, the original identifier 
   (URI) is the main JSON entity, and it will have a bunch of objects.  On 
   import, original URIs are retained - valid identifiers brought in when we
   started to edit the app and were retained in the system.  All of the new
   statements, when you start to add children - all added using UUID values --
   RDF entities that were only created in the RDF context of this app so were
   never given a fully qualified, web-resolvable identifier.  The UUID chain is
   properly respected [shows example of array].  

   Diff showing the changes made.

Joseph: It will keep the property order as long as it was edited in this app.
Where it gets messy: new child added, so UUID added.

You can always take modified version and load it into ASN editor.

Joseph: This RDF/JSON format is the same format used in the LD4PE context
for the WordPress site: WP site reads the file and creates the taxonomy. 
Label is currently a literal value - could potentially be given a URI.

Tom: What is the template for assigning a URI to competency.

Links on the ASN website:

* http://asn.desire2learn.com/resources/ASNJurisdiction/DCMI
  Achievement Standards Network jurisdiction "DCMI"
* http://asn.desire2learn.com/resources/D2695955
  Competency Index for Linked Data
* http://asn.desire2learn.com/resources/S2742438
  An individual statement
* http://s3.amazonaws.com/asnstaticd2l/data/rdf/D2695955.json
  Downloadable as JSON

Joseph suggested that for the Github version to be canonical, one would need to
have resolution of the URIs to Github.  If that were the source of truth, the
one place, then would have to be able to serve out.  Unless there were a hook
to generate static pages out of competency that is checked in, you would need
to solve the individual URI resolution.

* Competencies and benchmarks get URIs assigned in the ASN repository
  namespace.  If we want to make individual competencies "clickable", such that
  a web page showing the content of a given competency is displayed, we will
  have to look either to the default ASN repository or give some thought to
  generating our own representation of the CI to which the URIs would
  dereference.  However, it is not at all clear how this could work without
  customization given that the URI assignment mechanism defaults to ASN URIs.

The RDF/JSON format used for `D2695955.md` is the same format
used in the LD4PE context for the WordPress site.  The WordPress
site reads the JSON file and creates a (WordPress) taxonomy.


