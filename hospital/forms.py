from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):

    class Meta:

        model = Appointment

        fields = [
            'patient_name',
            'patient_phone',
            'patient_email',
            'doctor',
            'appointment_date',
            'appointment_time',
            'reason',
        ]

        widgets = {

            'patient_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter patient name'
                }
            ),

            'patient_phone': forms.TextInput(
                attrs={
                    'placeholder': 'Enter phone number'
                }
            ),

            'patient_email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter email'
                }
            ),

            'appointment_date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'appointment_time': forms.TimeInput(
                attrs={
                    'type': 'time'
                }
            ),

            'reason': forms.Textarea(
                attrs={
                    'placeholder': 'Reason for appointment',
                    'rows': 4
                }
            ),
        }