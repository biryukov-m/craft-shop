# Generated by Django 2.0.6 on 2018-08-27 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20180822_1506'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товари'},
        ),
    ]