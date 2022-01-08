from django.urls import path
from .views import WorkerListAPIView, WorkerInfoAPIView, StoreListAPIView, CreateStoreAPIView, VisitStoreAPIView

urlpatterns = [
    path('workers', WorkerListAPIView.as_view(), name="workers"),
    path('stores', StoreListAPIView.as_view(), name="stores"),
    path('visit', VisitStoreAPIView.as_view(), name="visit"),
  
    path('workers/<str:slug>', WorkerInfoAPIView.as_view(), name="worker"),
    path('store', CreateStoreAPIView.as_view(), name="Stores"),
]
