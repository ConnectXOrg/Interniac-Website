# Generated by Django 3.1.6 on 2021-03-07 05:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('marketplace', '0008_auto_20210228_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='acceptances',
            field=models.ManyToManyField(blank=True, related_name='listing_acceptances', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listing',
            name='rejections',
            field=models.ManyToManyField(blank=True, related_name='listing_rejections', to=settings.AUTH_USER_MODEL),
        ),
    ]
