from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404

from .forms import SubjectForm
from departments.models import Department
from .models import Subject
from teachers.models import Teacher
from groups.models import Group


def subject_list(request):
    subjects = Subject.objects.annotate(
        total_students=Count('groups__students', distinct=True),
        )
    departments = Department.objects.all()
    search = request.GET.get('search', '')
    selected_grade = request.GET.get('grade', '')
    selected_status = request.GET.get('status', '')
    selected_department = request.GET.get('selected_department', '')

    if selected_status:
        subjects = subjects.filter(status=selected_status)

    if search:
        subjects = subjects.filter(name__icontains=search)

    if selected_department:
        subjects = subjects.filter(department_id=selected_department)

    if selected_grade:
        subjects = subjects.filter(grade=selected_grade)

    ctx = {
        'subjects': subjects,
        'search': search,
        'departments': departments,
        'selected_department': selected_department,
        'selected_grade': selected_grade,
        'selected_status': selected_status,
    }
    return render(request, 'subjects/list.html', ctx)



def subject_create(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subjects:list')
    else:
        form = SubjectForm()
    return render(request,'subjects/form.html', {'form': form})

def subject_detail(request, pk, year, month, day, slug):
    subject = Subject.objects.annotate(
        total_students=Count('groups__students', distinct=True),
       ).get(
        pk=pk,
        slug=slug,
        created_at__year=year,
        created_at__month=month,
        created_at__day=day,
    )
    prerequisites = subject.prerequisites.all()
    teachers = Teacher.objects.filter(subjects=subject)
    groups = Group.objects.filter(subjects=subject)
    ctx = {
        'subject': subject,
        'prerequisites': prerequisites,
        'teachers': teachers,
        'groups': groups,
    }
    return render(request,'subjects/detail.html', ctx)

def subject_update(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subjects:list')
    else:
        form = SubjectForm(instance=subject)
    return render(request,'subjects/form.html', {'form': form})

def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.delete()
        return redirect('subjects:list')
    return render(request,'subjects/delete.html', {'subject': subject})




