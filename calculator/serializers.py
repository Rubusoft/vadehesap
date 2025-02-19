from rest_framework import serializers
from .models import InstallmentRate

class InstallmentRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstallmentRate
        fields = ['id', 'number_of_installments', 'interest_rate', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class CalculationRequestSerializer(serializers.Serializer):
    amount = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=0.01,
        help_text="Toplam tutar"
    )
    number_of_installments = serializers.IntegerField(
        min_value=1,
        max_value=36,
        help_text="Taksit sayısı"
    )

class CalculationResponseSerializer(serializers.Serializer):
    original_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    monthly_installment = serializers.DecimalField(max_digits=10, decimal_places=2)
    number_of_installments = serializers.IntegerField()
    interest_rate = serializers.DecimalField(max_digits=5, decimal_places=2)
    total_interest = serializers.DecimalField(max_digits=10, decimal_places=2) 