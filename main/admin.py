from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import *


# Register your models here.

@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    mptt_level_indent = 50
    ordering = ['id']

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('name',)
        }


admin.site.register(Product)
admin.site.register(TopWorker)
admin.site.register(Statistics)
admin.site.register(Review)
