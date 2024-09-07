from django.db import models


# About Model
class About(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='about/')

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        return self.name


# Service Model
class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name


#Recent Work Model
class RecentWork(models.Model):
    title = models.CharField(max_length=255,verbose_name="Work title")
    image = models.ImageField(upload_to='works')

    def __str__(self):
        return self.title

# Client Model
class Client(models.Model):
    name = models.CharField(max_length=100,verbose_name="Client Name")
    description = models.TextField(verbose_name="Client say")
    image = models.ImageField(upload_to='clients', default='default.png')

    def __str__(self):
        return self.name