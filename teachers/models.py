from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

from departments.base_model import BaseModel
from departments.models import Department
from subjects.models import Subject


class Teacher(BaseModel):
    EMPLOYMENT = [
        ('full', 'Full Time'),
        ('part', 'Part Time'),
        ('contract', 'Contract'),
    ]
    STATUS = [
        ('ac', 'Active'),
        ('in', 'Inactive'),
    ]
    image = models.ImageField(upload_to='teachers_image/')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teachers', blank=True)
    subjects = models.ManyToManyField(Subject, related_name='teacher')
    qualification = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13)
    address = models.TextField()
    employment = models.CharField(max_length=50, choices=EMPLOYMENT)
    status = models.CharField(max_length=20, choices=STATUS)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name)
        super(Teacher, self).save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('teachers:detail', args=[
            self.pk,
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug,
        ])

    def get_update_url(self):
        return reverse('teachers:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('teachers:delete', args=[self.pk])


