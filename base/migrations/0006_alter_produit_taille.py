# Generated by Django 4.2.3 on 2023-07-21 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_produit_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='taille',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
