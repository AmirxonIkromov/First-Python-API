from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from api.serializers import ProductSerializers, CategorySerializers
from .models import Product, Category


class ProductDetailAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, id):

        product = Product.objects.get(id=id)
        serializer = ProductSerializers(product)

        return Response(data=serializer.data)

    def delete(self, request, id):
        product = Product.objects.get(id=id)
        product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        product = Product.objects.get(id=id)
        serializer = ProductSerializers(instance=product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        product = Product.objects.get(id=id)
        serializer = ProductSerializers(instance=product, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductsAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializers(product, many=True)

        return Response(data=serializer.data)

    def post(self, request):
        serializer = ProductSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailAPIView(APIView):

    def get(self, request, id):

        products_by_category = Product.objects.filter(category_id=id)
        serializer = CategorySerializers(products_by_category, many=True)

        return Response(data=serializer.data)

    def delete(self, request, id):

        category = Category.objects.get(id=id)
        category.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        category = Category.objects.get(id=id)
        serializer = CategorySerializers(instance=category, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        category = Category.objects.get(id=id)
        serializer = CategorySerializers(instance=category, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriesAPIView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializers(category, many=True)

        return Response(data=serializer.data)

    def post(self, request):
        serializer = CategorySerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
# @api_view(['GET'])
# def get_products(request):
#     products = Product.objects.all()
#     serializer = ProductSerializers(products, many=True)
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def get_product(id):
#     product = Product.objects.get(id=id)
#     serializer = ProductSerializers(product, many=False)
#     return Response(serializer.data)
#
#
# @api_view(['POST'])
# def add_product(request):
#     serializer = ProductSerializers(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
#
# @api_view(['POST'])
# def update_product(request, id):
#     product = Product.objects.get(id=id)
#     serializer = ProductSerializers(instance=product, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
#
# @api_view(['DELETE'])
# def delete_product(request, id):
#     product = Product.objects.get(id=id)
#     product.delete()
#     return Response(status='Deleted')
