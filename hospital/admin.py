import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import (ContactMessage, DownloadItem, Feedback, GalleryImage,
                     JobPosting, NewsPost, Service, SiteSettings, StaffMember)


@admin.action(description="Download selected as CSV (opens in Excel)")
def export_csv(modeladmin, request, queryset):
    meta = modeladmin.model._meta
    names = [f.name for f in meta.fields]
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f'attachment; filename="{meta.model_name}.csv"'
    response.write("\ufeff")  # makes Excel read the file as UTF-8
    writer = csv.writer(response)
    writer.writerow(names)
    for obj in queryset:
        writer.writerow([str(getattr(obj, n)) for n in names])
    return response


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Branding", {"fields": ["hospital_name", "tagline", "logo", "hero_image"]}),
        ("Home page introduction", {"fields": ["intro_title", "intro_text"]}),
        ("About us page", {"fields": ["about_text", "mission", "vision"]}),
        ("Contact details", {"fields": ["address", "phone", "emergency_phone", "email", "working_hours"]}),
    ]

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "icon", "order", "is_active")
    list_editable = ("order", "is_active")


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("__str__", "order")
    list_editable = ("order",)


@admin.register(StaffMember)
class StaffMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "order")
    list_editable = ("order",)


@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ("title", "published_at", "is_published")
    list_filter = ("is_published",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ("title", "department", "deadline", "is_active")
    list_filter = ("is_active", "department")


@admin.register(DownloadItem)
class DownloadItemAdmin(admin.ModelAdmin):
    list_display = ("title", "uploaded_at")


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("created_at", "name", "rating", "email", "phone")
    list_filter = ("rating", "created_at")
    search_fields = ("name", "email", "message")
    actions = [export_csv]


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("created_at", "name", "email", "subject")
    search_fields = ("name", "email", "subject", "message")
    actions = [export_csv]
