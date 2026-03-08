from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, AdminProfile,MedecinProfile,InfirmiereProfile,LaborantinProfile
@receiver(post_save, sender=User)
def create_admin_profile_for_admin_user(sender, instance, created, **kwargs):
    if created and instance.role == 'ADMIN':
        AdminProfile.objects.get_or_create(user=instance)

@receiver(post_save, sender=AdminProfile)
def set_user_role_for_admin_profile(sender, instance, created, **kwargs):
    if created and instance.user.role != 'ADMIN':
        instance.user.role = 'ADMIN'
        instance.user.save()
        
@receiver(post_save, sender=User)
def update_admin_profile_on_role_change(sender, instance, **kwargs):
    if instance.role == 'ADMIN':
        AdminProfile.objects.get_or_create(user=instance)
    else:
        AdminProfile.objects.filter(user=instance).delete()


@receiver(post_save, sender=User)
def create_medecin_profile_for_admin_user(sender, instance, created, **kwargs):
    if created and instance.role == 'MEDECIN':
        MedecinProfile.objects.get_or_create(user=instance)


@receiver(post_save, sender=MedecinProfile)
def set_user_role_for_medecin_profile(sender, instance, created, **kwargs):
    if created and instance.user.role != 'MEDECIN':
        instance.user.role = 'MEDECIN'
        instance.user.save()
        
@receiver(post_save, sender=User)
def update_medecin_profile_on_role_change(sender, instance, **kwargs):
    if instance.role == 'MEDECIN':
        MedecinProfile.objects.get_or_create(user=instance)
    else:
        MedecinProfile.objects.filter(user=instance).delete()


@receiver(post_save, sender=User)
def create_Infirmiere_Profile_for_admin_user(sender, instance, created, **kwargs):
    if created and instance.role == 'INFIRMIERE':
        InfirmiereProfile.objects.get_or_create(user=instance)


@receiver(post_save, sender=InfirmiereProfile)
def set_user_role_for_Infirmiere_Profile(sender, instance, created, **kwargs):
    if created and instance.user.role != 'INFIRMIERE':
        instance.user.role = 'INFIRMIERE'
        instance.user.save()
        
@receiver(post_save, sender=User)
def update_Infirmiere_Profile_on_role_change(sender, instance, **kwargs):
    if instance.role == 'INFIRMIERE':
        InfirmiereProfile.objects.get_or_create(user=instance)
    else:
        InfirmiereProfile.objects.filter(user=instance).delete()


@receiver(post_save, sender=User)
def create_Laborantin_profile_for_admin_user(sender, instance, created, **kwargs):
    if created and instance.role == 'LAB':
        LaborantinProfile.objects.get_or_create(user=instance)


@receiver(post_save, sender=LaborantinProfile)
def set_user_role_for_Laborantin_profile(sender, instance, created, **kwargs):
    if created and instance.user.role != 'LAB':
        instance.user.role = 'LAB'
        instance.user.save()
        
@receiver(post_save, sender=User)
def update_Laborantin_profile_on_role_change(sender, instance, **kwargs):
    if instance.role == 'LAB':
        LaborantinProfile.objects.get_or_create(user=instance)
    else:
        LaborantinProfile.objects.filter(user=instance).delete()



