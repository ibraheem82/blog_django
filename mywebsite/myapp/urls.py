from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('blog', views.blog, name = 'blog'),
    path('detail/<str:slug>', views.detailsPage, name = 'detail'),
    path('create-post', views.createPost, name = 'create-blog'),
    path('update-post/<str:slug>', views.updatePost, name='update'),
    path('delete-post/<str:slug>', views.deletePost, name='delete')
]