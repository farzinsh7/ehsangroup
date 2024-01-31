from django.contrib import admin
from .models import Industry

# Register your models here.
class IndustryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('thumbnail_tag', 'title', 'status')
    ordering = ['-publish']

admin.site.register(Industry, IndustryAdmin)

