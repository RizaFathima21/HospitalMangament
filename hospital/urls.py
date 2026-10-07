from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'doctors/',
        views.doctors,
        name='doctors'
    ),

    path(
        'appointment/',
        views.book_appointment,
        name='book_appointment'
    ),

    path(
        'appointment/doctor/<int:doctor_id>/',
        views.book_doctor,
        name='book_doctor'
    ),

    path(
        'appointment/success/',
        views.appointment_success,
        name='appointment_success'
    ),

]