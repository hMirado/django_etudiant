# Generated by Django 3.0.4 on 2020-03-28 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etudiant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etudiant',
            name='niveau',
        ),
        migrations.DeleteModel(
            name='Niveau',
        ),
    ]
