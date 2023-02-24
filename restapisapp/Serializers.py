from rest_framework import serializers
from .models import Article, Book
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User


class ArticleSerializer(serializers.ModelSerializer):
    # id=serializers.IntegerField()
    class Meta:
        model = Article
        # title = serializers.CharField(max_length=100)
        # author = serializers.CharField(max_length=100)
        # email = serializers.EmailField(max_length=100)
        # date = serializers .DateTimeField()
        fields = '__all__'

    # def create(self, validated_data):
    #     return Article.objects.create(validated_data)
    #
    # def update(self,  instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.author = validated_data.get('title', instance.author)
    #     # instance.email = validated_data.get('title', instance.email)
    #     # instance.date = validated_data.get('title', instance.date)
    #     instance.save
    #     return instance


class BookSerializer(serializers.ModelSerializer):
    # id=serializers.IntegerField()
    class Meta:
        model = Book
        # title = serializers.CharField(max_length=100)
        # author = serializers.CharField(max_length=100)
        # email = serializers.EmailField(max_length=100)
        # date = serializers .DateTimeField()
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    # id=serializers.IntegerField()
    class Meta:
        model = User
        # title = serializers.CharField(max_length=100)
        # author = serializers.CharField(max_length=100)
        # email = serializers.EmailField(max_length=100)
        # date = serializers .DateTimeField()
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    # id=serializers.IntegerField()
    class Meta:
        model = User
        # fields = [
        #     'username','email','password'
        # ]
        fields = ('id', 'username', 'email', 'password')



def create(self, validated_data):
    user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

    return user


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50, required=True)
    password = serializers.CharField(max_length=50, required=True)


class RegisterSerialzierNew(serializers.Serializer):
    first_name=serializers.CharField(max_length=30,required=True)
    last_name=serializers.CharField(max_length=30,required=True)
    password=serializers.CharField(max_length=30,required=True)
    email=serializers.EmailField(required=True)


# class UpdateUserSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email')
#         extra_kwargs = {
#             'first_name': {'required': True},
#             'last_name': {'required': True},
#         }
#
#     def validate_email(self, value):
#         user = self.context['request'].user
#         if User.objects.exclude(pk=user.pk).filter(email=value).exists():
#             raise serializers.ValidationError({"email": "This email is already in use."})
#         return value
#
#     def validate_username(self, value):
#         user = self.context['request'].user
#         if User.objects.exclude(pk=user.pk).filter(username=value).exists():
#             raise serializers.ValidationError({"username": "This username is already in use."})
#         return value
#
#     def update(self, instance, validated_data):
#         instance.first_name = validated_data['first_name']
#         instance.last_name = validated_data['last_name']
#         instance.email = validated_data['email']
#         instance.username = validated_data['username']
#
#         instance.save()
#
#         return instance

# class UserSerializer(serializers.Serializer):
#     profile = RegisterSerialzierNew(source="userprofile", many=False)
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'first_name', 'last_name', 'profile')
#
#         # Custom .update() method for serializer to handle UserProfile data update
#         def update(self, instance, validated_data):
#             userprofile_serializer = self.fields['profile']
#             userprofile_instance = instance.userprofile
#             userprofile_data = validated_data.pop('userprofile', {})
#
#             # to access the UserProfile fields in here
#             # mobile = userprofile_data.get('mobile')
#
#             # update the userprofile fields
#             userprofile_serializer.update(userprofile_instance, userprofile_data)
#
#             instance = super().update(instance, validated_data)
#             return instance

class UsereSerializer(serializers.Serializer):
    # id=serializers.IntegerField()
    class Meta:
        model = User
        # title = serializers.CharField(max_length=100)
        # author = serializers.CharField(max_length=100)
        # email = serializers.EmailField(max_length=100)
        # date = serializers .DateTimeField()
        fields = '__all__'