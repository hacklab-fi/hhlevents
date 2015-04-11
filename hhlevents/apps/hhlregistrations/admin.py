from django.contrib import admin
from happenings.admin import EventAdmin as HappeningsEventAdmin
from happenings.admin import CancellationInline

from .models import Event, Person, Registration

class EventAdmin(HappeningsEventAdmin):
    fieldsets = (
        (None, {
            'fields': ('start_date', 'end_date', 'all_day', 'repeat',
                       'end_repeat', 'title', 'description',
                       'created_by', 'max_registrations', 
                       'extra_url', 'gforms_url')
        }),
        ('Location', {
            'classes': ('collapse',),
            'fields': ('location',)
        }),
        ('Category', {
            'classes': ('collapse',),
            'fields': ('categories',)
        }),
        ('Tag', {
            'classes': ('collapse',),
            'fields': ('tags',)
        }),
        ('Color', {
            'classes': ('collapse',),
            'fields': (
                ('background_color', 'background_color_custom'),
                ('font_color', 'font_color_custom'),
            )
        }),
    )

    list_display = ('title', 'start_date', 'end_date', 'repeat', 'end_repeat')
    list_filter = ['start_date']
    search_fields = ['title']
    date_hierarchy = 'start_date'
    inlines = [CancellationInline]


admin.site.register(Event, EventAdmin)
admin.site.register(Person)
admin.site.register(Registration)
