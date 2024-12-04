from django.contrib import admin
from .models import Courses, Lessons, Comments, RateLesson
# Register your models here.


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('name',)


@admin.register(Lessons)
class LessonsAdmin(admin.ModelAdmin):
    list_display = ('course', 'title', 'content')
    search_fields = ('course__name', 'title', 'content')
    list_filter = ('course', 'created_at')
    ordering = ('course', 'created_at')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):

    list_display = ('lesson', 'user', 'text')
    search_fields = ('lesson__course__name', 'lesson__title', 'user__username', 'text')
    list_filter = ('lesson__course', 'user', )
    ordering = ('lesson__course', )


@admin.register(RateLesson)
class RateLessonAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'user', 'rate')
    search_fields = ('lesson__course__name', 'lesson__title', 'user__username', 'rate')
    list_filter = ('lesson__course', 'user', 'rate', )
    ordering = ('lesson__course',)


admin.site.site_header = 'Imtihon Projecti'
admin.site.site_title = 'Imtihon Projecti Admin'
admin.site.index_title = 'Boshqaruv Paneli'

