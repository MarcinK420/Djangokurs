from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)  # nazwa usługi
    description = models.TextField(default="")         # opis
    price = models.DecimalField(max_digits=6, decimal_places=2)  # cena

    def __str__(self):
        return self.name
