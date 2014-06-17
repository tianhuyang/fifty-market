from django.contrib import admin
from main.models import Contact



class ContactAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contact._meta.fields]


admin.site.register(Contact, ContactAdmin)