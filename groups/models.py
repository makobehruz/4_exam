from django.db import models
from django.shortcuts import reverse

from departments.base_model import BaseModel
from subjects.models import Subject
from teachers.models import Teacher
from django.utils.text import slugify


class Group(BaseModel):
    STATUS = [
        ('ac', 'Active'),
        ('in', 'Inactive'),
    ]
    GRADE_LEVELS = [
        ('9', 'Grade 9'),
        ('10', 'Grade 10'),
        ('11', 'Grade 11'),
        ('12', 'Grade 12'),
    ]
    SCHEDULE = [
        ('morning', 'Morning Session'),
        ('afternoon', 'Afternoon Session'),
        ('evening', 'Evening Session'),
    ]
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, blank=True, null=True, on_delete=models.CASCADE, related_name='groups')
    academic_year = models.CharField(max_length=100)
    grade = models.CharField(max_length=25, choices=GRADE_LEVELS)
    schedule = models.CharField(max_length=25, choices=SCHEDULE)
    max_students = models.PositiveIntegerField()
    desc = models.TextField()
    subjects = models.ManyToManyField(Subject, related_name='groups')
    status = models.CharField(max_length=20, choices=STATUS)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Group, self).save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('groups:detail', args=[
            self.pk,
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug,
        ])

    def get_update_url(self):
        return reverse('groups:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('groups:delete', args=[self.pk])