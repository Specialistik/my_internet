from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=30)


class Person(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    token = models.CharField(max_length=32)
    sim = models.CharField(max_length=11)
    fio = models.CharField(max_length=80)
    passport = models.CharField(max_length=10)
    role = models.ForeignKey(Role, default=3, on_delete=models.RESTRICT)
