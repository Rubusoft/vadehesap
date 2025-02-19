from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InstallmentRateViewSet, CalculatorViewSet, CalculatorTemplateView

router = DefaultRouter()
router.register(r'rates', InstallmentRateViewSet)
router.register(r'calculator', CalculatorViewSet, basename='calculator')

urlpatterns = [
    path('', CalculatorTemplateView.as_view(), name='calculator'),
    path('api/', include(router.urls)),
] 