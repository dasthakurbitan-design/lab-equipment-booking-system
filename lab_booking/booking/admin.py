from django.contrib import admin
from .models import Equipment, Booking, LabBooking

admin.site.register(Equipment)
admin.site.register(Booking)        # 👈 ADD THIS
admin.site.register(LabBooking)     # 👈 ADD THIS