
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload-book'),
    path('<int:book_id>/edit/', views.update_book, name='update'),
    path('<int:book_id>/delete/', views.delete_book, name="delete"),
]
