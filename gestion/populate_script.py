########################
#      DATA FAKER      #
########################

import os, django, random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gestion.settings")
django.setup()

from faker import Faker
from etudiant.models import Niveau, Etudiant, Contact, Parent
from django.utils import timezone
from random import randint

# def create_niveau():
#     faker = Faker()
#     Niveau.objects.create(
#         niveau="L1 - IRD"
#     )
#     Niveau.objects.create(
#         niveau="L1 - TC"
#     )
#     Niveau.objects.create(
#         niveau="L2 - BANCASS"
#     )
#     Niveau.objects.create(
#         niveau="L2 - IRD"
#     )
#     Niveau.objects.create(
#         niveau="L2 - MEGP"
#     )
#     Niveau.objects.create(
#         niveau="L3 - BANCASS"
#     )
#     Niveau.objects.create(
#         niveau="L3 - IRD"
#     )
#     Niveau.objects.create(
#         niveau="L3 - MEGP"
#     )
#
# create_niveau()
# print("OK OK")

def create_etudiant(N):
    faker = Faker()
    for _ in range(N):

        id_niveau = random.randint(1,8)
        id = random.randint(1,20)
        identifiant = "SE"+str(random.randint(2017, 2020))+str(random.randint(100, 500))
        Etudiant.objects.create(
            identifiant=identifiant,
            lname=faker.last_name(),
            fname=faker.first_name(),
            birthday="2000-01-01",
            adresse=faker.address(),
            niveau_id=id_niveau
        )

        id_etudiant = Etudiant.objects.get(identifiant=identifiant)

        Contact.objects.create(
            email=faker.email(),
            phone=faker.phone_number(),
            etudiant_id=id_etudiant.id
        )

        Parent.objects.create(
            pere=faker.name(),
            mere=faker.name(),
            phone_mere=faker.phone_number(),
            phone_pere=faker.phone_number(),
            adresse_parent=faker.address(),
            etudiant_id=id_etudiant.id
        )

create_etudiant(50)
print("OK OK")

# def create_contact(N):
#     faker = Faker()
#     for _ in range(N):
#         id = random.randint(1,19)
#         id_etudiant = Etudiant.objects.get(identifiant=identifiant)
#         Contact.objects.create(
#             email=faker.email(),
#             phone=faker.phone_number(),
#             etudiant_id=id_etudiant.id
#         )
# create_contact(10)
# print("OK OK")
