from django.contrib import admin
from showmessages.models import UserModel
# Register your models here.
@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ["name","email","password"]