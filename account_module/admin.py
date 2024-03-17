from django.contrib import admin

# Register your models here.
from account_module.models import User , AbilityUser , user_education

admin.site.register(User)
admin.site.register(AbilityUser)
admin.site.register(user_education)
