# Generated by Django 5.1.1 on 2024-10-03 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_product_created_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AvailableProduct',
        ),
    ]
