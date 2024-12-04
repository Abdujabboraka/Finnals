from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Comments, Courses, Lessons, VideoLesson, RateLesson



class RegisterSerializer(serializers.ModelSerializer):
    """BU register uchun serializer"""
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class CourseSerializer(serializers.ModelSerializer):
    """BU courslarni serializatsya qiishga moljallangan"""
    class Meta:
        model = Courses
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    """BU darslarni serializatsya qiishga moljallangan"""
    class Meta:
        model = Lessons
        fields = "__all__"



class VideolessonSerializer(serializers.ModelSerializer):
    """BU video darslarni serializatsya qiishga moljallangan"""
    class Meta:
        model = VideoLesson
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    """BU xabarlarini serializatsya qiishga moljallangan"""
    class Meta:
        model = Comments
        fields = "__all__"


class RateSerializer(serializers.ModelSerializer):
    """BU darsning qiymatlarini serializatsya qiishga moljallangan"""
    class Meta:
        model = RateLesson
        fields = "__all__"



class EmailSerializer(serializers.Serializer):
    """Bu email uchun serializer"""
    subject = serializers.CharField(max_length=150)
    message = serializers.CharField()