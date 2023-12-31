from audioop import reverse
from datetime import timezone
from django.db import models
from django.contrib.auth.models import User  

# Create your models here.
class VoitureImage(models.Model):
 image=models.ImageField()
 voiture=models.ForeignKey('Voiture',on_delete=models.CASCADE)

class Voiture(models.Model):
    class Status(models.TextChoices):
      Disponible = 'Dis', 'Disponible'
      InDisponible = 'InDis', 'IndDisponible'

    immatriculation = models.SlugField(max_length=250)
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    annee_fabrication = models.DateField()
    couleur = models.CharField(max_length=50)
    status = models.CharField(max_length=5,
                              choices=Status.choices,
                              default=Status.Disponible)
    


    def __str__(self):
        return f"{self.marque} {self.modele} ({self.annee_fabrication.year})" 
 # Meta pour spécifier l'ordre par defaut de recuperation 
    class Meta: 
        ordering = ['annee_fabrication', 'marque', 'modele']
        
    def get_absolute_url(self):
        return reverse('voiture_detail', args=[str(self.id)])
    


# ****** Class Client ********** #
class Client(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    numero_telephone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.email})"    
    
# ****** Class Location ********** #
class Location(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    voiture = models.ForeignKey('Voiture', on_delete=models.CASCADE)
    date_debut = models.DateTimeField(auto_now_add=True)
    mise_ajour_date = models.DateTimeField(auto_now=True)
    date_fin = models.DateField()
    prix_jour = models.DecimalField(max_digits=10, decimal_places=2)
    nombres_jours = models.DecimalField(max_digits=10, decimal_places=2)
    total= models.DecimalField(max_digits=10, decimal_places=2 ,editable=False)

    def save(self, *args, **kwargs):
        # Calculer le total avant de sauvegarder l'objet
        self.total = self.prix_jour * self.nombres_jours
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Location de {self.voiture} à {self.client} du {self.date_debut} au {self.date_fin}"
    