from django.shortcuts import get_object_or_404, render, redirect
from .models import Course, Question, Submission, Choice, Enrollment

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        # 1. Lấy danh sách các Choice ID đã chọn từ form
        selected_ids = request.POST.getlist('choice')
        
        # 2. Tạo đối tượng Submission mới
        enrollment = Enrollment.objects.get(user=request.user, course=course)
        submission = Submission.objects.create(enrollment=enrollment)
        
        # 3. Lưu các Choice đã chọn vào Submission (ManyToMany)
        for choice_id in selected_ids:
            choice = get_object_or_404(Choice, pk=choice_id)
            submission.choices.add(choice)
        submission.save()
        
        return redirect('onlinecourse:show_exam_result', course_id=course.id, submission_id=submission.id)

def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    
    # Tính toán total_score và possible_score
    total_score = 0
    possible_score = 0
    selected_ids = [choice.id for choice in submission.choices.all()]
    
    for question in course.question_set.all():
        possible_score += question.grade
        # Kiểm tra xem câu trả lời có đúng hoàn toàn không
        if question.is_get_score(selected_ids):
            total_score += question.grade

    # Truyền đầy đủ context theo yêu cầu feedback
    context = {
        'course': course,
        'submission': submission,
        'grade': total_score,
        'possible': possible_score,
        'selected_ids': selected_ids
    }
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
