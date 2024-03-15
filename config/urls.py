from django.contrib import admin
from django.urls import path

from page.views import ProductAPIList, MaterialList, ProductMaterialList, WarehousesList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/product/', ProductAPIList.as_view()),
    path('api/v1/material/', MaterialList.as_view()),
    path('api/v1/product_material/', ProductMaterialList.as_view()),
    path('api/v1/warehouses/', WarehousesList.as_view()),
]
