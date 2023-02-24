from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import  JSONParser
from .models import Article,Book,User
from .Serializers import *

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
import json
from rest_framework.authtoken.models import Token
# from knox.models import AuthToken

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny



from django.contrib.auth import authenticate #add this







# class RegisterAPI(generics.GenericAPIView):
#     serializer_class = RegisterSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#         "user": UserSerializer(user, context=self.get_serializer_context()).data,
#         "token": AuthToken.objects.create(user)[1]
#         })


# class GenericAPIVIEW(generics.GenericAPIView, mixins.ListModelMixin,mixins.CreateModelMixin):
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()
#
#     def get(self, request):
#         return self.list(request)
#
#
@csrf_exempt
@api_view(['GET','POST'])
def Book_list(request):

    if request.method == 'GET':
        articles = Book.objects.all()
        serializer = BookSerializer(articles, many=True)
        return JsonResponse(serializer.data,safe= False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BookSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors,status=400)
class ArticleAPIView(APIView):

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class BookAPIView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
@api_view(['GET','POST','DELETE'])
def Article_list(request):

    if request.method == 'GET':

        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
@api_view(['GET','POST'])
def Add_Book(request):

    if request.method == 'GET':
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return JsonResponse(serializer.data, safe = False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BookSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class Articledetails(APIView):

    def get_object(self,id):
        try:
            return Article.objects.get(id=id)

        except Article.DoesnotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        article=self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=200)

    def put(self,request,id):
        article=self.get_object(id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        article=self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Articledetails(APIView):

    def get_object(self,id):
        try:
            return Article.objects.get(id=id)

        except Article.DoesnotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        article=self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=200)

    def put(self,request,id):
        article=self.get_object(id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        article=self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET','PUT','DELETE'])
def article_detail(request,pk):
    try:
        article = Article.objects.get(pk=pk)


    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return  Response(serializer.data, status=200)

    elif request.method == 'PUT':

        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method  == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def book_detail(request,pk):
    try:
        book = Book.objects.get(pk=pk)

    except Book.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return  Response(serializer.data, status=200)

    elif request.method == 'PUT':

        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','DELETE'])
def delete_books(request,pk):
    try:
        book = Book.objects.get(pk=pk)

    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return  Response(serializer.data, status=200)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def update_book(request, pk):
        try:
            user = User.objects.get(pk=pk)
            print(user)

        except Book.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = UserSerializer(user)
            return Response(serializer.data, status=200)

        # elif request.method == 'PUT':
        #     data = JSONParser().parse(request)
        #     serializer = BookSerializer(book, data=data)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response(serializer.data)
        #     return JsonResponse(serializer.errors, status=400)
    # elif request.method == 'PUT':
    #
    #     serializer = ArticleSerializer(article, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def filter_book(request):
    if request.method == 'GET':
        book = Book.objects.filter(pages__lte=500)

        # book1=book.pages()
        serializer = BookSerializer(book,many=True)
        return Response(serializer.data, status=200)


class RegisterApi(APIView):
    serializer_class = RegisterSerialzierNew

    def post(self, request):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        serializer = self.serializer_class(data=request.data)
        response = serializer.is_valid(raise_exception=True)

        user = User.objects.create_user(email=(request.data.get('email').lower()),
                                            username=request.data.get('email'),
                                            first_name=first_name,
                                            last_name=last_name,
                                            )
        user.is_active = True
        user.set_password(request.data.get('password'))
        user.save()
        token = Token.objects.get_or_create(user=user)[0].key
        get_user = get_object_or_404(User, email=user.username)
        user_profile_serializer = RegisterSerializer(get_user)
        user_profile_serializer = user_profile_serializer.data
        return Response(
            {"status_code": status.HTTP_200_OK, "success": True, "message": "user login success", "data": user_profile_serializer})


# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny,))
class LoginApi(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    def post(self, request):
        print("1")
        serializer = self.serializer_class(data=request.data)
        response = serializer.is_valid(raise_exception=True)
        print("2")
        return self.on_valid_request_data(serializer.validated_data, request)

    def on_valid_request_data(self, data, request):
        email = data.get('username')
        password = data.get('password')
        user_obj = User.objects.filter(username=email).last()
        if user_obj:
            try:
                user = authenticate(username=user_obj.username, password=password)
                if user is not None:
                    user_profile_serializer = UserSerializer(user)
                    user_profile_serializer = user_profile_serializer.data
                    token, created = Token.objects.get_or_create(user=user)
                    response = {
                        'token': token.key,
                        'user_profile': user_profile_serializer
                    }
                    return Response({"status_code":status.HTTP_200_OK,"success":True,"message":"user login success","data":response})

                return Response({"status_code":status.HTTP_400_BAD_REQUEST,"success":False,"message":"user login fail"})
            except Exception as e:
                return Response(
                    {"status_code": status.HTTP_400_BAD_REQUEST, "success": False, "message": "user login fail"})

        else:
            return Response(
                {"status_code": status.HTTP_400_BAD_REQUEST, "success": False, "message": "user login fail"})

def update_password(self, instance, validated_data):
    for attr, value in validated_data.items():
        if attr == 'password':
            instance.set_password(value)
        else:
            setattr(instance, attr, value)
    instance.save()
    return instance


class ChangePasswordView(APIView):
    """
    An endpoint for changing password.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer
    def post(self, request):
        self.object = self.get_object()
        serializer = self. serializer_class(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

# class UpdateProfile(APIView):
#     def update(request, pk):
#         try:
#             # book = User.objects.get(pk=pk)
#             user_profile = User.objects.get(pk=pk)
#
#
#         except User.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#         if request.method == 'GET':
#             user_profile_serializer = UserSerializer(user_profile)
#             print(user_profile_serializer)
#             # serializer = BookSerializer(book)
#             return Response(user_profile_serializer.data, status=200)
#         #
#         # elif request.method == 'PUT':
#         #     data = JSONParser().parse(request)
#         #     serializer = UserSerializer(user_profile, data=data)
#         #     if serializer.is_valid():
#         #         serializer.save()
#         #         return Response(serializer.data)
#             # return JsonResponse(serializer.errors, status=400)
#         response = {
#
#         }

# class UpdateProfileView(generics.UpdateAPIView):
#
#     queryset = User.objects.all()
#     permission_classes = (IsAuthenticated,)
#     serializer_class = UpdateUserSerializer


# class UpdateProfileView(APIView):
#     def update_profile(request, pk):
#         try:
#             user = User.objects.get(pk=pk)
#
#         except User.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#         if request.method == 'GET':
#             serializer = UserSerializer(user)
#             return Response(serializer.data, status=200)
#             # try:
#             #     user = User.objects.get(pk=pk)
#             #     print(user)
#             #
#             # except Book.DoesNotExist:
#             #     return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#             #
#             # if request.method == 'GET':
#             #     serializer = UserSerializer(user)
#             #     return Response(serializer.data, status=200)
#             #
#             # elif request.method == 'PUT':
#             #     data = JSONParser().parse(request)
#             #     serializer = UserSerializer(user, data=data)
#             #     if serializer.is_valid():
#             #         serializer.save()
#             #         return Response(serializer.data)
#             #     return JsonResponse(serializer.errors, status=400)
#
#     #         try:
#     #             user = User.objects.get(pk=pk)
#     #
#     #         except User.DoesNotExist:
#     #             return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#     #
#     #         if request.method == 'GET':
#     #             serializer = UserSerializer(user)
#     #             return Response(serializer.data, status=200)
#     #
#     #         elif request.method == 'PUT':
#     #
#     #             serializer = UserSerializer(user, data=request.data)
#     #             if serializer.is_valid():
#     #                 serializer.save()
#     #                 return Response(serializer.data)
#     #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     #
#     #
class UpdateProfileView(APIView):

    def get_object(self,id):

        try:
            return User.objects.get(id=id)

        except User.DoesnotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        user=self.get_object(id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=200)

    def post(self,request,id):
        user=self.get_object(id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







