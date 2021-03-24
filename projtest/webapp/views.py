from django.shortcuts import render

# Create your views here.
from django.template import RequestContext

from django.shortcuts import render
import datetime


def tag_lookup(request):
    # Creating a dictionary of key-value pairs
    dic = {'var1': 300,
           'var2': 200,
           'var3': 300}

    # Calling the render() method to render the request from template_ex.htm page by using the dictionary, dic
    return render(request, "template.html", dic)


from django.shortcuts import render


# create a function
def geeks_view(request):
    # create a dictionary
    context = {
        "data": ["Chef de division", "Centre de verification", "Centre de traitement", "Centre de suivi et archivage"],
    }
    # return response
    return render(request, "geeks.html", context)


def login1(request):
    anarana = request.GET["uname"]
    if request.GET["psw"] == '49a58e87cf2ade6c4d5870e1e0e54aa0':
        return render(request, "menu.html", context_instance=RequestContext(request))


def login2(request):
    return render(request, "demandeur.html")


def login3(request):
    return render(request, "longin.html")


def login4(request):
    return render(request, "dossier.html")


def login5(request):
    return render(request, "dossiermodif.html")


def login6(request):
    return render(request, "listedossier.html")


def login7(request):
    return render(request, "listecheck.html")


def login8(request):
    return render(request, "listdosstri.html")


def login9(request):
    return render(request, "ajoutdoss1.html")


def login10(request):
    return render(request, "majdoss2.html")


def login11(request):
    return render(request, "listecheck1.html", {'titre': 'après récéption des dossiers'})


def login12(request):
    context = {
        "data": ["Centre de verification", "Centre de traitement", "Centre de suivi et archivage"],
        "Titulaire": ["le Chef de division"],
    }
    return render(request, "ajoutdoss2.html", context)


def login13(request):
    context = {
        "data": ["Chef de division", "Centre de traitement", "Centre de suivi et archivage"],
        "Titulaire": ["le Centre de vérification"],
    }
    return render(request, "ajoutdoss2.html", context)


def login14(request):
    context = {
        "data": ["Chef de division", "Centre de vérification", "Centre de suivi et archivage"],
        "Titulaire": ["le Centre de traitement"],
    }
    return render(request, "ajoutdoss2.html",context)


def login15(request):
    context = {
        "data": ["Chef de division", "Centre de vérification", "Centre de traitement"],
        "Titulaire": ["le Centre de suivi et archivage"],
    }
    return render(request, "ajoutdoss2.html", context)


def login16(request):
    return render(request, "listecheck1.html", {'titre': 'après validation du Chef de division'})


def login17(request):
    return render(request, "listecheck1.html", {'titre': 'après validation du  centre de validation'})


def login18(request):
    return render(request, "listecheck1.html", {'titre': 'après validation du centre traitement'})


def login19(request):
    return render(request, "listecheck1.html", {'titre': 'après validation du centre de suivi et archivage'})


def login20(request):
    return render(request, "listecheck2.html")


def login21(request):
    return render(request, "listecheck3.html")


def login22(request):
    return render(request, "listecheck4.html")


def login23(request):
    return render(request, "listecheck5.html")


def saisie1(request):
    anarana = request.GET["uname"]
    motpass = request.GET["psw"]
    if request.GET["psw"] == '9a6babf8051eca3dfa63bbcb01770096' and anarana == 'Suivi':

        return render(request, "menu.html", {"result": anarana})
    else:
        return render(request, "Erreur.html")
