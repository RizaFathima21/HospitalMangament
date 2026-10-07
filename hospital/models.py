from django.db import models


class Doctor(models.Model):

    name = models.CharField(max_length=100)

    specialization = models.CharField(max_length=100)

    experience = models.PositiveIntegerField()

    phone = models.CharField(max_length=15)

    email = models.EmailField()

    available_days = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Appointment(models.Model):

    STATUS_CHOICES = [

        ('Pending', 'Pending'),

        ('Confirmed', 'Confirmed'),

        ('Completed', 'Completed'),

        ('Cancelled', 'Cancelled'),

    ]


    patient_name = models.CharField(
        max_length=100
    )

    patient_phone = models.CharField(
        max_length=15
    )

    patient_email = models.EmailField()

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE
    )

    appointment_date = models.DateField()

    appointment_time = models.TimeField()

    reason = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return (
            f"{self.patient_name} - "
            f"{self.doctor.name}"
        )