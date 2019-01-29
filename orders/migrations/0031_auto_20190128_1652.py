# Generated by Django 2.0.6 on 2019-01-28 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0030_auto_20190125_0430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_method',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.DeliveryMethod', verbose_name='Спосіб доставки'),
        ),
        migrations.AlterField(
            model_name='productinbasket',
            name='size',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='properties.Size', verbose_name='Розмір'),
        ),
    ]