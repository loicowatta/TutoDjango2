'''
Created on 23 févr. 2018

@author: loico
'''
from django.shortcuts import render, redirect
from datetime import datetime


def welcome(request):
       
            
    return render(request, 'welcome.html', 
                  {'la_date':datetime.now})

def login(request):
    #Test de transmission
    if len(request.POST) > 0 :
        #Test de la transmission des données d'intéret
        if ("email" not in request.POST) or ("password" not in request.POST):
            #Création du message d'erreur
            error = "Veuillez entrer un adresse de courrierl et un mot de passe"
            #Renvoi du message d'erreur
            return render(request, "login.html", {"error":error})
        else :
            #affectation des données transmises
            email       = request.POST["email"]
            password    = request.POST["password"]
            #test de la validité des données transmises
            if (email != 'l_owatta@me.com') or (password != 'sabado'):
                #Création du message d'erreur
                error = "adresse de messagerie ou mot de passe incorect"
                return render(request, "login.html", {'error':error})
            else :
                #chargement de la page d'acceuil
                return redirect('/welcome')
    return render(request, 'login.html')