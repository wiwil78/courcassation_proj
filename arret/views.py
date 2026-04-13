from django.shortcuts import render, get_object_or_404
from .models import Arret
from .forms import ContactForm
from .forms import ArretForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import Arret, Categorie
from django.db.models import Q

from django.core.mail import send_mail

from .models import TexteJuridique, Titre, Chapitre, Article

from .models import Actualite




def home(request):
     return render(request, 'home.html')

def historique(request):
    # Pou kounye a, ou ka teste ak yon mesaj senp
     return render(request, 'historique.html', {'titre': 'Historique de la Cour de Cassation'})

def presentation(request):
    return render(request, 'presentation.html', {
        'titre': 'Présentation de la Cour de Cassation'
    })



def galerie(request):
    return render(request, 'galerie.html')


# Publication page
from .models import Abonne

def publication(request):
    message = None

    if request.method == 'POST':
        email = request.POST.get('email')

        if email:
            if Abonne.objects.filter(email=email).exists():
                message = "Cette adresse est déjà inscrite."
            else:
                Abonne.objects.create(email=email)
                message = "Merci pour votre abonnement à la lettre d’information."

    return render(request, 'publication.html', {
        'message': message
    })





def enregistrer_arret(request):
    if request.method == 'POST':
        form = ArretForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('enregistrer_arret')  # Ou ka mete paj siksè
    else:
        form = ArretForm()
    return render(request, 'arret/enregistrer_arret.html', {'form': form})




def consulter_arret(request):
    q = request.GET.get('q')
    annee = request.GET.get('annee')
    categorie = request.GET.get('categorie')
    section = request.GET.get('section')

    arrets = Arret.objects.select_related('categorie')

    if q:
        arrets = arrets.filter(
            Q(mots_cles__icontains=q) |
            Q(resume__icontains=q) |
            Q(parties__icontains=q) |
            Q(domaine__icontains=q)
        )

    if annee:
        arrets = arrets.filter(date_arret__year=annee)

    if categorie:
        arrets = arrets.filter(categorie_id=categorie)

    if section:
        arrets = arrets.filter(section__icontains=section)

    categories = Categorie.objects.all()

    return render(request, "arret/consulter_arret.html", {
        "arrets": arrets.order_by('-date_arret'),
        "categories": categories
    })



def detail_arret(request, id):
    """
    Affiche les détails d'un arret spécifique
    """
    arret = get_object_or_404(Arret, id=id)
    context = {
        'arret': arret
    }
    return render(request, 'arret/detail_arret.html', context)




def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()  # Sove nan DB ak statut default "Nouveau"

            # Notifikasyon email (opsyonèl: modifye ak email admin)
            send_mail(
                subject=f"Nouveau message: {contact_message.get_sujet_display()}",
                message=f"Nom: {contact_message.nom}\nEmail: {contact_message.email}\nMessage: {contact_message.message}",
                from_email='no-reply@courcassation.ht',
                recipient_list=['admin@courcassation.ht'],
                fail_silently=True,
            )

            messages.success(request, "Votre message a été envoyé avec succès !")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})



# views.py
from .forms import AbonnementForm

def abonnement(request):
    if request.method == 'POST':
        form = AbonnementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Merci pour votre abonnement.")
            return redirect('abonnement')
    else:
        form = AbonnementForm()

    return render(request, 'abonnement.html', {'form': form})


from django.db.models import Q
from django.shortcuts import render
from .models import Article


def recherche_globale(request):
    q = request.GET.get('q')
    resultats = []

    if q:
        resultats = Article.objects.filter(
            Q(numero__icontains=q) |
            Q(contenu__icontains=q) |
            Q(chapitre__intitule__icontains=q) |
            Q(chapitre__titre__intitule__icontains=q) |
            Q(chapitre__titre__texte__titre__icontains=q)
        )

    return render(request, 'recherche_globale.html', {
        'resultats': resultats,
        'q': q
    })

def constitution_1987(request, langue='fr'):
    texte = TexteJuridique.objects.get(
        type_texte='constitution',
        langue=langue
    )
    return render(request, 'constitution1987.html', {
        'texte': texte
    })

    #pou actualites

    from .models import Actualite

def home(request):
    actualites = Actualite.objects.all()[:5]  # ex: 5 dernières
    return render(request, 'home.html', {
        'actualites': actualites
    })

def evenement_detail(request):
    return render(request, "evenement_detail.html")

def mission(request):
    return render(request, 'mission.html')

def organisation(request):
    return render(request, 'organisation.html')

def procedure(request):
    return render(request, 'procedure.html')