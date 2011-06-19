from django.contrib import admin
from django.forms import ModelForm, ModelChoiceField, ModelMultipleChoiceField

from webapp.models import AccessToken

from models import WeavrCliqueGroupMembership


class AccessTokenChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s on %s (%s)"%(obj.weavr_name,
                                obj.prosthetic.server,
                                obj.prosthetic.name)


class WCGMForm(ModelForm):
   weavr_token = AccessTokenChoiceField(AccessToken.objects.all())

   class Meta:
       model = WeavrCliqueGroupMembership


class WeavrCliqueGroupMembershipAdmin(admin.ModelAdmin):
    form = WCGMForm

admin.site.register(WeavrCliqueGroupMembership,
                    WeavrCliqueGroupMembershipAdmin)
