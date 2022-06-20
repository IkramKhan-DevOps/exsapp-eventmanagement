from django.contrib import admin

from .models import (
    AddOn, Venue, EventType, Event, Video

)


class AddOnAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'price', 'is_active'
    ]


class VenueAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'is_active'
    ]


class EventTypeAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'is_active'
    ]


class EventAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user', 'event_type', 'venue', 'event_charge', 'venue_charge', 'total_charge',
        'tax_charge', 'is_paid', 'is_active', 'created_on'
    ]


class VideoAdmin(admin.ModelAdmin):
    list_display = [
         'caption','description','video' 
    ]


admin.site.register(AddOn, AddOnAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventType, EventTypeAdmin)
admin.site.register(Video,VideoAdmin)