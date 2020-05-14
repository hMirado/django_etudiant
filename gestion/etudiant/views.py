from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction

from .forms import EtudiantForm, ContactForm, ParentForm

from .models import Etudiant, Parent, Contact, v_etudiant_info

def index(request):
    return render(request, 'index.html')


def add_etudiant(request):
    if request.method == 'POST':
        etudiant_form = EtudiantForm(request.POST)
        contact_form = ContactForm(request.POST)
        parent_form = ParentForm(request.POST)

        if etudiant_form.is_valid() & contact_form.is_valid() & parent_form.is_valid():
            identifiant = etudiant_form.cleaned_data['identifiant']
            fname = etudiant_form.cleaned_data['fname']
            lname = etudiant_form.cleaned_data['lname']
            birthday = etudiant_form.cleaned_data['birthday']
            adresse = etudiant_form.cleaned_data['adresse']

            phone = contact_form.cleaned_data['phone']
            email = contact_form.cleaned_data['email']

            pere = parent_form.cleaned_data['pere']
            mere = parent_form.cleaned_data['mere']
            phone_pere = parent_form.cleaned_data['phone_pere']
            phone_mere = parent_form.cleaned_data['phone_mere']
            adresse_parent = parent_form.cleaned_data['adresse_parent']

            with transaction.atomic():
                student = Etudiant.objects.filter(identifiant=identifiant)
                if not student.exists():
                    etudiant = Etudiant.objects.create(
                        identifiant=identifiant,
                        fname=fname,
                        lname=lname,
                        birthday=birthday,
                        adresse=adresse
                    )

                    id_etudiant = Etudiant.objects.get(identifiant=identifiant)

                    contact = Contact.objects.create(
                        etudiant_id=id_etudiant.id,
                        phone=phone,
                        email=email
                    )

                    parent = Parent.objects.create(
                        etudiant_id=id_etudiant.id,
                        pere=pere,
                        mere=mere,
                        phone_pere=phone_pere,
                        phone_mere=phone_mere,
                        adresse_parent=adresse_parent
                    )
                else:
                    identifiant = identifiant.first()

            text = "<div class='w-full bg-green-200' role='alert'><span class='p-3 text-red-800'>Enregistrement effectué avec success.</span></div>"
            messages.success(request, text)
            return redirect('etudiant:etudiant')
        else:
            text = etudiant_form.errors or contact_form.errors or parent_form.errors
            messages.success(request, text)
            return redirect('etudiant:etudiant')


def update_etudiant(request, id, num):
    if request.method == 'POST':
        #etudiant_form = EtudiantForm(request.POST)
        contact_form = ContactForm(request.POST)
        parent_form = ParentForm(request.POST)

        #if etudiant_form.is_valid() & contact_form.is_valid() & parent_form.is_valid():
        if contact_form.is_valid() & parent_form.is_valid():
            # identifiant = etudiant_form.cleaned_data['identifiant']
            # fname = etudiant_form.cleaned_data['fname']
            # lname = etudiant_form.cleaned_data['lname']
            # birthday = etudiant_form.cleaned_data['birthday']
            # adresse = etudiant_form.cleaned_data['adresse']

            phone = contact_form.cleaned_data['phone']
            email = contact_form.cleaned_data['email']

            pere = parent_form.cleaned_data['pere']
            mere = parent_form.cleaned_data['mere']
            phone_pere = parent_form.cleaned_data['phone_pere']
            phone_mere = parent_form.cleaned_data['phone_mere']
            adresse_parent = parent_form.cleaned_data['adresse_parent']

            with transaction.atomic():
                etudiant = Etudiant.objects.get(id=id)
                #etudiant.identifiant=request.POST.get('identifiant'),
                etudiant.fname=request.POST.get('fname'),
                etudiant.lname=request.POST.get('lname'),
                #etudiant.birthday=request.POST.get('birthday'),
                etudiant.adresse=request.POST.get('adresse')
                etudiant.save()

                #id_etudiant = Etudiant.objects.get(identifiant=identifiant)

                contact = Contact.objects.filter(etudiant_id=num).update(
                    phone=phone,
                    email=email
                )

                parent = Parent.objects.filter(etudiant_id=num).update(
                    pere=pere,
                    mere=mere,
                    phone_pere=phone_pere,
                    phone_mere=phone_mere,
                    adresse_parent=adresse_parent
                )

            text = "<div class='w-full bg-green-200' role='alert'><span class='p-3 text-red-800'>Modification effectué avec success.</span></div>"
            messages.success(request, text)
            return redirect('etudiant:etudiant')
        else:
            text = contact_form.errors or parent_form.errors
            messages.success(request, text)
            return redirect('etudiant:etudiant')


def etudiant(request):
    etudiant_info = v_etudiant_info.objects.all()

    etudiant_form = EtudiantForm()
    contact_form = ContactForm()
    parent_form = ParentForm()

    context = {
        'etudiant_info': etudiant_info,
        'eform': etudiant_form,
        'cform': contact_form,
        'pform': parent_form
    }

    id = request.POST.get('id')
    num = request.POST.get('num')
    if not id and not num:
        add_etudiant(request)
    else:
        update_etudiant(request, id, num)

    return render(request, 'etudiant/home.html', context)
