from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

import models


def get_token_location(weavr_token):
    """Get the Weavr's location, or None if no location yet"""
    location = None
    locations = weavr_token.get_json("/1/weavr/location/")['locations']
    if len(locations) > 0:
        location = locations[0]
    else:
        logging.info("no location found")
    return location


def info_for_weavrs(weavrs):
    """Build a list of information dicts describing each Weavr's position"""
    infos = []
    for weavr in weavrs:
        weavr_token = weavr.weavr_token
        location = get_token_location(weavr_token)
        if location:
            infos.append({"name":weavr_token.weavr_name, 
                          "url": weavr_token.weavr_url,
                          "latitude":location['lat'],
                          "longitude":location['lon']})
    return infos


@login_required()
def show_group_locations(request, group_number):
    """Render a Google Map showing the locations of the group"""
    weavrs = models.weavrs_in_group(group_number)
    infos = info_for_weavrs(weavrs)
    return render_to_response("display_locations.html",
                              {"weavrs": infos},
                              context_instance=RequestContext(request))
