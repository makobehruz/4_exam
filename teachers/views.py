from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect

from students.models import Student
from subjects.models import Subject
from .forms import TeacherForm
from .models import Teacher, Department


def teacher_list(request):
    teachers = Teacher.objects.all()
    departments = Department.objects.all()
    subjects = Subject.objects.all()
    search = request.GET.get('search', '').strip()
    selected_subject = request.GET.get('subject', '').strip()
    selected_status = request.GET.get('status', '').strip()
    selected_department = request.GET.get('selected_department', '').strip()

    if search:
        teachers = teachers.filter(first_name__icontains=search)

    if selected_department:
        teachers = teachers.filter(department_id=selected_department)

    if selected_subject:
        teachers = teachers.filter(subjects__id=selected_subject)

    if selected_status:
        teachers = teachers.filter(status=selected_status)

    ctx = {
        'teachers': teachers,
        'subjects': subjects,
        'departments': departments,
        'search': search,
        'selected_status': selected_status,
        'selected_department': selected_department,
        'selected_subject': selected_subject,
    }
    return render(request, 'teachers/list.html', ctx)


def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("teachers:list")
    else:
        form = TeacherForm()
    return render(request, 'teachers/form.html', {'form': form})

def teacher_detail(request, pk, year, month, day, slug):
    students = Student.objects.all()
    teacher = get_object_or_404(
        Teacher,
        pk=pk,
        slug=slug,
        created_at__year=year,
        created_at__month=month,
        created_at__day=day,
    )
    ctx = {
        'teacher': teacher,
        'students': students,
    }
    return render(request,'teachers/detail.html', ctx)

def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect("teachers:list")
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'teachers/form.html', {'form': form})

def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teachers:list')
    return render(request,'teachers/delete.html', {'teacher': teacher})