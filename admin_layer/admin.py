
from member.models import EventRequest  
from django.contrib import admin
from member.models import Donation


class EventRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'description')
    actions = ['approve_event', 'reject_event']

    def approve_event(self, request, queryset):
        queryset.update(status='Approved') 

    def reject_event(self, request, queryset):
        queryset.update(status='Rejected')  

admin.site.register(EventRequest, EventRequestAdmin)

admin.site.register(Donation)
