from django.contrib import admin

from .models import Deciduous, NameSynonym

admin.site.register(NameSynonym)
admin.site.register(Deciduous)
