from django.contrib import admin
from .models import Users
from .models import techque
from .models import commque

admin.site.register(Users)
admin.site.register(techque)
admin.site.register(commque)
