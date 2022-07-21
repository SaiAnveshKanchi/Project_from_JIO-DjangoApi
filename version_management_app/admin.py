
from django.contrib import admin

from version_management_app.models import Data, Device,Version,DateSent

# Register your models here.
admin.site.register(Version)
admin.site.register(Device)
admin.site.register(Data)
admin.site.register(DateSent)