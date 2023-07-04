from django.contrib import admin


from django.contrib.auth.admin import UserAdmin
from .models import User  # Asegúrate de que esto apunte a tu modelo de usuario personalizado



# Register your models here.

admin.site.register(User, UserAdmin)