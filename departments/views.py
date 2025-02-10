from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404

from .models import Department, Boss
from .forms import DepartmentForm
from groups.models import Group
from subjects.models import Subject
from students.models import Student
from teachers.models import Teacher


def home(request):
    total_groups = Group.objects.count()
    total_students = Student.objects.count()
    total_subjects = Subject.objects.count()
    total_teachers = Teacher.objects.count()
    subject_names = [subject.name for subject in Subject.objects.all()]
    subject_teachers_counts = [subject.teacher.count() for subject in Subject.objects.all()]

    ctx = {
        'total_groups': total_groups,
        'total_students': total_students,
        'total_subjects': total_subjects,
        'total_teachers': total_teachers,
        'subject_names': subject_names,
        'subject_teachers_counts': subject_teachers_counts,
    }
    return render(request, 'dashboard.html', ctx)


def department_list(request):
    departments = Department.objects.all()
    bosses = Boss.objects.all()
    search = request.GET.get('search', '')
    boss_id = request.GET.get('boss', '')
    selected_status = request.GET.get('status', '')
    if search:
        departments = departments.filter(name__icontains=search)
    if boss_id:
        departments = departments.filter(boss_id=boss_id)
    if selected_status:
        departments = departments.filter(status=selected_status)
    ctx = {
        'departments': departments,
        'search': search,
        'bosses': bosses,
        'selected_boss': boss_id,
        'selected_status': selected_status,
    }
    return render(request,'departments/list.html', ctx)

def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('departments:list')
    else:
        form = DepartmentForm()
    return render(request,'departments/form.html', {'form': form})

def department_detail(request, pk, year, month, day, slug):
    department = get_object_or_404(
        Department,
        pk=pk,
        slug=slug,
        created_at__year=year,
        created_at__month=month,
        created_at__day=day,
    )
    teachers = Teacher.objects.filter(department=department)
    subjects = Subject.objects.filter(department=department)
    students = Student.objects.all()

    ctx = {
        'department': department,
        'students': students,
        'teachers': teachers,
        'subjects': subjects,
    }
    return render(request, 'departments/detail.html', ctx)

def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('departments:list')
    else:
        form = DepartmentForm(instance=department)
    return render(request,'departments/form.html', {'form': form})

def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('departments:list')
    return render(request,'departments/delete.html', {'department': department})




