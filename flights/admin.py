from django.contrib import admin
from .models import Flight


# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Airline Information', {'fields': ['airline', 'flight_number']}),
        ('Origin/Destination', {'fields': ['origin', 'destination']}),
        ('Departure and Arrival Time', {'fields': ['departure', 'arrival'], 'classes': ['collapse']})
    ]


admin.site.register(Flight, FlightAdmin)
