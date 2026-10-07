from django.shortcuts import render, redirect
from .models import Doctor
from .forms import AppointmentForm


def home(request):

    return render(
        request,
        'hospital/home.html'
    )


def doctors(request):

    doctor_list = Doctor.objects.all()

    return render(
        request,
        'hospital/doctors.html',
        {
            'doctors': doctor_list
        }
    )


def book_appointment(request):

    if request.method == 'POST':

        form = AppointmentForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                'appointment_success'
            )

    else:

        form = AppointmentForm()

    return render(
        request,
        'hospital/book_appointment.html',
        {
            'form': form
        }
    )


def book_doctor(request, doctor_id):

    doctor = Doctor.objects.get(
        id=doctor_id
    )

    if request.method == 'POST':

        form = AppointmentForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                'appointment_success'
            )

    else:

        form = AppointmentForm(
            initial={
                'doctor': doctor
            }
        )

    return render(
        request,
        'hospital/book_appointment.html',
        {
            'form': form
        }
    )


def appointment_success(request):

    return render(
        request,
        'hospital/success.html'
    )