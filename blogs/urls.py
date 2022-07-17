from django.urls import path
from .views import PostListView, PostDetailView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('<int:pk>/post/', PostDetailView.as_view(), name='detail')
]