"""restapis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from restapisapp.views import Article_list, article_detail, ArticleAPIView, Articledetails, Book_list, BookAPIView, \
    delete_books, book_detail, Add_Book, update_book, filter_book, LoginApi
# from restapisapp.views import UserDetailAPI,RegisterUserAPIView
from restapisapp.views import *
from restapisapp.playlistviews import *
urlpatterns = [
    path('admin/', admin.site.urls),

    # path('article/', Article_list),
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:pk>/', article_detail),
    path('detail/<int:id>/',Articledetails.as_view()),
    path('generic/article/',ArticleAPIView.as_view()),
    path('addbook/', Add_Book),
    path('book/', BookAPIView.as_view()),
    path('bookdetails/<int:pk>/', book_detail),
    path('deletebook/<int:pk>/', delete_books),
    path('updatebook/<int:pk>/', update_book),
    path('filterbook/', filter_book),
    path('login/', LoginApi.as_view()),

    path('updatepassword/', update_password),
    path('register/', RegisterApi.as_view(), name='register'),
    path('change-password/', ChangePasswordView.as_view()),
    # path('update-profile/<int:pk>', UpdateProfile.as_view()),
    path('update-profile/<int:id>/', UpdateProfileView.as_view()),


    # path("get-details", UserDetailAPI.as_view()),
    # path('register', RegisterUserAPIView.as_view()),



    # playlist_urls
    path('addsongs/',Add_Songs),
    path('deletesong/<int:pk>/', Delete_Song),
    path('allsongs/', GetAllSongsdetails),
    path('singlesong/<int:pk>/', Singlesong_detail),
    path('addplaylist/', Add_Playlist),
    path('getallplaylist/', GetAllPlaylistdetails),
    path('playlist/<int:pk>/', get_playlist_by_id),
    path('registerplaylist/', RegisterPlaylistApi.as_view(), name='register'),
    path('login/', PlaylistLoginApi.as_view()),
    path('deleteplaylist/<int:pk>/', Delete_Playlist),
    path('getuserplaylist/', GetAllPlaylistbyid),
    path('logout/', User_logout),


    # path('deletebook/<int:pk>/', delete_books),



]
