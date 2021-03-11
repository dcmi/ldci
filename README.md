### Linked Data Competency Index

This is the back-end repository used to generate a [documentation website](https://dcmi.github.io/ldci/) for the Linked Data Competency Index.  The website also supports the maintenance of the index by crowdsourcing.

#### Build the website using MkDocs

* Install [mkdocs](http://mkdocs.org) on your machine (see [installation instructions](http://www.mkdocs.org/#installation).
* Run the command `mkdocs gh-deploy` (or use [deploy.sh](https://github.com/dcmi/ldci/blob/master/deploy.sh)).  
    * This command creates (or refreshes) the website at [https://dcmi.github.io/ldci/](https://dcmi.github.io/ldci/).  
    * The command must be run from the root directory of this repo.  
    * Behind the scenes, `mkdocs gh-deploy` builds HTML docs from the Markdown sources, uses the `ghp-import` tool to commit them to the `gh-pages` branch, and pushes the `gh-pages` branch to GitHub.

