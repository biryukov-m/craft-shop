# Generated by Django 2.0.6 on 2019-01-02 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_auto_20181222_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinbasket',
            name='is_inactive',
        ),
    ]