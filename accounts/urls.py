from django.urls import path
from . import views
from django.contrib import admin

app_name = 'accounts'
urlpatterns = [
    path('', admin.site.urls),
 ]