from django.shortcuts import render, redirect
from accounts.models import User
from django.contrib import messages
from .models import AdminProfile


def administrator(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        email = request.POST.get("email")
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")
        date_naissance = request.POST.get("date_naissance")
        telephone = request.POST.get("telephone")
        nom_de_hopital = request.POST.get("nom_de_hopital")
        gender=request.POST.get("gender")
        
        

        if not gender or not nom_de_hopital or not telephone or not date_naissance or not nom or not prenom or not email or not confirm_password or not password or not username:
            
            return render(request, "index.html",{"error":"Veuillez remplir tous les champs.","padding_class":"error_padding"})
        else:
           if User.objects.filter(username=username).exists():
                return render(request, "index.html",{"error":"Le nom d'utilisateur existe déjà.","padding_class":"error_padding"})
           else:
               if password != confirm_password:
                  return render(request, "index.html",{"error":"Le mot de passe ne correspondent pas.","padding_class":"error_padding"})
               else:

                 
                  user = User.objects.create_user(
                      username=username,
                      password=password,
                      email=email,
                      role='ADMIN'
                  )
       
                  user.is_staff = True
                  user.is_superuser = True
                  user.save()
                  AdminProfile.objects.create(
                      user=user,
                      nom=nom,
                      prenom=prenom,
                      nom_de_hopital=nom_de_hopital,
                      telephone=telephone,
                      date_naissance=date_naissance, 
                      gender=gender  
                  )
       
                  messages.success(request, "Connexion reussie.")
                  return redirect("/admin/")

    return render(request, "index.html")

