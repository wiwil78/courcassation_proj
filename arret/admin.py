from django.contrib import admin
from .models import Categorie, Arret
from .models import ContactMessage


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description')
    search_fields = ('nom',)
    ordering = ('nom',)



@admin.register(Arret)
class ArretAdmin(admin.ModelAdmin):

    # Kolòn nan lis la
    list_display = (
        'reference',
        'categorie',
        'date_arret',
        'section',
        'domaine',
        'mots_cles',
        'fichier_pdf_link',
    )

    # Filtè
    list_filter = (
        'categorie',
        'domaine',
        'section',
        ('date_arret', admin.DateFieldListFilter),
    )

    # Chèche
    search_fields = (
        'reference',
        'parties',
        'mots_cles',
        'resume',
        'textes_loi',
        'decision_attaquee',
        'le_texte',
    )

    ordering = ('-date_arret', 'reference')

    # Fòm admin nan — TOUT CHAN YO ANNDAN YO
    fieldsets = (
        ("IDENTIFICATION", {
            'fields': (
                'reference',
                'categorie',
                'date_arret',
                'section',
                'domaine',
                'mots_cles',
            )
        }),

        ("PARTIES ET CONTEXTE", {
            'fields': (
                'parties',
                'decision_attaquee',
                'textes_loi',
            )
        }),

        ("CONTENU DE L'ARRÊT", {
            'fields': (
                'resume',
                'le_texte',
            )
        }),

        ("DOCUMENT", {
            'fields': ('fichier_pdf',)
        }),

        ("SYSTEME", {
            'classes': ('collapse',),
            'fields': ('date_publication',),
        }),
    )

    readonly_fields = ('date_publication',)

    # Lyen PDF
    def fichier_pdf_link(self, obj):
        if obj.fichier_pdf:
            return f"📄 Télécharger"
        return "—"
    fichier_pdf_link.short_description = "PDF"


# page contact



@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'telephone', 'sujet', 'message','statut', 'assigne_a', 'date_envoi', 'date_traitement')
    list_filter = ('statut', 'sujet')
    search_fields = ('nom', 'email', 'telephone', 'message')
    
    actions = ['mark_as_traited']

    def mark_as_traited(self, request, queryset):
        queryset.update(statut='Traité', date_traitement=timezone.now())
        self.message_user(request, "Messages marqués comme Traité.")
    mark_as_traited.short_description = "Marquer comme Traité"


# admin.py
from django.contrib import admin
from .models import Abonne

@admin.register(Abonne)
class AbonneAdmin(admin.ModelAdmin):
    list_display = ('email', 'actif', 'date_inscription')
    list_filter = ('actif', 'date_inscription')
    search_fields = ('email',)

#pourla constitution
from django.contrib import admin
from .models import TexteJuridique, Titre, Chapitre, Article

admin.site.register(TexteJuridique)
admin.site.register(Titre)
admin.site.register(Chapitre)
admin.site.register(Article)

#pour actualites

from django.contrib import admin
from .models import Actualite

@admin.register(Actualite)
class ActualiteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_publication')
    ordering = ('-date_publication',)
