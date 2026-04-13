from django.db import models
from django.contrib.auth.models import User

class Categorie(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Catégorie d'arrêt"
        verbose_name_plural = "Catégories d'arrêts"
        ordering = ['nom']

    def __str__(self):
        return self.nom



class Arret(models.Model):
    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.CASCADE,
        related_name="arrets"
    )

    # CHAM YO
    date_arret = models.DateField()
    section = models.CharField(max_length=200, default="Non défini")
    domaine = models.CharField(max_length=200, default="Non défini")
    mots_cles = models.CharField(max_length=255, default="Non défini")
    parties = models.TextField(default="Non défini")
    decision_attaquee = models.TextField(default="Non défini")
    textes_loi = models.TextField(default="Non défini")
    resume = models.TextField(default="Non défini")
    le_texte = models.TextField(default="Non défini")
    fichier_pdf = models.FileField(upload_to='pdfs/', blank=True, null=True)

    # Chan ki itil pou admin ak rechèch
    reference = models.CharField(max_length=255, unique=True, default="Non défini")
    date_publication = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Arrêt"
        verbose_name_plural = "Arrêts"
        ordering = ['-date_arret', 'reference']

    def __str__(self):
        return f"{self.reference} — {self.categorie.nom}"






class ContactMessage(models.Model):
    STATUT_CHOICES = [
        ('nouveau', 'Nouveau'),
        ('encours', 'En cours'),
        ('traite', 'Traité'),
    ]

    SUJET_CHOICES = [
        ('info', 'Information'),
        ('requete', 'Requête juridique'),
        ('autre', 'Autre'),
    ]

    nom = models.CharField(max_length=150)
    email = models.EmailField()
    telephone = models.CharField(max_length=30, blank=True)
    sujet = models.CharField(
    max_length=30,
    choices=SUJET_CHOICES,
    default='autre'   # <--- default value
)
    message = models.TextField()
    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='nouveau'
    )
    assigne_a = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    date_envoi = models.DateTimeField(auto_now_add=True)
    date_traitement = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.nom} - {self.get_sujet_display()}"

#S'abonner
# models.py
from django.db import models

class Abonne(models.Model):
    email = models.EmailField(unique=True)
    date_inscription = models.DateTimeField(auto_now_add=True)
    actif = models.BooleanField(default=True)

    def __str__(self):
        return self.email


#pour la constitution - page publication

from django.db import models

class TexteJuridique(models.Model):
    TYPE_CHOICES = [
        ('constitution', 'Constitution'),
        ('loi', 'Loi'),
        ('arret', 'Arrêt'),
    ]

    LANGUE_CHOICES = [
        ('fr', 'Français'),
        ('cr', 'Créole'),
    ]

    titre = models.CharField(max_length=255)
    type_texte = models.CharField(max_length=20, choices=TYPE_CHOICES)
    langue = models.CharField(max_length=2, choices=LANGUE_CHOICES, default='fr')
    date_publication = models.DateField()
    est_version_amendee = models.BooleanField(default=False)
    version_de = models.ForeignKey(
        'self', null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='versions'
    )

    def __str__(self):
        return self.titre


class Titre(models.Model):
    texte = models.ForeignKey(TexteJuridique, on_delete=models.CASCADE, related_name='titres')
    numero = models.PositiveIntegerField()
    intitule = models.CharField(max_length=255)

    class Meta:
        ordering = ['numero']


class Chapitre(models.Model):
    titre = models.ForeignKey(Titre, on_delete=models.CASCADE, related_name='chapitres')
    numero = models.PositiveIntegerField()
    intitule = models.CharField(max_length=255)

    class Meta:
        ordering = ['numero']


class Article(models.Model):
    chapitre = models.ForeignKey(Chapitre, on_delete=models.CASCADE, related_name='articles')
    numero = models.PositiveIntegerField(blank=True)
    contenu = models.TextField()

    class Meta:
        ordering = ['numero']

    def save(self, *args, **kwargs):
        if not self.numero:
            self.numero = Article.objects.filter(chapitre=self.chapitre).count() + 1
        super().save(*args, **kwargs)


# pou files d'actualites


class Actualite(models.Model):
    titre = models.CharField(max_length=255)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='actualites/', blank=True, null=True)

    class Meta:
        ordering = ['-date_publication']  # 🔥 le plus récent en premier

    def __str__(self):
        return self.titre
