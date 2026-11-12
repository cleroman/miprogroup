from django.contrib import admin
from django.utils.html import format_html
from .models import SiteSettings, Service, ProcessStep, Partner, News, ProjectRequest

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('hero_title', 'email1', 'phone1')
    
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)

@admin.register(ProcessStep)
class ProcessStepAdmin(admin.ModelAdmin):
    list_display = ('step_number', 'title', 'order')
    list_editable = ('order',)

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('logo_preview', 'name', 'role', 'order')
    list_editable = ('order',)
    search_fields = ('name',)
    
    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="height: 40px; max-width: 80px; object-fit: contain;" />', obj.logo.url)
        return "(Pas de logo)"
    logo_preview.short_description = "Logo"

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

@admin.register(ProjectRequest)
class ProjectRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'email', 'domain', 'created_at')
    readonly_fields = ('name', 'company', 'email', 'phone', 'domain', 'location', 'description', 'budget', 'timeline', 'document', 'created_at')