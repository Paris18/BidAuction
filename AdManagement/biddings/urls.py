


from django.urls import path
from . import views

urlpatterns = [
    path('action/', views.biddingsapp.as_view({'get':'get_ad_bid','post':'bid_for_add','delete':'deletebid','put':'updatebid'}), name='test'),
]
