from django.contrib import admin
from .models import Pyme_DB
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class PymeResource(resources.ModelResource):

    class Meta:
        model = Pyme_DB


class PymeAdmin(ImportExportModelAdmin):
    resource_class = PymeResource

admin.site.register(Pyme_DB, PymeAdmin)