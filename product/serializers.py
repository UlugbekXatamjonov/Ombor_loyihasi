from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Product, Report

# ---------------------- Product Serializer -----------------------
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','tur','nom','rang','rasm','narx','son','kompania','mudat','kg','qr_code','barcode','izoh','sana')
    


# ---------------------- Report Serializer -----------------------
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('id','tur','nom','rang','rasm','son','kompania','mudat','kg','izoh','sana','tekshir')