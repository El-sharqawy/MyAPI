from django.db import models
from users.models import CustomUser
from django.core.validators import MinValueValidator

class IncomeSource(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="income_sources")
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"

class Expanses(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="expanses")
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.category} - {self.user.username}"

class Transaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="transactions")
    income_source = models.ForeignKey(IncomeSource, on_delete=SET_NULL, null=True, blank=True)
    expanses = models.ForeignKey(Expanses, on_delete=SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators = [MinValueValidator(0.01)])
    transaction_date = models.DateField()
    description = models.TextField(blank=True)