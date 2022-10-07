from django.urls import path
from .views import ProductsAPIView, ProductDetailAPIView, CategoriesAPIView, CategoryDetailAPIView

urlpatterns = [
    path('products/', ProductsAPIView.as_view(), name='products-list'),
    path('products/<int:id>/', ProductDetailAPIView.as_view(), name='products-detail'),
    path('categories/', CategoriesAPIView.as_view(), name='category-list'),
    path('categories/<int:id>/', CategoryDetailAPIView.as_view(), name='category-detail'),

]
