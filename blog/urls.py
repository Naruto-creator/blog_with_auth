from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name="home"),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name="post_detail"),
    path('blog/new/', views.BlogCreateView.as_view(), name="new_post"),
    path('blog/<int:pk>/edit/', views.BlogUpdateView.as_view(), name="post_edit"),
    path('blog/<int:pk>/delete/', views.BlogDeleteView.as_view(), name="post_delete"),
]