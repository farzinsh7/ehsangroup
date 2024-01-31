from django.contrib import admin
from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('thumbnail_tag', 'title', 'status')
    ordering = ['-publish']

admin.site.register(Company, CompanyAdmin)
