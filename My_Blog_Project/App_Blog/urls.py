from django.urls import path
from . import views

app_name = 'App_Blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name= 'blog_list'),
    path('write', views.CreateBlog.as_view(), name= 'write_blog'),
    path('details/<slug:slug>', views.blog_details, name='blog_details'),
    path('liked/<pk>', views.liked, name='liked_post'),
    path('unliked/<pk>', views.unliked, name='unliked_post'),
    path('my-blogs', views.MyBlog.as_view(), name= 'my_blog'),
    path('edit-blog/<pk>', views.UpdateBlog.as_view(), name= 'edit_blog'),
    path('delete-blog/<int:pk>', views.DeleteBlog.as_view(), name= 'delete_blog'),

    path('blog', views.blog, name='blog'),

]