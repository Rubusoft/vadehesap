from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class InstallmentRate(models.Model):
    number_of_installments = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(36)],
        verbose_name="Taksit Sayısı"
    )
    interest_rate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Faiz Oranı (%)"
    )
    is_active = models.BooleanField(default=True, verbose_name="Aktif mi?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncellenme Tarihi")

    class Meta:
        verbose_name = "Taksit Oranı"
        verbose_name_plural = "Taksit Oranları"
        ordering = ['number_of_installments']
        unique_together = ['number_of_installments', 'is_active']

    def __str__(self):
        return f"{self.number_of_installments} Taksit - %{self.interest_rate}"
