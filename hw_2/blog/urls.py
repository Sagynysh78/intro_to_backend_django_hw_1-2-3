from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list),
    path('<int:id>/', views.article_detail),
]
