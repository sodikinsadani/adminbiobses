from django.urls import path
from . import views

app_name = 'adminbiobses'
urlpatterns = [
    path('login/', views.login_view.as_view(), name='login'),
    path('', views.index.as_view(), name='index'),
    path('logout/', views.logout_view.as_view(), name='logout'),
    path('penerbit/', views.penerbit.as_view(), name='penerbit'),
    path('penerbit/<int:pk>/edit/', views.penerbitEdit.as_view(), name='penerbitEdit'),
    path('penerbit/<int:pk>/delete/', views.penerbitDelete.as_view(), name='penerbitDelete'),
]
