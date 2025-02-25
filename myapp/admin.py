from django.contrib import admin

# admin.site.register(Appointment)
from .models import Doctor, ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "submitted_at")
    list_filter = ("submitted_at",)

admin.site.register(Doctor)



from django.contrib import admin
from .models import Doctors

from django.contrib import admin
from django.utils.html import format_html
from .models import Doctors

class DoctorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'department', 'image_tag', 'description')
    search_fields = ('name', 'specialty')
    list_filter = ('specialty', 'department')
    fields = ('name', 'specialty', 'department', 'image', 'description')

    def image_tag(self, obj):
        if obj.image:  # Check if image exists
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        else:
            return 'No Image'  # Or some other placeholder

    image_tag.short_description = 'Image'

admin.site.register(Doctors, DoctorsAdmin)
