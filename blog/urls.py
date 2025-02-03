from django.urls import path
from .views import BlogListView, BlogDetailView ,search , blog_chart_view

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),  
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),  
    path('search/', search, name='search'),
    path('chart/', blog_chart_view, name='chart'),

]
