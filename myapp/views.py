from django.shortcuts import render,redirect
from .forms import AppointmentForm,ContactForm
from django.contrib import messages


def Home(request):
    return render(request,'home.html')

def About(request):
    return render(request,'about.html')

def Service(request):
    return render(request,'service.html')

def Location(request):
    return render(request,'location.html')

def Bookapp(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')  # Render success page
    else:
        form = AppointmentForm()

    return render(request, 'bookappointment.html', {'form': form})



def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return render(request,'contact.html') 
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})


from django.http import JsonResponse
from .models import Doctor

def get_doctors(request, category):
    doctors = Doctor.objects.filter(specialty=category)
    doctor_list = [{'id': doctor.id, 'name': doctor.name} for doctor in doctors]
    return JsonResponse({'doctors': doctor_list})

from django.shortcuts import render
from .models import Doctors

def doctor_list(request):
    doctors = Doctors.objects.all()
    print(doctors)  # Add this line for debugging
    return render(request, 'doctors.html', {'doctors': doctors})


# views.py
from django.shortcuts import render, redirect
from .models import Doctor
from .forms import AppointmentForm

def bookapp(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # Save appointment logic here
           return redirect('success_page') # Redirect after successful booking
    else:
        # Create an empty form or handle GET parameters
        form = AppointmentForm()

    return render(request, 'bookappointment.html', {
        'form': form,
        'doctors': request.GET.get('doctors'),
        'department': request.GET.get('department'),
    })
