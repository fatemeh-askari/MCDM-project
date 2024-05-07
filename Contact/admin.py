from django.contrib import admin
from . import models

@admin.register(models.ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created', 'read']
    list_filter = ['read', 'created']
    search_fields = ['name', 'email', 'subject', 'message']
