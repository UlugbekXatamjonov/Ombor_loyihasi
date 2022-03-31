from django.urls import path
from .views import ListProduct, DetailProduct, ListReport, DetailReport

app_name = "products"

urlpatterns = [
    path('products/<int:year>/<int:month>/<int:day>/<int:pk>',DetailProduct.as_view(), name='detail'),
    path('products/',ListProduct.as_view(), name='list'),

    path('reports/<int:year>/<int:month>/<int:day>/<int:pk>', DetailReport.as_view(), name='repo_detail'),
    path('reports/',ListReport.as_view(), name='repo_list'),
]
