# forms.py
from django import forms
from .models import Arret

from .models import ContactMessage


from .models import Abonne


from .models import Arret

class ArretForm(forms.ModelForm):
    class Meta:
        model = Arret
        fields = [
            'reference', 'categorie', 'date_arret', 'section', 'domaine',
            'mots_cles', 'parties', 'decision_attaquee', 'textes_loi',
            'resume', 'le_texte', 'fichier_pdf'
        ]
        widgets = {
            'date_arret': forms.DateInput(attrs={'type': 'date'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['nom', 'email', 'telephone','sujet','message']

        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Entrez votre nom'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Entrez votre email'
            }),

            'telephone': forms.TextInput(attrs={'placeholder': 'Ex: +509 1234 5678'}),

            'sujet': forms.Select(attrs={}),
        
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Votre message...',
                'rows': 5
            }),

            
        }

#S'abonner
# forms.py

class AbonnementForm(forms.ModelForm):
    class Meta:
        model = Abonne
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Entrez votre email'
            })
        }
