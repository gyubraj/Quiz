from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/',include('quiz.urls')),
    path('api/',include('quiz.api.urls')),
]
