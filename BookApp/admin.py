from django.contrib import admin
from BookApp.models import UsedBooks, RegisteredUsers

# Register your models here.
admin.site.register(UsedBooks)
admin.site.register(RegisteredUsers)