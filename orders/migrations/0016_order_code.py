# Generated by Django 2.0.6 on 2018-08-03 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_auto_20180803_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='code',
            field=models.PositiveSmallIntegerField(default=None, editable=False, verbose_name='Код'),
        ),
    ]