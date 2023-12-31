# Generated by Django 4.2.3 on 2023-07-21 06:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0003_rename_createdat_produit_creea_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('methodePaiement', models.CharField(blank=True, max_length=200, null=True)),
                ('prixTaxe', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('prixLivraison', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('prixTotal', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('estPaye', models.BooleanField(default=False)),
                ('payeLe', models.DateTimeField(blank=True, null=True)),
                ('estLivre', models.BooleanField(default=False)),
                ('livreLe', models.DateTimeField(blank=True, null=True)),
                ('creeLe', models.DateTimeField(auto_now_add=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommandeArticle',
            fields=[
                ('nom', models.CharField(blank=True, max_length=200, null=True)),
                ('quantite', models.IntegerField(blank=True, default=0, null=True)),
                ('prix', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('image', models.CharField(blank=True, max_length=200, null=True)),
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('commande', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.commande')),
                ('produit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.produit')),
            ],
        ),
        migrations.CreateModel(
            name='Avis',
            fields=[
                ('nom', models.CharField(blank=True, max_length=200, null=True)),
                ('evaluation', models.IntegerField(blank=True, default=0, null=True)),
                ('commentaire', models.TextField(blank=True, null=True)),
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('produit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.produit')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AdresseLivraison',
            fields=[
                ('adresse', models.CharField(blank=True, max_length=200, null=True)),
                ('ville', models.CharField(blank=True, max_length=200, null=True)),
                ('codePostal', models.CharField(blank=True, max_length=200, null=True)),
                ('pays', models.CharField(blank=True, max_length=200, null=True)),
                ('prixLivraison', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('commande', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.commande')),
            ],
        ),
    ]
