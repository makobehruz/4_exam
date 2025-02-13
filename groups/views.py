from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404

from teachers.models import Teacher
from .models import Group
from .forms import GroupForm
from students.models import Student


def group_list(request):
    groups = Group.objects.all()
    teachers = Teacher.objects.all()
    search = request.GET.get('search')
    selected_grade = request.GET.get('grade', '')
    selected_status = request.GET.get('status', '')
    selected_teacher = request.GET.get('teacher', '')
    total_students = Student.objects.count()

    if search:
        groups = groups.filter(name__icontains=search)

    if selected_grade:
        groups = groups.filter(grade=selected_grade)

    if selected_teacher:
        try:
            teacher_obj = Teacher.objects.get(id=selected_teacher)
            groups = groups.filter(teacher=teacher_obj)
        except Teacher.DoesNotExist:
            groups = groups.none()

    if selected_status:
        groups = groups.filter(status=selected_status)


    ctx = {
        'groups': groups,
        'search': search,
        'teachers': teachers,
        'selected_grade': selected_grade,
        'selected_status': selected_status,
        'total_students': total_students,
        'selected_teacher': selected_teacher,
    }
    return render(request, 'groups/list.html', ctx)
def group_create(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groups:list')
    else:
        form = GroupForm()
    return render(request,'groups/form.html', {'form': form})

def group_detail(request, pk, year, month, day, slug):
    group = get_object_or_404(
        Group,
        pk=pk,
        slug = slug,
        created_at__year = year,
        created_at__month = month,
        created_at__day = day
    )
    students = Student.objects.filter(group=group)
    subjects = group.subjects.all()
    ctx = {
        'group': group,
        'subjects': subjects,
        'students': students,
    }
    return render(request, 'groups/detail.html', ctx)

def group_update(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('groups:list')
    else:
        form = GroupForm(instance=group)
    ctx = {
        'form': form,
        'group': group,
    }
    return render(request,'groups/form.html', ctx)

def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group.delete()
        return redirect('groups:list')
    return render(request,'groups/delete.html', {'group': group})

