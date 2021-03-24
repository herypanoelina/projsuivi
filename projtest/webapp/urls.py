from django.urls import path
from . import views

urlpatterns = [
    path('Menu/', views.login1, name='login1'),
    path('dossier/', views.login4, name='login2'),
    path('dossiermodif/', views.login5, name='login3'),
    path('listedossier/', views.login6, name='login4'),
    path('listedossierCh/', views.login7, name='login5'),
    path('listedossiertri/',views.login8, name='login6'),
    path('ajoutdossier1/',views.login9, name='login7'),
    path('Majdossier1/',views.login10, name='login8'),
    path('Listedossier1/',views.login11, name='login9'),
    path('ListedossierCH/', views.login12, name='login10'),
    path('ListedossierCH1/', views.login13, name='login11'),
    path('ListedossierCH2/', views.login14, name='login12'),
    path('ListedossierCH3/', views.login15, name='login13'),
    path('ListedossierCH4/', views.login16, name='login14'),
    path('ListedossierCH5/', views.login17, name='login15'),
    path('ListedossierCH6/', views.login18, name='login16'),
    path('ListedossierCH7/', views.login19, name='login17'),
    path('ListedossierCH8/', views.login20, name='login17'),
    path('ListedossierCH9/', views.login21, name='login18'),
    path('ListedossierCH10/', views.login22, name='login18'),
    path('ListedossierCH11/', views.login23, name='login19'),
    path('', views.login3, name='login3'),
    path('test/', views.tag_lookup),
    path('test1/', views.geeks_view),
    path('add/', views.saisie1, name='debut'),

]
