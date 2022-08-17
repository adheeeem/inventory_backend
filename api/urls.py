from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('inventory/all', views.getInventoryProducts, name='invAll'),
    path('inventory/<int:pk>', views.inventory_details, name='inventory_details'),
    path('store/all', views.getStoreProducts, name='storeAll'),
    path('store/<int:pk>', views.store_details, name='store_details'),
    path('actions/all', views.getActions, name="getActions"),
    path('store/create', views.createStoreProduct, name="createStoreProduct"),
    path('inventory/create', views.createInventoryProduct, name="createInventoryProduct"),
    path('action/create', views.createAction, name="createAction"),
]

#urlpatterns = format_suffix_patterns(urlpatterns)