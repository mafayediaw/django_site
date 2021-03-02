from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here


class Destination(models.Model):
    pays = models.CharField(max_length=20)

    def __str__(self):
        return '%s' % (self.pays)


class Excursion(models.Model):
    nom = models.CharField(max_length=100)
    optionnelle = models.BooleanField()
    
    class VoyageExcursions:
            ordering = ['nom']

    def __str__(self):
        return str(self.nom)


class Voyage(models.Model):
    nom = models.CharField(max_length=100)
    photo = models.ImageField(default='index.jpg', upload_to='photos/')
    duree = models.IntegerField()
    prix = models.FloatField()
    destinations = models.ForeignKey(Destination, on_delete=models.CASCADE)
    excursions = models.ManyToManyField(Excursion)
    class VoyageExcursions:
            ordering = ['nom']

    def __str__(self):
        return str(self.nom)
    
    
class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image= models.ImageField(default='index.jpeg', upload_to='photos/')

    def __str__(self):
        return f'{self.user.username} Profil'

    def save(self):
        super().save()

        img= Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
