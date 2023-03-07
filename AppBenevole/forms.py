from django import forms
from .models import Agenda, EtablissementAccueil, Mission, Personne, Referent_Benevole

class AjouterPersonneForm(forms.ModelForm):

    class Meta:
        model = Personne
        fields = ("nom", "prenom", "Ville", "postale", "telephone", "Email", 
        "Autoriser_a_exercer" )
        widgets = {
            'nom' :forms.TextInput(attrs={'class': 'form-control'}),
            'prenom' :forms.TextInput(attrs={'class': 'form-control'}),
            'Ville' :forms.TextInput(attrs={'class': 'form-control'}),
            'postale' :forms.NumberInput(attrs={'class': 'form-control'}),
            'telephone' :forms.NumberInput(attrs={'class': 'form-control'}),
            'Email' :forms.EmailInput(attrs={'class': 'form-control'}),
            'Autoriser_a_exercer' :forms.Select(attrs={'class':'form-control'}),
            
        }

class AjouterMissionForm(forms.ModelForm):
    class Meta:

        model = Mission
        fields = ("id_personne", "types_mission", "ville", "postale", "mots_cles")
        widgets = {
            'id_personne' : forms.NumberInput(attrs={'class': 'form-control'}),
            'types_mission' :forms.Select(attrs={'class': 'form-control'}),
            'ville' : forms.TextInput(attrs={'class': 'form-control'}),
            'postale' : forms.NumberInput(attrs={'class': 'form-control'}),
            'mots_cles' : forms.TextInput(attrs={'class': 'form-control'}),
            
        }

class AjouterAgendaForm(forms.ModelForm):
    class Meta:

        model = Agenda
        fields = ("id_personne", "id_mission", "date_debut", "date_fin")
        widgets = {
            'id_personne' : forms.NumberInput(attrs={'class': 'form-control'}),
            'id_mission' :forms.NumberInput(attrs={'class': 'form-control'}),
            'date_debut' : forms.DateInput(attrs={'class': 'form-control'}),
            'date_fin' : forms.DateInput(attrs={'class': 'form-control'}),
            
            
        }


class AjouterReferentBenevoleForm(forms.ModelForm):
    class Meta:

        model = Referent_Benevole
        fields = ("id_personne", "nom", "prenom", "disponibilite", "nbres_personnes_suivi", "orientations_vers",
         "date_orientation", "etat_avancement")
        widgets = {
            'id_personne' : forms.NumberInput(attrs={'class': 'form-control'}),
            'nom' :forms.TextInput(attrs={'class': 'form-control'}),
            'prenom' : forms.TextInput(attrs={'class': 'form-control'}),
            "disponibilite" : forms.DateInput(attrs={'class': 'form-control'}),
            'nbres_personnes_suivi' : forms.NumberInput(attrs={'class': 'form-control'}),
            
            'orientations_vers' : forms.TextInput(attrs={'class': 'form-control'}),
            'date_orientation' : forms.DateTimeInput(attrs={'class': 'form-control'}),
            'etat_avancement' : forms.Select(attrs={'class': 'form-control'}),
            
            
        }

class AjouterEtablissementAccueilForm(forms.ModelForm):
    class Meta:

        model = EtablissementAccueil
        fields = ("id_personne", "nom", "ville", "postale", "types_activités")
        widgets = {
            'id_personne' : forms.NumberInput(attrs={'class': 'form-control'}),
            'nom' :forms.TextInput(attrs={'class': 'form-control'}),
            'ville' : forms.TextInput(attrs={'class': 'form-control'}),
            'postale' : forms.NumberInput(attrs={'class': 'form-control'}),
            'types_activités' : forms.Select(attrs={'class': 'form-control'}),
            
            
            
        }
