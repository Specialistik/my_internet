# Generated by Django 3.1.4 on 2020-12-24 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='core.company', verbose_name='Компания'),
            preserve_default=False,
        ),
    ]