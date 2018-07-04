# Generated by Django 2.0.7 on 2018-07-03 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_remove_productinorder_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinorder',
            name='order',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='orders.Order'),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
