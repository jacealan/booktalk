from django.contrib import admin
from .models import StoreId

# Register your models here.
class StoreIdAdmin(admin.ModelAdmin):
    list_display = ('userid', 'aladin_id', 'yes24_id', 'ridibooks_id', 'start_date', 'end_date')
    search_fields = ['userid', 'aladin_id', 'yes24_id', 'ridibooks_id']

admin.site.register(StoreId, StoreIdAdmin)
