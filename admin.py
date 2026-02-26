from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Lesson, LessonAdmin)
# Đừng quên register các class còn lại theo yêu cầu bài lab
