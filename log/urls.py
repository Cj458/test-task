from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.index_page, name="login"),
    # path('logout_user', views.logout_user, name='logout'),
    # path('register_user', views.register_user, name='register_user'),
]