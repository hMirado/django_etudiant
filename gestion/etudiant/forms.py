from django.forms import ModelForm, TextInput, EmailInput, DateInput, NumberInput
from django.forms.utils import ErrorList
from .models import Etudiant, Parent, Contact

class EtudiantForm(ModelForm):
    class Meta:
        model = Etudiant
        fields = ["identifiant", "fname", "lname", "birthday", "adresse"]
        widgets = {
            'identifiant': TextInput(attrs={'class': 'w-full border border-gray-800 rounded-lg', 'id': 'edutiant-identifiant'}),
            'fname': TextInput(attrs={'class': 'w-full border border-gray-800 rounded-lg', 'id': 'edutiant-fname'}),
            'lname': TextInput(attrs={'class': 'w-full border border-gray-800 rounded-lg', 'id': 'edutiant-lname'}),
            'birthday': DateInput(attrs={'class': 'w-full border border-gray-800 rounded-lg', 'placeholder': 'AAAA/MM/JJ', 'id': 'edutiant-birthday'}),
            'adresse': TextInput(attrs={'class': 'w-full border border-gray-800 rounded-lg', 'id': 'edutiant-adresse'})
        }

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["email", "phone"]
        widgets = {
            'phone': TextInput(attrs={'class': 'w-full border border-gray-800 rounded-lg', 'id': 'contact-phone'}),
            'email': EmailInput(attrs={'class': 'w-full border border-gray-800 rounded-lg', 'id': 'contact-email'})
        }

class ParentForm(ModelForm):
    class Meta:
        model = Parent
        fields = ["pere", "mere", "phone_pere", "phone_mere", "adresse_parent"]
        widgets = {
            'pere': TextInput(attrs={'class': 'w-full border border-gray-800 rounded-lg', 'id': 'parent-pere'}),
            'mere': TextInput(attrs={'class': 'w-full border border-gray-800 rounded-lg', 'id': 'parent-mere'}),
            'phone_pere': TextInput(attrs={'class': 'w-full border border-gray-800 rounded-lg', 'id': 'parent-phone_pere'}),
            'phone_mere': TextInput(attrs={'class': 'w-full border border-gray-800 rounded-lg', 'id': 'parent-phone_mere'}),
            'adresse_parent': TextInput(attrs={'class': 'w-full border border-gray-800 rounded-lg', 'id': 'parent-adresse_parent'})
        }
