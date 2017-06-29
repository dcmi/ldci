### Linked Data Competency Index

This is the back-end repository used to generate a [documentation website](https://dcmi.github.io/ldci/) for the Linked Data Competency Index.  The website also supports the maintenance of the index by crowdsourcing.

Processes not covered in the website:

@@@ Running the Python script to generate the Markdown version of the index.  Assumes Python 3.

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

Joseph: Will discuss in terms of LD4PE workflow, the modified workshop that the
CIEB is using today, using Github as the "source of truth".  Using Ruby scripts
to produce RDF.  Goal of editor: you create the RDF representation, it will
create unique identifiers, will respect unique identifiers if it encounters
data.  Produces output. Output is the RDF/JSON-resource-centric version of RDF
(first pass at representing RDF with JSON, created by Talis) - can read and
write that data.  Ultimate workflow, with Github, would be: I own a standards
data file hosted on Github.  User could download, could use ASN editor to make
changes, could issue a pull request for approval ("hey, I've made some changes
to your competency file").

Tom: Kai and I are Github-literate, also command-line literate - would find it
helpful to see what the representation of the competency index looks like in
RDF, and get a sense of what a pull request would look like -- how readable it
would be.  Because I do have this fear that if we are viewing a pull request
against a RDF/JSON-resource-centric representation, it will be hard for members 
of the Editorial Board to read and interpret.

Joseph: Agree - looking at JSON pull request could get very messy - especially
if someone moves blocks of RDF around.  But the good news is that if you are
unsure of the changes you can always pull JSON into the ASN editor and view it
in this UI.  [Demonstrates]

Tom: The editor will run in my browser?  I'm just pointing it to my local repo?

Joseph: To demonstrate:

1. Go to http://rdf.tools - pure JavaScript - click on ASN
   With this tool, can create a SKOS or ASN scheme from scratch.
   A few flavors of this authoring environment:
   -- Taxonomies: for creating simple SKOS taxonomies or ASN data.
   -- Conversion (not hooked up yet): for converting data to Turtle or some 
      other RDF serialization.

   Click on "ASN" - app has four work flows:
   -- Configure Tool
   -- Describe collection
   -- Create competencies
   -- Download RDF

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

Stuart: The LD4PE repository is published at:

* Achievement Standards Network - jurisdiction "DCMI"
  http://asn.desire2learn.com/resources/ASNJurisdiction/DCMI
* Competency Index for Linked Data
  http://asn.desire2learn.com/resources/D2695955
* An individual statement
  http://asn.desire2learn.com/resources/S2742438
* Downloadable as JSON
  http://s3.amazonaws.com/asnstaticd2l/data/rdf/D2695955.json

At this point, it is the only repository of its kind.

Joseph: And for getting the data ultimately up into the ASN system, that's a
completely separate workflow -- something we would need to discuss.  If you
were just working with the raw RDF output, you could dump them into a triple
store and expose it, if that's what you wanted to do, or in another system of
record.  Going up into the ASN is a bit more rigorous -- we would need to
discuss what that may look like.  Think of this as a scratchpad for working
with the raw data.

I took the RDF-centric data and dumped it into http://www.easyrdf.org/converter
and pops out as Turtle.  Don't know if it would make sense just in terms of
legibility and readability to always do that conversion to Turtle -- I'm not
sure of that.  We're still experimenting with the Github workflow.

Tom: It would be easier to look at a diff between Turtle representations 
than between JSON.  

Joseph: This JSON/RDF-RC (RDF/JSON) can be converted by most existing libraries.

Tom: One piece I see missing here.  Are we assuming that a Web page will be
generated from this as well?  E.g., Ruby script that generates a PDF that
people can download and print.  Will not be used much if the best
representation is Turtle.  The website representation has a role, but need PDF.

Joseph: Could be added on or done separately.  

Tom: Maybe with a Githook - on commit, generate an updated PDF 
and that could be committed and made available.  Maybe we would set 
up a little Jekyll webpage describing how to use this, with links 
to latest PDF.

Stuart: There will be some final destination for this.  Probability 
is very high that WordPress site will vanish.  How all this stuff 
interfaces to the public will change.  My term is coming to an end 
in five weeks.  Some decision will need to be made by IAC about how 
to handle the WP pieces.  The workflow has to be rethought.

Tom: Unclear about the integration to Github backend.  Ideally, 
clone the repo, call up RDF tool, you'd point it at the JSON file, 
you'd do the edits, you'd save it back to the JSON file, then you'd 
go back and commit your changes and issue a pull request or whatever.
That's how I'm picturing it.

Joseph: That was my understanding as well, but you did raise a good 
point in terms of -- there's always going to be looking at the raw 
RDF and the diffs.  In the near future, would be good to suss out that 
workflow.  Maybe ultimately should involve conversion to some PDF 
structure with a diff.

Tom: In essence, that's what I did when we tested a way for people 
to give input to a Google doc, so I had this primitive representation 
of the competency index - simple Ruby script that generated a doc 
file which I could then pull up into Google Docs.  Then people 
could make comments there.  There workflow was not very automated 
but it sort of worked.  If the JSON representation - if we could put 
that on the LD4PE Github repo -- or would we getting that from ASN?

Joseph: You might be able to pull it from ASN, but probably better if 
I check that into the LD4PE repo.

Tom: Please do - so we can play around.  So unclear -- if the publication 
platform is the ASN repository, and the canonical copy (as I have been 
assuming) would be on our repo -- is that what you are thinking?  Assuming 
we would have canonical version.  Still some things about the workflow.

Joseph: I think for the Github version to be canonical, you'd need to 
have resolution of the URIs to Github.  If that were the source of truth, 
the one place, then would have to be able to serve out.  Unless there 
were a hook to generate static pages out of competency that is checked in,
you would need to solve the individual URI resolution.

Kai: What we want to have is the same process that DCMI is pursuing for the
website.  So we have a Github repo somewhere, with ASN or whatever -- but there
is somewhere this canonical version that must be maintained, then some readable
versions must be produced -- some data representation so that URIs be
dereferenced.  And see clearly that we need PDF.  But based on same data.  So
have to find way to edit it.  This ASN editor looks quite nice.  What we have
to test now is whether the editor works with this Git workflow that we have in
mind.  Technically oriented people may want to edit Turtle, but have to see how
that fits with rest of workflow.  My concerns, based on former projects: the
ordering issue.  If we create a JSON version -- must always be created the same
way -- this or JSON-LD -- because in JSON order is maintained.  Some process
that changes the order messes up the diff.  

We actually have to try it out.  Obviously, that's not yet in place, Git
integration, but even if it is not completely in place, if I take something
from Git and I put it into the ASN editor and edit it, and I put it back and
commit, or do pull request, to Git, if this works and reliably, also that I can
trust that the editor does not mess it up and everything is as expected, then I
would say that it is doable -- and worthwhile to do a full integration.  But
this is something I cannot see from this demonstration.  I would like to have
this file for tests.  With the whole editorial board, so we can see what is
going in and coming out.  Also would like to be able to view the source while
in the editor -- the editor is currently a bit too disconnected with source --
work side-by-side between JSON and graphical interface.  Just a thought.

Tom: Joseph, you will put copy in LD4PE repo? [Yes]  In terms of the LD4PE
project, Mike would like to finish the project before the summer takes over,
say in July?  Does that sound doable?  have another call after we have had a
chance to test this?  Have a call in June?

Joseph: That would probably work.

Tom's comments

* The ASN editor is very polished and quite easy to use.

* The location of the "canonical" RDF representation of the Competency Index
  must still be decided.  Currently, the canonical RDF representation resides
  on the ASN site.  Kai and I would like for it to be in our own Github
  repository.  Either way, some workflow issues have yet to be worked out.

* If we assume that users will download the JSON representation of the CI, use
  the online editor at http://rdf.tools to make changes, and submit the changed
  JSON file as a pull request, it remains to be clarified how we should view
  the changes in order to make an editorial decision.  Possibilities include
  automatically generating yet another representation, from the JSON source,
  that would lend itself better to a visualizing in a diff, such as Turtle or
  plain text.

* We will at any rate also need to have a PDF representation of the CI that
  people can download and print out.  This could perhaps be generated
  automatically, with a Ruby script, triggered perhaps by a git hook whenever a
  pull request is accepted and committed.

* By default, the typology of "competency", "benchmark", etc, is encoded as
  string values for a label.  This is how hundreds of other competency indexes
  are handled in the ASN environment.  The model could be customized for URI 
  values, though this would require extra work with no crucial advantage.
  It seems like something that could be postponed.

* Competencies and benchmarks get URIs assigned in the ASN repository
  namespace.  If we want to make individual competencies "clickable", such that
  a web page showing the content of a given competency is displayed, we will
  have to look either to the default ASN repository or give some thought to
  generating our own representation of the CI to which the URIs would
  dereference.  However, it is not at all clear how this could work without
  customization given that the URI assignment mechanism defaults to ASN URIs.

* Joseph will put a copy of the JSON representation into the LD4PE Github repo
  this afternoon so that we can start playing with it.

* Tom, Stuart, and Kai briefly discussed how the workflow will need to be
  integrated into the new static-site-based workflow for the DCMI website.  Tom
  raised the possibility of creating a gh-page branch in the LD4PE repo for
  documentation of the LD4PE CI, perhaps using Hugo or Jekyll.  The options
  will need to be discussed with the Infrastructure Advisory Committee.

* I explained to Joseph that we are aiming at finishing this work by July
  and suggested that we have a follow-up call to discuss details,
  once we have all had a chance to play with the tool, sometime in June.
  Joseph agreed.

