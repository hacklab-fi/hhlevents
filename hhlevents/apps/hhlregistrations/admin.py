# -*- coding: UTF-8 -*-
from django.contrib import admin
from happenings.models import Event as HappeningsEvent
from happenings.admin import EventAdmin as HappeningsEventAdmin
from happenings.admin import CancellationInline

from .models import Event, Person, Registration

class EventAdmin(HappeningsEventAdmin):
    fieldsets = (
        (None, {
            'fields': ('start_date', 'end_date', 'all_day', 'repeat',
                       'end_repeat', 'title', 'description',
                       'created_by', 'extra_url', 'gforms_url',
                       )
        }),
        ('Registrations', {
            'classes': ('collapse',),
            'fields': ( 'require_registration', 'max_registrations', 'close_registrations',
                        'event_cost', 'materials_cost', 'materials_mandatory',
                        'payment_due', 'hide_join_checkbox',
                       )
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

# Remove the happenings event admin
admin.site.unregister(HappeningsEvent)
# And use our own
admin.site.register(Event, EventAdmin)
admin.site.register(Person)
admin.site.register(Registration)

