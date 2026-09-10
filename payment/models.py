from django.db import models

# Create your models here.


class Payment (models.Model):
    upi_id = models.CharField(max_length=100)
    receiver_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.CharField(max_length =200)


    def ___str__(self):
        return self.upi_id
