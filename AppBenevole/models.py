from distutils.command.upload import upload
from django.db import models


# Create your models here.

class Personne(models.Model):

    Autoriser_a_exercer=(

        ('Oui', 'Oui'),
        ('Non', 'Non'),
        
    )

    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    Ville = models.CharField(max_length=50)
    postale = models.IntegerField()
    telephone = models.IntegerField()
    Email = models.EmailField(max_length=100)
    Autoriser_a_exercer = models.CharField(max_length=50, null=False, choices=Autoriser_a_exercer)

class Mission(models.Model):

    types_mission=(

        ('Autres', 'Autres'),
         ('Formation', 'Formation'),
          ('Traveaux Bâtiments', 'Traveaux Bâtiments'),
          ('Restauration', 'Restauration'),
          ('Accompagnement Scolaire', 'Accompagnement Scolaire'),
          ('Informatique (Web, mobile)', 'Informatique (Web, mobile)'),
          ('Traveaux Ménages', 'Traveaux Ménage'),
          ('Distribution (Aliments, vêtements', 'Distribution (Aliments, vêtements'),
          ('vente, commerce', 'vente, commerce'),
          ('Resources Humaines', 'Resources Humaines'),
          ('Organisation, Gestion de projest', 'Organisation, Gestion de projest'),
          ('Ménages', 'ménages'),
          ('BTP, Logistique, Sécurité, Transport', 'BTP, Logistique, Sécurité, Transport'),
          ('Aide a l''insertion, Parrainges', 'Aide a l''insertion, Parrainges'),
              
    )

    id_personne = models.ForeignKey('Personne', models.DO_NOTHING, db_column='id_personne')
    types_mission = models.CharField(max_length=50, null=False, choices=types_mission)
    ville = models.CharField(max_length=50)
    postale = models.IntegerField()
    mots_cles = models.CharField(max_length=50)

class Agenda(models.Model):
    id_personne = models.ForeignKey('Personne', models.DO_NOTHING, db_column='id_personne')
    id_mission = models.ForeignKey('Mission', models.DO_NOTHING, db_column='id_mission')
    date_debut = models.DateField()
    date_fin = models.DateField()

class Referent_Benevole(models.Model):
    etat_avancement=(

        ('En attente', 'En attente'),
        ('Traiter', 'Traiter'),
        ('Refusé', 'Refusé'),
    )


    id_personne = models.ForeignKey('Personne', models.DO_NOTHING, db_column='id_personne')
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    disponibilite = models.DateField()
    nbres_personnes_suivi = models.IntegerField()
    
    orientations_vers = models.CharField(max_length=50)
    date_orientation = models.DateField()
    etat_avancement = models.CharField(max_length=50, null=False, choices=etat_avancement)

class EtablissementAccueil(models.Model):

    types_activités=(

        ('Autres', 'Autres'),
         ('Formation', 'Formation'),
          ('Traveaux Bâtiments', 'Traveaux Bâtiments'),
          ('Restauration', 'Restauration'),
          ('Accompagnement Scolaire', 'Accompagnement Scolaire'),
          ('Informatique (Web, mobile)', 'Informatique (Web, mobile)'),
          ('Traveaux Ménages', 'Traveaux Ménage'),
          ('Distribution (Aliments, vêtements', 'Distribution (Aliments, vêtements'),
          ('vente, commerce', 'vente, commerce'),
          ('Resources Humaines', 'Resources Humaines'),
          ('Organisation, Gestion de projest', 'Organisation, Gestion de projest'),
          ('Ménages', 'ménages'),
          ('BTP, Logistique, Sécurité, Transport', 'BTP, Logistique, Sécurité, Transport'),
          ('Aide a l''insertion, Parrainges', 'Aide a l''insertion, Parrainges'),
              
    )



    id_personne = models.ForeignKey('Personne', models.DO_NOTHING, db_column='id_personne')
    nom = models.CharField(max_length=50)
    ville = models.CharField(max_length=50)
    postale = models.IntegerField()
    types_activités = models.CharField(max_length=50, null=False, choices=types_activités)



