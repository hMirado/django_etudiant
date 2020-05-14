from django.db import models

# Create your models here.


class Etudiant(models.Model):
    identifiant = models.CharField(max_length = 10, unique = True)
    fname = models.CharField(max_length = 250)
    lname = models.CharField(max_length = 250)
    birthday = models.DateField()
    adresse = models.CharField(max_length = 500)

    def __str__(self):
        return self.identifiant


class Parent(models.Model):
    pere = models.CharField(max_length = 250)
    mere = models.CharField(max_length = 250)
    phone_pere = models.CharField(max_length = 50)
    phone_mere = models.CharField(max_length = 50)
    adresse_parent = models.CharField(max_length = 500)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.pere, self.mere)


class Contact(models.Model):
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length = 50)
    etudiant = models.OneToOneField(Etudiant, on_delete=models.CASCADE)

    def __str__(self):
        return self.email

class v_etudiant_info(models.Model):
    id = models.AutoField(primary_key = "true")
    identifiant = models.CharField(max_length = 500)
    fname = models.CharField(max_length = 500)
    lname = models.CharField(max_length = 500)
    birthday = models.DateField(max_length = 500)
    adresse = models.CharField(max_length = 500)
    pere = models.CharField(max_length = 500)
    mere = models.CharField(max_length = 500)
    phone_pere = models.IntegerField()
    phone_mere = models.IntegerField()
    adresse_parent = models.CharField(max_length = 500)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    etudiant_id = models.CharField(max_length = 500)

    class Meta:
        managed = False
        db_table = 'v_etudiant_info'
