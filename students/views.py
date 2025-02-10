from django.shortcuts import render, redirect, get_object_or_404

from groups.models import Group
from subjects.models import Subject
from .forms import StudentForm
from .models import Student


def student_list(request):
    students = Student.objects.all()
    search = request.GET.get('search', '')
    groups = Group.objects.all()
    selected_grade = request.GET.get('grade', '').strip()
    selected_status = request.GET.get('status', '').strip()
    selected_group = request.GET.get('group', '').strip()
    if selected_group:
        students = students.filter(group__name__iexact=selected_group)
    if search:
        students = students.filter(first_name__icontains=search)
    if selected_grade:
        students = students.filter(grade=selected_grade)
    if selected_status:
        students = students.filter(status=selected_status)

    ctx = {
        'students': students,
        'search': search,
        'groups': groups,
        'selected_grade': selected_grade,
        'selected_status': selected_status,
        'selected_group': selected_group,
    }
    return render(request,'students/list.html', ctx)

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('students:list')
    else:
        form = StudentForm()
    return render(request,'students/form.html', {'form': form})

def student_detail(request, pk, year, month, day, slug):
    student = get_object_or_404(
        Student,
        pk=pk,
        slug=slug,
        created_at__year=year,
        created_at__month=month,
        created_at__day=day,
    )
    subjects = Subject.objects.filter(groups__students=student).distinct()
    ctx = {
        'student': student,
        'subjects': subjects,
    }
    return render(request, 'students/detail.html', ctx)

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students:list')
    else:
        form = StudentForm(instance=student)
    return render(request,'students/form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('students:list')
    return render(request,'students/delete.html', {'student': student})

