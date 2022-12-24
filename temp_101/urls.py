from django.urls import path, include

from temp_101 import views
urlpatterns = [
    path('', views.index, name="index"),
    path('blog/all/', views.blog_all, name="blog_all"),
    path('blog/create/', views.blog_create, name="blog-create"),
    path('blog/update/', views.blog_update, name="blog-update"),
    path('blog/delete/', views.blog_delete, name="blog-delete"),
    path('blog/delete/all/', views.blog_delete_all, name="blog-delete-all"),
   ]