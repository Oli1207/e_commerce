# Generated by Django 4.2.3 on 2023-07-21 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_user_produit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produit',
            old_name='createdAt',
            new_name='creeA',
        ),
        migrations.RenameField(
            model_name='produit',
            old_name='countInStock',
            new_name='enStock',
        ),
        migrations.RenameField(
            model_name='produit',
            old_name='price',
            new_name='evaluation',
        ),
        migrations.RenameField(
            model_name='produit',
            old_name='brand',
            new_name='nom',
        ),
        migrations.RenameField(
            model_name='produit',
            old_name='numReviews',
            new_name='numEvaluations',
        ),
        migrations.RenameField(
            model_name='produit',
            old_name='rating',
            new_name='prix',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='category',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='name',
        ),
        migrations.AddField(
            model_name='produit',
            name='matiere',
            field=models.CharField(default='coton', max_length=100),
        ),
        migrations.AddField(
            model_name='produit',
            name='motif',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='produit',
            name='taille',
            field=models.IntegerField(default=1),
        ),
    ]