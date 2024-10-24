from django.contrib import admin
from.models import Flight,Airport,Passenger


class FlightAdmin(admin.ModelAdmin):
    list_display = ("id","origin","destination","duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

#给admin我想用admin app来管理这个2个class
admin.site.register(Flight,FlightAdmin)
admin.site.register(Airport)    
admin.site.register(Passenger,PassengerAdmin)
# Register your models here.
