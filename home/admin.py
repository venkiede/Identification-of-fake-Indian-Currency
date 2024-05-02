from django.contrib import admin
from .models import Register

# Register your models here.
@admin.register(Register)   
class RegisterAdmin(admin.ModelAdmin):
    list_display = Register.DisplayFields