from django.db import models
from cloudinary.models import CloudinaryField

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=50, choices=[
        ('General', 'General'),
        ('Cardiology', 'Cardiology'),
        ('Gastroenterology', 'Gastroenterology'),
        ('Nephrology', 'Nephrology'),
        ('Orthopaedics','Orthopaedics')
    ])

    def __str__(self):
        return f"{self.name} ({self.specialty})"

class Appointment(models.Model):
    CATEGORIES = [
        ('General', 'General'),
        ('Cardiology', 'Cardiology'),
         ('Gastroenterology', 'Gastroenterology'),
        ('Nephrology', 'Nephrology'),
        ('Orthopaedics','Orthopaedics')

    ]
    
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    category = models.CharField(max_length=50, choices=CATEGORIES)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    symptoms = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.category} - {self.date}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Message from {self.name} ({self.email})"
    


class Doctors(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    image = CloudinaryField('image')
    description = models.TextField()

    def __str__(self):
        return self.name 