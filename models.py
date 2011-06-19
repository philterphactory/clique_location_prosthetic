from django.db import models


class WeavrCliqueGroupMembership(models.Model):
    """Group Weavrs, so only Weavrs in the same group communicate"""
    group = models.IntegerField()
    weavr_token = models.ForeignKey('webapp.AccessToken', verbose_name='weavr',
                                    related_name='clique_group_weavr_token')

    def __str__(self):
        return "%i: %s" % (self.group, self.weavr_token.weavr_name)


def weavrs_in_group(group):
    """Get all the Weavrs in the group"""
    return WeavrCliqueGroupMembership.objects.filter(group=group)
