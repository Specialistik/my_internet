# -*- coding: utf-8 -*-
from django.db import models

class Emails(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name=u"Почта")

    def __str__(self):
        return '%s' % self.name

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = u'Почта'
        verbose_name_plural = u'Почты'

class Company(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name=u"Компания")
    emails = models.ManyToManyField(Emails, verbose_name=u'e-mail')

    def __str__(self):
        return '%s' % self.name

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = u'Компания'
        verbose_name_plural = u'Компании'

class Operator(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name=u"Оператор мобильной связи")

    def __str__(self):
        return '%s' % self.name

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = u'Оператор связи'
        verbose_name_plural = u'Операторы связи'


class Region(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name=u"Регион")
    company = models.ForeignKey(Company, verbose_name=u"Компания", on_delete=models.RESTRICT)

    def __str__(self):
        return '%s' % self.name

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = u'Регион'
        verbose_name_plural = u'Регионы'

class Role(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name=u"Роль пользователя")

    def __str__(self):
        return '%s' % self.name

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = u'Роль'
        verbose_name_plural = u'Роли'


class Person(models.Model):
    login = models.CharField(max_length=30, verbose_name=u'Логин', unique=True)
    password = models.CharField(max_length=30, verbose_name=u'Пароль')
    token = models.CharField(max_length=255, unique=True, blank=True, verbose_name=u'Токен')
    sim = models.CharField(max_length=11, verbose_name=u"Номер телефона SIM-карты (10 знаков, без +7)", unique=True)
    fio = models.CharField(max_length=80, verbose_name=u"ФИО")
    passport = models.CharField(max_length=10, verbose_name=u"Серия, номер паспорта (без пробелов)")
    role = models.ForeignKey(Role, default=3, on_delete=models.RESTRICT, verbose_name=u'Роль')
    address = models.CharField(max_length=80, verbose_name=u"Адрес")
    operator_type = models.ForeignKey(Operator, verbose_name=u"Оператор связи", on_delete=models.RESTRICT)
    passport_pic = models.ImageField(upload_to='passport1', verbose_name=u'Первая страница паспорта')
    passport_pic2 = models.ImageField(upload_to='passport2', verbose_name=u'Вторая страница паспорта')
    company = models.ForeignKey(Company, verbose_name=u"Компания", on_delete=models.RESTRICT)

    def __str__(self):
        return '%s' % self.fio

    def __unicode__(self):
        return '%s' % self.fio

    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'
