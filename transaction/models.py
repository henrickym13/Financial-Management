from django.db import models
from django.contrib.auth.models import User
from category.models import Category


# Create your models here.
class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('income', 'Receita'),
        ('expense', 'Despesa')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    type_choice = models.CharField(max_length=7, choices=TRANSACTION_TYPES)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.description} - {self.amount} - ({self.type_choice})'