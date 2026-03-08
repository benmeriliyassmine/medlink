from django.contrib import admin
from django.contrib.auth.models import Group
from .models import InfirmiereProfile
@admin.register(InfirmiereProfile)
class InfirmiereProfile(admin.ModelAdmin):
    list_display=("user__username",'user__first_name',"user__last_name",'user__genre')
    search_fields=("user__username",'user__first_name',"user__last_name")