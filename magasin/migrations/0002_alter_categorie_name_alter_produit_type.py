# Generated by Django 4.2 on 2023-05-23 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='name',
            field=models.CharField(choices=[('Ap', 'Apprentissage'), ('Av', 'Aventures'), ('Bg', 'Biographie'), ('Cm', 'Commerce'), ('Fn', 'Finance'), ('Ph', 'Philosophique'), ('Pc', 'Policier'), ('Sf', 'Science-fiction')], default='Al', max_length=50),
        ),
        migrations.AlterField(
            model_name='produit',
            name='type',
            field=models.CharField(choices=[('Ap', 'Apprentissage'), ('Av', 'Aventures'), ('Bg', 'Biographie'), ('Cm', 'Commerce'), ('Fn', 'Finance'), ('Ph', 'Philosophique'), ('Pc', 'Policier'), ('Sf', 'Science-fiction')], default='em', max_length=2),
        ),
    ]
