# Generated by Django 2.0.6 on 2018-09-03 12:24

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20180827_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=product.models.get_section_upload_path, verbose_name='зображення секції'),
        ),
    ]