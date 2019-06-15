from django.contrib import admin
from .. import models

# Import your custom admin classes here.
from .user import UserAdmin


admin.site.register(models.User, user.UserAdmin)
