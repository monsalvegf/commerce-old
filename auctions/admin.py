from django.contrib import admin


from django.contrib.auth.admin import UserAdmin
from .models import User  # Asegúrate de que esto apunte a tu modelo de usuario personalizado
from .models import Category, Item, Bid, Comment


# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Bid)
admin.site.register(Comment)