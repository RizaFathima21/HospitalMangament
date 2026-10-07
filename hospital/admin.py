from django.contrib import admin
from .models import Doctor, Appointment


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'specialization',
        'experience',
        'phone',
        'available_days',
    )

    search_fields = (
        'name',
        'specialization',
    )


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = (
        'patient_name',
        'doctor',
        'appointment_date',
        'appointment_time',
        'status',
    )

    list_filter = (
        'status',
        'appointment_date',
        'doctor',
    )

    search_fields = (
        'patient_name',
        'patient_phone',
        'patient_email',
    )