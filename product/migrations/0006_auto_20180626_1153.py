# Generated by Django 2.0.6 on 2018-06-26 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20180625_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='bag',
            name='item_code',
            field=models.CharField(blank=True, default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='cosmeticbag',
            name='item_code',
            field=models.CharField(blank=True, default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='dress',
            name='item_code',
            field=models.CharField(blank=True, default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='dresspattern',
            name='item_code',
            field=models.CharField(blank=True, default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='mobilecase',
            name='item_code',
            field=models.CharField(blank=True, default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='shirt',
            name='item_code',
            field=models.CharField(blank=True, default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='shirtpattern',
            name='item_code',
            field=models.CharField(blank=True, default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='skirt',
            name='item_code',
            field=models.CharField(blank=True, default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='skirtpattern',
            name='item_code',
            field=models.CharField(blank=True, default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='tablecloth',
            name='item_code',
            field=models.CharField(blank=True, default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='tshirt',
            name='item_code',
            field=models.CharField(blank=True, default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='tshirtpattern',
            name='item_code',
            field=models.CharField(blank=True, default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='tunic',
            name='item_code',
            field=models.CharField(blank=True, default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='tunicpattern',
            name='item_code',
            field=models.CharField(blank=True, default=None, max_length=20),
        ),
    ]
