from django.db import models


class CreditCard(models.Model):
    owner_id = models.IntegerField()
    card_name = models.CharField(max_length=128)
    name_on_card = models.CharField(max_length=32)
    expiry_date = models.CharField(max_length=5)
    card_type = models.CharField(max_length=128)
    cvv = models.IntegerField()
    card_number = models.CharField(max_length=16)

    def __str__(self):
        return self.card_name
