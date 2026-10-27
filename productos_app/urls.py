from django.urls import path
from .views import (
    CategoriaListCreate, CategoriaDetail,
    ProductoListCreate, ProductoDetail
)

urlpatterns = [
    path('categorias/', CategoriaListCreate.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', CategoriaDetail.as_view(), name='categoria-detail'),
    path('productos/', ProductoListCreate.as_view(), name='producto-list'),
    path('productos/<int:pk>/', ProductoDetail.as_view(), name='producto-detail'),
]