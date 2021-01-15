# -*- coding: utf-8 -*-
import datetime
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


class Person(models.Model):
    # Прикрутить автоматическую генерацию логина и пароля
    login = models.CharField(max_length=30, verbose_name=u'Логин', unique=True, editable=False, blank=True)
    password = models.CharField(max_length=30, verbose_name=u'Пароль', editable=False, blank=True)
    token = models.CharField(max_length=255, unique=True, blank=True, verbose_name=u'Токен')
    sim = models.CharField(max_length=11, verbose_name=u"Номер телефона SIM-карты (10 знаков, без +7)", unique=True)
    fio = models.CharField(max_length=80, verbose_name=u"ФИО")
    passport = models.CharField(max_length=10, verbose_name=u"Серия, номер паспорта (без пробелов)")
    address = models.CharField(max_length=80, verbose_name=u"Адрес")
    operator_type = models.ForeignKey(Operator, verbose_name=u"Оператор связи", on_delete=models.RESTRICT)
    passport_pic = models.ImageField(upload_to='passport1', verbose_name=u'Первая страница паспорта')
    passport_pic2 = models.ImageField(upload_to='passport2', verbose_name=u'Вторая страница паспорта')
    company = models.ForeignKey(Company, verbose_name=u"Компания", on_delete=models.RESTRICT)
    balance = models.IntegerField(default=0, verbose_name=u"Баланс")
    monthly_payment = models.IntegerField(default=500, verbose_name=u"Платёж в месяц")
    payment_date = models.DateField(defult=datetime.datetime.now(), verbose_name=u"Дата следующего платежа")

    def __str__(self):
        return '%s' % self.fio

    def __unicode__(self):
        return '%s' % self.fio

    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'


class Payment(models.Model):
    user = models.ForeignKey(Person, verbose_name=u"Пользователь", on_delete=models.RESTRICT)
    sum = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u"Сумма платежа")
    datetime = models.DateTimeField(default=datetime.datetime.now(), verbose_name=u"Дата платежа")
    status = models.CharField(max_length=20, default="in_progress", verbose_name=u"Статус")

    def __str__(self):
        return '%s - %s' % (self.user, self.sum)

    def __unicode__(self):
        return '%s - %s' % (self.user, self.sum)

    class Meta:
        verbose_name = u'Оплата'
        verbose_name_plural = u'Оплаты'
