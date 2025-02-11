from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.thread_list, name='thread_list'),
    path('<int:thread_id>/', views.thread_detail, name='thread_detail'),
    path('<int:thread_id>/delete/', views.delete_thread, name='delete_thread'),
    path('<int:thread_id>/edit/', views.edit_thread, name='edit_thread'),
    path('<int:thread_id>/posts/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('<int:thread_id>/posts/<int:post_id>/edit/', views.edit_post, name='edit_post'),
]