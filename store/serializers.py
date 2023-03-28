from rest_framework import serializers
from .models import Product, Collection, Review
from decimal import Decimal


# class CollectionSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "title", "featured_product"]


# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     price = serializers.DecimalField(
#         max_digits=6, decimal_places=2, source="unit_price"
#     )
#     price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")
#     # collection = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all())
#     # collection = serializers.StringRelatedField()

#     # collection = CollectionSerializer()
#     collection = serializers.HyperlinkedRelatedField(
#         queryset=Collection.objects.all(), view_name="collection_detail"
#     )

#     def calculate_tax(self, product: Product):
#         return product.unit_price * Decimal(1.1)


class ProductSerializer(serializers.ModelSerializer):
    # model serializer by default uses primarykeyrelatedfield to get the foreign key field
    # you can override as shown below
    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "slug",
            "inventory",
            "description",
            "unit_price",
            "price_with_tax",
            "collection",
        ]

    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")
    # collection = CollectionSerializer()

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)

    # pass the serializer's validated_data to the create function and use it to set other fields of product model
    # def create(self, validated_data):
    #     product = Product(**validated_data)
    #     product.other_field = 1
    #     product.save()
    #     return product

    # use this to validate specific fields
    # def validate(self, attrs):
    #     return super().validate(attrs)


{"title": "a", "unit_price": 1, "collection": 1, "inventory": 1, "slug": "aaa"}


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "name", "description", "date"]

    def create(self, validated_data):
        product_id = self.context["product_id"]
        return Review.objects.create(product_id=product_id, **validated_data)
