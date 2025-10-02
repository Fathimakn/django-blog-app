from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='home'),
    path('logout/',views.logout,name='logout'),
    path('login/',views.user_login,name='login'),
    path('register/',views.register,name='register'),
    path('update/<int:id>',views.update,name='update'),
    path('posts/',views.posts,name='posts'),
    path('edit_post/<int:id>',views.edit_post,name='edit_post'),
    path('add_post/',views.add_post,name='add_post')



]
