from django.urls import path

from . import views

urlpatterns = [
    path('', views.render_home, name="home"),
    path('orders/', views.get_orders, name="orders"),
    path('orders/offer/', views.render_offer, name='offer'),
    path('delivery/', views.render_delivery, name="delivery"),
    path('delivery/update/', views.render_update_delivery, name="update_delivery"),
    path('delivery/label/', views.render_post_label, name = "label"),
    path('deliveries/', views.get_deliveries, name="deliveries"),
    path('delivery-driver/', views.render_driver_home, name="delivery-driver"),

]
