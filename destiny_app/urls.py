from django.contrib import admin
from django.urls import path, include
from destiny_website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('destiny_website.urls')),
]
