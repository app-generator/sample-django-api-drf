from django.db import models


class Transaction(models.Model):
    product = models.CharField(max_length=50)
    price = models.IntegerField()
    qty = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    info = models.CharField(max_length=250, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product}"
