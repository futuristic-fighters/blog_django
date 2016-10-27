from django.contrib import admin
from account.models import UserModel


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    exclude = ["article"]

admin.site.register(UserModel)
