# Generated by Django 2.0.6 on 2019-02-12 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0036_order_hash_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='number',
            field=models.PositiveSmallIntegerField(blank=True, default=True, null=True, verbose_name='Порядковий номер'),
        ),
    ]
