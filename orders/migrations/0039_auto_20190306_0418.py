# Generated by Django 2.0.6 on 2019-03-06 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0038_auto_20190212_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='hash_code',
            field=models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='хеш-код'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ManyToManyField(blank=True, default=None, to='orders.Status', verbose_name='Статус замовлення'),
        ),
    ]
