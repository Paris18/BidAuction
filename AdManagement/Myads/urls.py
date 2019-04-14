

from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('advertisement/', views.advertisement.as_view({'get':'get_ad','post':'insert_for_add','delete':'deleteadd','put':'updateAd'}), name='test'),
]
