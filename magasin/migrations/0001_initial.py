# Generated by Django 4.2 on 2023-05-23 19:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Al', 'Alimentaire'), ('Mb', 'Meuble'), ('Sn', 'Sanitaire'), ('Vs', 'Vaisselle'), ('Vt', 'Vêtement'), ('Jx', 'Jouets'), ('Lg', 'Linge de Maison'), ('Bj', 'Bijoux'), ('Dc', 'Décor')], default='Al', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, null=True)),
                ('adresse', models.TextField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('telephone', models.CharField(max_length=8, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
                ('transaction_id', models.CharField(max_length=100, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='magasin.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('digital', models.BooleanField(blank=True, default=False, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libellé', models.CharField(max_length=100)),
                ('description', models.TextField(default='non définie')),
                ('prix', models.DecimalField(decimal_places=3, default=0, max_digits=10)),
                ('type', models.CharField(choices=[('em', 'emballé'), ('fr', 'Frais'), ('cs', 'Conserve')], default='em', max_length=2)),
                ('img', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('catégorie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='magasin.categorie')),
                ('fournisseur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='magasin.fournisseur')),
            ],
        ),
        migrations.CreateModel(
            name='ProduitNC',
            fields=[
                ('produit_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='magasin.produit')),
                ('Duree_garantie', models.CharField(max_length=100)),
            ],
            bases=('magasin.produit',),
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='magasin.customer')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='magasin.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='magasin.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='magasin.product')),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCde', models.DateField(default=datetime.date.today, null=True)),
                ('nom_client', models.CharField(default='', max_length=100)),
                ('adresse_livraison', models.CharField(default='', max_length=200)),
                ('totalCde', models.DecimalField(decimal_places=3, max_digits=10)),
                ('produits', models.ManyToManyField(related_name='produits', to='magasin.produit')),
            ],
        ),
    ]
