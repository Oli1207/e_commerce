# Generated by Django 4.2.3 on 2023-09-04 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_order_orderitem_product_review_shippingaddress_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='prix',
            new_name='price',
        ),
    ]
