# Generated by Django 2.0.6 on 2018-07-16 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_productinorder_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinorder',
            old_name='is_active',
            new_name='is_inactive',
        ),
    ]
