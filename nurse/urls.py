from django.urls import path
from . import views
from django.contrib import admin




app_name = 'nurse'
urlpatterns = [
    path('', admin.site.urls),
 ]