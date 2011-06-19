The Clique Map [Prosthetic](http://developer.weavrs.com/) for [Weavrs](http://weavrs.com/) displays maps of groups of Weavrs.

# Installation

The Clique Map Prosthetic for Weavrs uses the prosthetic-runner system to run on Google App Engine.

You can download prosthetic-runner [here](https://github.com/philterphactory/prosthetic-runner), along with instructions on how to install a Prosthetic such as this one into it. Particularly see the section "Adding a prosthetic to the server" near the bottom of the page.

You will need to add the following new index to index.yaml in prosthetic-runner:

- kind: clique_weavrcliquegroupmembership
  properties:
  - name: __key__
    direction: desc

You will also need to add the Prosthetic's urls to the main urls.py :

(r'^clique/', include('clique_location_prosthetic.urls')),

Once you have prosthetic-runner and this Prosthetic installed, you can attach this Prosthetic to your Weavrs.
