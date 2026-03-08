from django.urls import path
from . import views
from django.contrib import admin




app_name = 'laboratory'
urlpatterns = [
    path('', admin.site.urls),
 ]