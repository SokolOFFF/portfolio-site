from django.db import models


class Project(models.Model):
    name = models.TextField()
    description = models.TextField()
    link = models.TextField(default='https://github.com/SokolOFFF')


class Contact(models.Model):
    name = models.CharField(max_length=10)
    link = models.TextField(default='https://vk.com/yeawou')
