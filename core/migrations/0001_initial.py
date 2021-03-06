# Generated by Django 3.1.4 on 2020-12-19 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Оператор мобильной связи')),
            ],
            options={
                'verbose_name': 'Оператор',
                'verbose_name_plural': 'Операторы',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Роль пользователя')),
            ],
            options={
                'verbose_name': 'Роль',
                'verbose_name_plural': 'Роли',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=30, unique=True, verbose_name='Логин')),
                ('password', models.CharField(max_length=30, verbose_name='Пароль')),
                ('token', models.CharField(blank=True, max_length=32, unique=True)),
                ('sim', models.CharField(max_length=11, unique=True, verbose_name='Номер телефона SIM-карты')),
                ('fio', models.CharField(max_length=80, verbose_name='ФИО')),
                ('passport', models.CharField(max_length=10, verbose_name='Серия, номер паспорта (без пробелов)')),
                ('address', models.CharField(max_length=80, verbose_name='Адрес')),
                ('passport_pic', models.ImageField(upload_to='passport1', verbose_name='Первая страница паспорта')),
                ('passport_pic2', models.ImageField(upload_to='passport2', verbose_name='Вторая страница паспорта')),
                ('operator_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='core.operator', verbose_name='Оператор связи')),
                ('role', models.ForeignKey(default=3, on_delete=django.db.models.deletion.RESTRICT, to='core.role')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
