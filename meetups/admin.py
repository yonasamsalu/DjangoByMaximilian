from django.contrib import admin

from meetups.models import Meet, Location, Participant

# Register your models here.

class MeetAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description', 'date', 'location', 'image')
    list_filter = ('location', 'date' )
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Meet, MeetAdmin)
admin.site.register(Location)
admin.site.register(Participant)
