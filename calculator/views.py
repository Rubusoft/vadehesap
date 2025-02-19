from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from decimal import Decimal, ROUND_HALF_UP
from .models import InstallmentRate
from .serializers import (
    InstallmentRateSerializer,
    CalculationRequestSerializer,
    CalculationResponseSerializer
)
from django.views.generic import TemplateView

# Create your views here.

class InstallmentRateViewSet(viewsets.ModelViewSet):
    queryset = InstallmentRate.objects.all()
    serializer_class = InstallmentRateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Deactivate other rates with same number of installments
        InstallmentRate.objects.filter(
            number_of_installments=serializer.validated_data['number_of_installments'],
            is_active=True
        ).update(is_active=False)
        serializer.save()

class CalculatorViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def calculate(self, request):
        request_serializer = CalculationRequestSerializer(data=request.data)
        if not request_serializer.is_valid():
            return Response(
                {"error": "Geçersiz veri formatı. Lütfen sayısal değerleri kontrol edin."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            amount = Decimal(str(request_serializer.validated_data['amount'])).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            number_of_installments = request_serializer.validated_data['number_of_installments']

            rate = get_object_or_404(
                InstallmentRate,
                number_of_installments=number_of_installments,
                is_active=True
            )

            # Vade farkı hesaplama formülü: Tutar / (1 - Vade Farkı Oranı)
            total_rate = rate.interest_rate / Decimal('100')
            total_amount = (amount / (Decimal('1') - total_rate)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            total_interest = (total_amount - amount).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            monthly_installment = (total_amount / Decimal(str(number_of_installments))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

            response_data = {
                'original_amount': amount,
                'total_amount': total_amount,
                'monthly_installment': monthly_installment,
                'number_of_installments': number_of_installments,
                'interest_rate': rate.interest_rate,
                'total_interest': total_interest
            }

            response_serializer = CalculationResponseSerializer(data=response_data)
            response_serializer.is_valid(raise_exception=True)
            
            return Response(response_serializer.data)
            
        except (ValueError, TypeError) as e:
            return Response(
                {"error": "Hesaplama sırasında bir hata oluştu. Lütfen girilen değerleri kontrol edin."},
                status=status.HTTP_400_BAD_REQUEST
            )
        except InstallmentRate.DoesNotExist:
            return Response(
                {"error": "Bu taksit sayısı için aktif bir oran bulunmamaktadır."},
                status=status.HTTP_404_NOT_FOUND
            )

class CalculatorTemplateView(TemplateView):
    template_name = "calculator/index.html"
