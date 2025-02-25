from django import forms
from .models import Appointment,ContactMessage

from django import forms
from .models import Appointment, Doctor

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'phone_number', 'category', 'doctor', 'date', 'time', 'symptoms']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # If category is already selected, filter doctors based on it
        if 'category' in self.data:
            try:
                category = self.data.get('category')
                self.fields['doctor'].queryset = Doctor.objects.filter(specialty=category)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            # If instance exists, filter doctors based on the category of the instance
            self.fields['doctor'].queryset = self.instance.category.doctor_set.all()


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your Name', 
                'class': 'vg', 
                'required': 'required'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Your Email', 
                'class': 'vg', 
                'required': 'required'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Your Phone', 
                'class': 'vg', 
                'required': 'required'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Your Message', 
                'class': 'cd', 
                'rows': 4, 
                'required': 'required'
            }),
        }

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        return phone