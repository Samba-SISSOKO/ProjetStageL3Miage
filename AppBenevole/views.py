from django.shortcuts import render, redirect

from django.views import View
from .models import Personne, Mission, Agenda, Referent_Benevole, EtablissementAccueil
from .forms import AjouterPersonneForm, AjouterMissionForm, AjouterAgendaForm, AjouterReferentBenevoleForm, AjouterEtablissementAccueilForm

# Create your views here.

class Accueil(View):
    def get(self, request):
        return render(request, 'AppBenevole/accueil.html')


class Personnes(View):
    def get(self, request):
        personne_data = Personne.objects.all()
        return render(request, 'AppBenevole/personne.html', {'personne' : personne_data})
   
class Ajouter_Personne(View):

    def get(self, request):
        fm = AjouterPersonneForm()
        
        return render(request, 'AppBenevole/ajouter-personne.html', {'form':fm})

    def post(self, request):
        fm = AjouterPersonneForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'AppBenevole/ajouter-personne.html', {'form': fm})

class Suprimer_Personne(View):


    def post(self, request):
        data = request.POST
        id = data.get('id')
        datapersonne = Personne.objects.get(id=id)
        datapersonne.delete()
        return redirect('/')

class ModifierPersonne(View):
    def get(self, request, id):

        personne = Personne.objects.get(id=id)
        fm= AjouterPersonneForm(instance=personne)
        
        return render(request, 'AppBenevole/modifier-personne.html',  {'form':fm} )
    
    def post(self, request, id):
        personne = Personne.objects.get(id=id)
        fm= AjouterPersonneForm(request.POST, instance=personne)
        if fm.is_valid():
            fm.save()
            return redirect('/')


class mMission(View):
    def get(self, request):
        mission_data = Mission.objects.all()
        return render(request, "AppBenevole/mission.html", {'mission' : mission_data})

class AjouterMission(View):
     def get(self, request):
        fp = AjouterMissionForm()

        return render(request, 'AppBenevole/ajouter-mission.html', {'form':fp} )

     def post(self, request):
        fp = AjouterMissionForm(request.POST)
        if fp.is_valid():
            fp.save()
            return redirect('/')
        else:
            return render(request, 'AppBenevole/ajouter-mission.html', {'form': fp})

class SuprimerMission(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        datamission = Mission.objects.get(id=id)
        datamission.delete()
        return redirect('/')

class ModifierMission(View):
     def get(self, request, id):

        mission = Mission.objects.get(id=id)
        fp= AjouterMissionForm(instance=mission)

        return render(request, 'AppBenevole/modifier-mission.html',  {'form':fp} )

     def post(self, request, id):
        mission = Mission.objects.get(id=id)
        fp= AjouterMissionForm(request.POST, instance=mission)
        if fp.is_valid():
            fp.save()
            return redirect('/')


class mAgenda(View):
    def get(self, request):
        agenda_data = Agenda.objects.all()
        return render(request, "AppBenevole/agenda.html", {'agenda' : agenda_data})

class AjouterAgenda(View):

   
    def get(self, request):
        fm = AjouterAgendaForm()

        return render(request, 'AppBenevole/ajouter-agenda.html', {'form':fm} )

    def post(self, request):
        fm = AjouterAgendaForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'AppBenevole/ajouter-agenda.html', {'form': fm})

class SuprimerAgenda(View):


    def post(self, request):
        data = request.POST
        id = data.get('id')
        agenda_data = Agenda.objects.get(id=id)
        agenda_data.delete()
        return redirect('/')

class ModifierAgenda(View):

    def get(self, request, id):

        agenda = Agenda.objects.get(id=id)
        fm= AjouterAgendaForm(instance=agenda)

        return render(request, 'AppBenevole/modifier-agenda.html',  {'form':fm} )

    def post(self, request, id):
        agenda = Agenda.objects.get(id=id)
        fm= AjouterAgendaForm(request.POST, instance=agenda)
        if fm.is_valid():
            fm.save()
            return redirect('/')


class mReferentBenevole(View):
    def get(self, request):
        referent_benevole_data = Referent_Benevole.objects.all()
        return render(request, "AppBenevole/referent-benevole.html", {'referent_benevole' : referent_benevole_data})

class AjouterReferentBenevole(View):

   
    def get(self, request):
        fm = AjouterReferentBenevoleForm()

        return render(request, 'AppBenevole/ajouter-referent-benevole.html', {'form':fm} )

    def post(self, request):
        fm = AjouterReferentBenevoleForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'AppBenevole/ajouter-referent-benevole.html', {'form': fm})

class SuprimerReferentBenevole(View):


    def post(self, request):
        data = request.POST
        id = data.get('id')
        referent_benevole_data = Referent_Benevole.objects.get(id=id)
        referent_benevole_data.delete()
        return redirect('/')

class ModifierReferentBenevole(View):

    def get(self, request, id):

        referent_benevole = Referent_Benevole.objects.get(id=id)
        fm= AjouterReferentBenevoleForm(instance=referent_benevole)

        return render(request, 'AppBenevole/modifier-referent-benevole.html',  {'form':fm} )

    def post(self, request, id):
        referent_benevole = Referent_Benevole.objects.get(id=id)
        fm= AjouterReferentBenevoleForm(request.POST, instance=referent_benevole)
        if fm.is_valid():
            fm.save()
            return redirect('/')


class mEtablissementAccueil(View):
    def get(self, request):
        etablissementaccueil_data = EtablissementAccueil.objects.all()
        return render(request, "AppBenevole/etablissement-accueil.html", {'etablissementaccueil' : etablissementaccueil_data})

class AjouterEtablissementAccueil(View):

   
    def get(self, request):
        fm = AjouterEtablissementAccueilForm()

        return render(request, 'AppBenevole/ajouter-etablissement-accueil.html', {'form':fm} )

    def post(self, request):
        fm = AjouterEtablissementAccueilForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'AppBenevole/ajouter_etablissementaccueil.html', {'form': fm})

class SuprimerEtablissementAccueil(View):


    def post(self, request):
        data = request.POST
        id = data.get('id')
        etablissementaccueil_data = EtablissementAccueil.objects.get(id=id)
        etablissementaccueil_data.delete()
        return redirect('/')

class ModifierEtablissemntAccueil(View):

    def get(self, request, id):

        etablissementaccueil = EtablissementAccueil.objects.get(id=id)
        fm= AjouterEtablissementAccueilForm(instance=etablissementaccueil)

        return render(request, 'AppBenevole/modifier-etablissement-accueil.html',  {'form':fm} )

    def post(self, request, id):
        etablissementaccueil = EtablissementAccueil.objects.get(id=id)
        fm= AjouterEtablissementAccueilForm(request.POST, instance=etablissementaccueil)
        if fm.is_valid():
            fm.save()
            return redirect('/')

