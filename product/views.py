from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .models import Product, Report
from .serializers import ProductSerializer, ReportSerializer

# ---------------------- Product -----------------------
class ListProduct(ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    template_name = 'list.html'

class DetailProduct(RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    template_name = 'list.html'



# ---------------------- Report -----------------------
class ListReport(ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    template_name = 'list.html'

class DetailReport(RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    template_name = 'list.html'

