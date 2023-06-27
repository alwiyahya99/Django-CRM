from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('keuangan/', views.keuangan, name='keuangan'),
    path('pekerjaan/', views.pekerjaan, name='pekerjaan'),
    path('pegawai/', views.pegawai, name='pegawai'),
    path('register/', views.register_user, name='register'),
]
