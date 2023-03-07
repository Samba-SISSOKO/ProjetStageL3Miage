from django.urls import path

from accounts.views import Signup, Logout_user, Login_user

from .views import Accueil, AjouterMission, Personnes, Ajouter_Personne, ModifierMission, Suprimer_Personne, ModifierPersonne, SuprimerMission, mMission, mAgenda, AjouterAgenda, SuprimerAgenda, ModifierAgenda, mReferentBenevole, mEtablissementAccueil, AjouterReferentBenevole, SuprimerReferentBenevole, ModifierReferentBenevole, AjouterEtablissementAccueil, SuprimerEtablissementAccueil, ModifierEtablissemntAccueil

urlpatterns =[

    path('', Accueil.as_view(), name='accueil'),

    path('signup/', Signup, name="signup"),
    path('logout/', Logout_user, name="logout"),
    path('login/', Login_user, name="login"),


     
    path('personne/', Personnes.as_view(), name='personne'),
    path('ajouter-personne/', Ajouter_Personne.as_view(), name='ajouter-personne'),
    path('suprimer-personne/', Suprimer_Personne.as_view(), name='suprimer-personne'),
    path('modifier-personne/<int:id>/', ModifierPersonne.as_view(), name='modifier-personne'),

    path('mission/', mMission.as_view(), name='mission'),
    path('ajouter-mission/', AjouterMission.as_view(), name='ajouter-mission'),
    path('suprimer-mission/', SuprimerMission.as_view(), name='suprimer-mission'),
    path('modifier-mission/<int:id>/', ModifierMission.as_view(), name='modifier-mission'),


    path('agenda/', mAgenda.as_view(), name='agenda'),
    path('ajouter-agenda/', AjouterAgenda.as_view(), name='ajouter-agenda'),
    path('suprimer-agenda/', SuprimerAgenda.as_view(), name='suprimer-agenda'),
    path('modifier-agenda/<int:id>/', ModifierAgenda.as_view(), name='modifier-agenda'),



    path('referent-benevole/', mReferentBenevole.as_view(), name='referent-benevole'),
    path('ajouter-referent-benevole/', AjouterReferentBenevole.as_view(), name='ajouter-referent-benevole'),
    path('suprimer-referent-benevole/', SuprimerReferentBenevole.as_view(), name='suprimer-referent-benevole'),
    path('modifier-referent-benevole/<int:id>/', ModifierReferentBenevole.as_view(), name='modifier-referent-benevole'),


    path('etablissemet-accueil/', mEtablissementAccueil.as_view(), name='etablissemet-accueil'),
    path('ajouter-etablissement-accueil/', AjouterEtablissementAccueil.as_view(), name='ajouter-etablissement-accueil'),
    path('suprimer-etablissement-accueil/', SuprimerEtablissementAccueil.as_view(), name='suprimer-etablissement-accueil'),
    path('modifier-etablissement-accueil/<int:id>/', ModifierEtablissemntAccueil.as_view(), name='modifier-etablissement-accueil'),
    
    
   

    


]