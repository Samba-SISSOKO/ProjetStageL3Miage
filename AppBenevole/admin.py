from django.contrib import admin

from django.contrib import admin
from .models import Personne, Referent_Benevole, Mission, Agenda, EtablissementAccueil


# Register your models here.

admin.site.register(Personne)
class PersonneAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom', 'prenom', 'Ville', 'postale', 'telephone', 'Email', 'Autoriser_a_exercer']

admin.site.register(Referent_Benevole)
class PersonneAdmin(admin.ModelAdmin):
    list_display = ['id', 'id_personne',  'nom', 'prenom', 'disponibilite', 'nbres_personnes_suivi', 'orienter_vers', 'etat_avancement']
admin.site.register(Mission)
admin.site.register(Agenda)
admin.site.register(EtablissementAccueil)

