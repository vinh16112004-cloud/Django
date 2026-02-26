from django.urls import path
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    # Các path mặc định đã có sẵn
    path(route='', view=views.CourseListView.as_view(), name='index'),
    path('course/<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),
    path('registration/', views.registration_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),

    # --- THÊM 2 PATH DƯỚI ĐÂY ---
    # Path cho việc nộp bài thi (POST request)
    path('course/<int:course_id>/submit/', views.submit, name='submit'),
    
    # Path cho việc hiển thị kết quả bài thi
    path('course/<int:course_id>/submission/<int:submission_id>/result/', 
         views.show_exam_result, name='show_exam_result'),
]
