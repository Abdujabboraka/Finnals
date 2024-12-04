from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Courses(models.Model):
    """BU model COURSLAR uchun ozida kours obyektlarini saqlaydi"""
    name = models.CharField(max_length=100, verbose_name='nomi')


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'kurs'
        verbose_name_plural = 'kurslar'


class Lessons(models.Model):
    """BU model darslar uchun ozida kours obyektlarini saqlaydi"""

    course = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name='kurs')
    title = models.CharField(max_length=100, verbose_name='Sarlavha')
    content = models.CharField(max_length=600, verbose_name='dars')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='sana')

    def __str__(self):
        return f"{self.title}"[:20]

    class Meta:
        verbose_name = 'Dars'
        verbose_name_plural = 'Darslar'


class VideoLesson(models.Model):
    """BU model videolar uchun ozida kours obyektlarini saqlaydi"""

    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, verbose_name='dars')
    video_file = models.FileField(upload_to='video-lessons/')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='sana')

    def __str__(self):
        return f"{self.lesson.title} - {self.video_file.name}"

    class Meta:
        verbose_name = 'Video dars'
        verbose_name_plural = 'Video darslar'



class Comments(models.Model):
    """BU model user commentlari uchun ozida kours obyektlarini saqlaydi"""

    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, verbose_name='dars')
    text = models.CharField(max_length=500, verbose_name='matn')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='avtor')

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = 'Darsning bahosi'
        verbose_name_plural = 'Darsning baholari'
        unique_together = ('user', 'lesson')  # Har bir dars uchun bitta bahol

class RateLesson(models.Model):
    """BU model Baholar uchun user baholari uchun ozida kours obyektlarini saqlaydi"""

    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, verbose_name='dars')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='avtor')
    rate = models.CharField(choices=(("like", 'like'), ("dislike", 'dislike')), max_length=8)

    def __str__(self):
        return f"{self.user}'s rate for {self.lesson}"

    class Meta:
        verbose_name = 'Darsning qiymati'
        verbose_name_plural = 'Darsning qiymatlari'
        unique_together = ('user', 'lesson')  # Har bir dars uchun bitta reyting


