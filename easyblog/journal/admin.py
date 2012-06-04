from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from easyblog.journal.models import Entry, Category, Tag

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'excerpt', 'date', 'published')
    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(attrs={
                'rows': 20,
                'cols': 80
    })}}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Entry, EntryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)

