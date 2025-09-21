from django.urls import path
from .views import BajajAPIView

urlpatterns = [
    path('bajaj/', BajajAPIView.as_view(), name='bajaj-api'),
]

