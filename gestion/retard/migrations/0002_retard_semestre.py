# Generated by Django 3.0.4 on 2020-03-28 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='retard',
            name='semestre',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
