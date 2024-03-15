from rest_framework import serializers
from .models import Product, Material, ProductMaterial, Warehouses


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'name', ]


class ProductMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMaterial
        fields = ['product', 'material', 'quantity', ]


class WarehousesSerializer(serializers.ModelSerializer):
    material_name = serializers.SerializerMethodField()
    qty = serializers.SerializerMethodField()
    warehouse_id = serializers.SerializerMethodField()

    class Meta:
        model = Warehouses
        fields = ['warehouse_id', 'material_name', 'qty', 'price', ]

    def get_warehouse_id(self, obj):
        return obj.id

    def get_material_name(self, obj):
        return obj.material.name if obj.material else None

    def get_qty(self, obj):
        material = obj.material
        if material:
            product_materials = ProductMaterial.objects.filter(material=material)
            if product_materials.exists():
                product = product_materials.first()
                return product.quantity  # quantity maydoni uchun "product" obyektini olib qo'yamiz
        return None


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'code', ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        product_materials = ProductMaterial.objects.filter(product=instance)
        material_names = [pm.material.name for pm in product_materials]
        warehouses = Warehouses.objects.filter(material__name__in=material_names)
        data['product_materials'] = WarehousesSerializer(warehouses, many=True).data
        return data

