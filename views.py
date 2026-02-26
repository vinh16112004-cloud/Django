from django.shortcuts import get_object_or_404, render, redirect
from .models import Course, Question, Submission, Choice, Enrollment

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        weights = request.POST.getlist('choice')
        # Logic tạo Submission và lưu kết quả tại đây
        return redirect('onlinecourse:show_exam_result', course_id=course.id, submission_id=submission.id)

def show_exam_result(request, course_id, submission_id):
    context = {}
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    context['course'] = course
    context['submission'] = submission
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
