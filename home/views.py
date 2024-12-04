from wsgiref.util import request_uri

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import  filters, permissions
from .permissions import IsOwner, IsAuthenticatedOrReadOnly, IsAdminUser
from .serializer import RegisterSerializer, RegisterSerializer, CourseSerializer, LessonSerializer, CommentSerializer, \
    VideolessonSerializer, RateSerializer, EmailSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import throttling
from .models import Courses, Lessons, Comments, VideoLesson, RateLesson

from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER

# Create your views here.


class RegisterView(APIView):
    """BU view userlarinni registratsiya qilish uchun"""
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseViewSet(ModelViewSet):
    """ Bu view Course modelining objectlari qaytarish uchun
    2 xil versiya bor"""
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.version == 'v1':
            return Courses.objects.all()
        elif self.request.version == 'v2':
            return Courses.objects.all().order_by('-id')
        else:
            raise ValueError(f"Unsupported API version: {self.request.version}")


class LessonViewSet(ModelViewSet):
    """Bu view lesson modelining objectlari qaytarish uchun  """
    queryset = Lessons.objects.all()
    serializer_class = LessonSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['course_id','id', 'title', 'created_at']


    def get_queryset(self):
        q = self.request.query_params.get('q', False)
        if q:
            return Lessons.objects.filter(title__icontains = q)
        else:
            return Lessons.objects.all()


class CommentViewSet(ModelViewSet):
    """Bu view commentt modelining objectlari qaytarish uchun """
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwner]


class VideoUploadViewSet(ModelViewSet):
    """Bu view videolarni  modelining objectlari qaytarish uchun """
    queryset = VideoLesson.objects.all()
    serializer_class = VideolessonSerializer



class RateLessonViewSet(ModelViewSet):
    """Bu view rate clasi modelining objectlari qaytarish uchun """
    queryset = RateLesson.objects.all()
    serializer_class = RateSerializer






class SendEmailAPIView(APIView):
    """Bu email Jonatish uchun"""
    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        subject = serializer.validated_data.get("subject")
        message = serializer.validated_data.get("message")

        for i in ['madrahimovq@gmail.com', 'shunchakiabdujabbor@gmail.com',
             'abdulvosid780@gmail.com']:
            send_mail(
                subject,
                message,
                EMAIL_HOST_USER,
                [i]
            )

        return Response("Yuborildi!!!")







