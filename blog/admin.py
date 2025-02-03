from django.contrib import admin
from import_export.admin import ExportMixin
from import_export import resources
from .models import Blog

class BlogResource(resources.ModelResource):
    class Meta:
        model = Blog

@admin.register(Blog)
class BlogAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = BlogResource
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'author__username')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_at', 'updated_at', 'author')
    ordering = ('-created_at',)
