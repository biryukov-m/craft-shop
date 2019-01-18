# Generated by Django 2.0.6 on 2019-01-18 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0023_auto_20190118_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinbasket',
            name='order',
        ),
        migrations.AddField(
            model_name='productinbasket',
            name='basket',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Order', verbose_name='Корзина'),
        ),
    ]
