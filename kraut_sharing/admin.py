# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

from django.contrib import admin
from kraut_sharing.models import TAXII_Remote_Server, TAXII_Remote_Collection

# Register your models here.

admin.site.register(TAXII_Remote_Server)
admin.site.register(TAXII_Remote_Collection)
