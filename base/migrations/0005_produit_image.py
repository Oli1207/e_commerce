# Generated by Django 4.2.3 on 2023-07-21 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_commande_commandearticle_avis_adresselivraison'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]