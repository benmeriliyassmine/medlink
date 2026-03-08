from django.contrib import admin
from django.contrib.auth.models import Group
from administrator.models import Service,AdminProfile
from administrator.models import User
@admin.register(User)
class User(admin.ModelAdmin):
    list_display=("username",'first_name','last_name','genre')
    search_fields=('first_name','last_name',"username")

admin.site.register(Service)
admin.site.unregister(Group)
@admin.register(AdminProfile)
class AdminProfile(admin.ModelAdmin):
    list_display=("user__username",'user__first_name',"user__last_name",'user__genre')
