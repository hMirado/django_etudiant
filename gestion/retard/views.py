from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Count, Sum

from retard.models import Retard
from etudiant.models import Etudiant

def index(request):
    return render(request, 'index.html')


def add_retard(request):
    if request.method == 'POST':
        identifiant = request.POST.get('identifiant')
        niveau = request.POST.get('niveau')
        matiere = request.POST.get('matiere')
        semestre = request.POST.get('semestre')

        if identifiant and niveau and matiere and semestre:
            retard = Retard.objects.create(
                identifiant=identifiant,
                niveau=niveau,
                matiere=matiere,
                semestre=semestre
            )

        text = "<div class='w-full bg-green-200' role='alert'><span class='p-3 text-red-800'>Enregistrement effectué avec success.</span></div>"
        messages.success(request, text)
        return redirect('retard:retard')


def update_retard(request, id):
    if request.method == 'POST':
        identifiant = request.POST.get('identifiant')
        niveau = request.POST.get('niveau')
        matiere = request.POST.get('matiere')
        semestre = request.POST.get('semestre')

        if identifiant and niveau and matiere:
            retard = Retard.objects.filter(id=id).update(
                identifiant=identifiant,
                niveau=niveau,
                matiere=matiere,
                semestre=semestre
            )
        text = "<div class='w-full bg-green-200' role='alert'><span class='p-3 text-red-800'>Modification effectué avec success.</span></div>"
        messages.success(request, text)
        return redirect('retard:retard')


### START HOME ###
def retard(request):
    retard = Retard.objects.all()
    #retard = Retard.objects.order_by().values('identifiant').distinct().filter(identifiant='SE2017102')
    etudiant = Etudiant.objects.all().order_by('identifiant')

    context = {
        'retard': retard,
        'etudiant':etudiant
    }

    id = request.POST.get('id')
    if not id:
        add_retard(request)
    else:
        update_retard(request, id)

    return render(request, 'retard/home.html', context)
### END HOME ###


### START DETAIL ###
def detail(request, retard_id):
    #retard = Retard.objects.annotate(count=Count('matiere')).filter(identifiant=retard_id).distinct()
    #retard = Retard.objects.distinct().filter(identifiant=retard_id).annotate(count=Count('matiere'))
    matiere = Retard.objects.distinct().values('matiere', 'niveau', 'semestre').annotate(count=Count('matiere')).filter(identifiant=retard_id)
    semestre = Retard.objects.values('semestre').annotate(sem=Count('matiere')).filter(identifiant=retard_id).order_by('semestre')
    etudiant = get_object_or_404(Etudiant, identifiant=retard_id)

    context = {
        'etudiant_id': etudiant.identifiant,
        'etudiant_lname': etudiant.lname,
        'etudiant_fname': etudiant.fname,
        'matiere': matiere,
        'semestre' : semestre
    }
    return render(request, 'retard/detail.html', context)
### END DETAIL ###
