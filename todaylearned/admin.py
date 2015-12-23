from django.contrib import admin

# Register your models here.
from django.forms import TextInput, Textarea
from django.db import models
from . models import Entry

class EntryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'50'})},
        models.TextField: {'widget': Textarea(attrs={'rows':14, 'cols':150})},    }

    list_filter = ['modified']
    search_fields = ['content']
    
    

admin.site.register(Entry, EntryAdmin)
