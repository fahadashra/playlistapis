
from django.urls import path
from .views import Article_list,article_detail
from django.urls import path,include
# from rest_framework.authtoken import views

urlpatterns = [
    path('article/',Article_list),
    path('details/int:pk>/',article_detail),
    # path('', include('api.urls')),
    # path('api-token-auth', views.obtain_auth_token)
]