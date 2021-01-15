# Generated by Django 3.1.4 on 2021-01-04 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210104_0417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='login',
            field=models.CharField(blank=True, editable=False, max_length=30, unique=True, verbose_name='Логин'),
        ),
        migrations.AlterField(
            model_name='person',
            name='password',
            field=models.CharField(blank=True, editable=False, max_length=30, verbose_name='Пароль'),
        ),
    ]
