# Generated by Django 2.0.5 on 2019-09-12 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_item_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='code',
            field=models.IntegerField(blank=True, editable=False, null=True, unique=True, verbose_name='код'),
        ),
    ]
