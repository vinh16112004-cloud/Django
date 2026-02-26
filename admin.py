from django.contrib import admin
# Đảm bảo import đầy đủ 7 classes như yêu cầu
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# Implementation của QuestionInline
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

# Implementation của QuestionAdmin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text', 'grade']

# Implementation của LessonAdmin (Bổ sung list_display)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']

# Đăng ký các class còn lại
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Submission)
