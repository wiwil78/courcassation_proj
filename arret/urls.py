from django.urls import path
from . import views
from .views import contact

urlpatterns = [
    path('', views.home, name='home'),
    path('mission/', views.mission, name='mission'),
    path('organisation/', views.organisation, name='organisation'),
    path('procedure/', views.procedure, name='procedure'),
    path('historique/', views.historique, name='historique'),
    path('presentation/', views.presentation, name='presentation'),
    path('galerie/', views.galerie, name='galerie'),
    path('publication/', views.publication, name='publication'),
    path('contact', views.contact, name="contact"),
    path('enregistrer_arret/', views.enregistrer_arret, name='enregistrer_arret'),
    path('consulter_arret/', views.consulter_arret, name='consulter_arret'),
    path('arrets/<int:id>/', views.detail_arret, name='detail_arret'),
    path(
        'constitution-1987/<str:langue>/',
        views.constitution_1987,
        name='constitution_1987'  # <- NON LA OBLIGATWA
    ),
    path(
        'recherche/',
        views.recherche_globale,
        name='recherche_globale'
    ),

    
    path("evenements/rentree-judiciaire-2025-2026/",
         views.evenement_detail,
         name="evenement_detail"),
   

]



