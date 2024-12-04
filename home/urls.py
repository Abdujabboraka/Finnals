from django.urls import path, include
from .views import RegisterView, CourseViewSet, LessonViewSet, CommentViewSet, VideoUploadViewSet, RateLessonViewSet, SendEmailAPIView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('courses', CourseViewSet)
router.register('comments', CommentViewSet)
router.register('lessons', LessonViewSet)
router.register('video', VideoUploadViewSet)
router.register('rate', RateLessonViewSet)


urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('email/', SendEmailAPIView.as_view()),
    path('', include(router.urls))

]
