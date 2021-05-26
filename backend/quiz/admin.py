from django.contrib import admin
from .models import Question,Answer,Choice
# Register your models here.

admin.site.register([Question,Answer,Choice])