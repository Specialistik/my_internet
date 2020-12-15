# -*- coding: utf-8 -*-
from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = u'Роль'
        verbose_name_plural = u'Роли'


class Person(models.Model):
    login = models.CharField(max_length=30, verbose_name=u'Логин')
    password = models.CharField(max_length=30, verbose_name=u'Пароль')
    token = models.CharField(max_length=32)
    sim = models.CharField(max_length=11, verbose_name=u"Номер телефона SIM-карты")
    fio = models.CharField(max_length=80, verbose_name=u"ФИО")
    passport = models.CharField(max_length=10, verbose_name=u"Серия, номер паспорта (без пробелов)")
    role = models.ForeignKey(Role, default=3, on_delete=models.RESTRICT)

    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'
