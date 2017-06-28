#!/bin/bash 

# This command creates (or refreshes) the website at https://dcmi.github.io/ldci/
# The command must be run from the root directory of the https://github.com/dcmi/ldci/ repo
# MkDocs must be installed - see http://www.mkdocs.org/#installation
# Behind the scenes, MkDocs will build your docs and use the ghp-import tool to commit them 
# to the gh-pages branch and push the gh-pages branch to GitHub.

mkdocs gh-deploy
