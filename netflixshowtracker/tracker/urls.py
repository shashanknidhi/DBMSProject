from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('database/',views.database,name="database"),
    path('database/add1/',views.add1,name='add1'),
    path('database/add1/addshow/',views.addshow,name='addshow'),
    path('database/displayshow/',views.displayshow,name='displayshow'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('addtowishlist/',views.addtowishlist,name='addtowishlist'),
]