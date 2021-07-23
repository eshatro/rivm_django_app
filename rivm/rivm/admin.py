from django.contrib import admin
from .models import Geography, Entry, Indicator, Impact

# Register your models here.

admin.site.register(Geography)
admin.site.register(Entry)
admin.site.register(Indicator)
admin.site.register(Impact)
