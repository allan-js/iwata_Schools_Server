from django.urls import path
from django.contrib import admin
from django.shortcuts import render
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import StudentWork

class StudentWorkAdmin(admin.ModelAdmin):
    list_display = ('student', 'name', 'created', 'file_preview', 'view_full')
    search_fields = ('name', 'student')
    list_filter = ('created', 'is_archived')
    list_per_page = 50

    def file_preview(self, obj):
        if obj.file:
            file_url = obj.file.url
            if obj.file.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', file_url)
            elif obj.file.name.lower().endswith('.pdf'):
                return format_html('<embed src="{}" type="application/pdf" width="100" height="100"/>', file_url)
            elif obj.file.name.lower().endswith(('.mp4', '.webm', '.ogg')):
                return format_html(
                    '<video width="100" height="100" controls><source src="{}" type="video/mp4"></video>',
                    file_url,
                )
        return "No Preview Available"
    file_preview.short_description = "Preview"

    def view_full(self, obj):
        return format_html('<a href="{}" target="_blank">View Full</a>', f'view-work/{obj.id}/')
    view_full.short_description = "Full View"

    # Custom admin view for full work display
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('view-work/<int:pk>/', self.admin_site.admin_view(self.view_work), name='view_work'),
        ]
        return custom_urls + urls

    def view_work(self, request, pk):
        obj = self.get_object(request, pk)
        context = {
            'title': f'Viewing {obj.name}',
            'file_url': obj.file.url,
            'file_type': obj.file.name.split('.')[-1].lower(),
            'object': obj,
        }
        return render(request, 'admin/core/view_work.html', context)

admin.site.register(StudentWork, StudentWorkAdmin)