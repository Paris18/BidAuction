


from django.urls import path
from . import views

urlpatterns = [
    path('action/', views.auctionapp.as_view({'get':'get_bids','put':'updatebid'}), name='test'),
    path('adproperty/', views.auctionapp.as_view({'get':'available_bids'}), name='test'),
    path('getauction/', views.auctionapp.as_view({'post':'select_bid'}), name='test'),
]
