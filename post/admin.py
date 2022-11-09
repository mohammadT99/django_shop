from django.contrib import admin
from .models import *
# Register your models here.
class postAdmin(admin.ModelAdmin):
    list_display=('titel','slug','status','publish')
    list_filter=('status'  , 'publish')
    search_fields=('titel','slug')
    prepopulated_fields={'slug':('titel',)}
    ordering=['status','publish']

admin.site.register(Post,postAdmin)
admin.site.register(contact)