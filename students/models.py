from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

from departments.base_model import BaseModel
from groups.models import Group


class Student(BaseModel):
    STATUS = [
        ('ac', 'Active'),
        ('in', 'Inactive'),
    ]
    GENDER = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    GRADE_LEVELS = [
        ('1', 'Grade 1'),
        ('2', 'Grade 2'),
        ('3', 'Grade 3'),
        ('4', 'Grade 4'),
        ('5', 'Grade 5'),
        ('6', 'Grade 6'),
        ('7', 'Grade 7'),
        ('8', 'Grade 8'),
        ('9', 'Grade 9'),
        ('10', 'Grade 10'),
        ('11', 'Grade 11'),
        ('12', 'Grade 12'),
    ]
    image = models.ImageField(upload_to='students_image/')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=20, choices=GENDER)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')
    grade = models.CharField(max_length=25, choices=GRADE_LEVELS)
    address = models.TextField()
    parent_name = models.CharField(max_length=255)
    parent_phone = models.CharField(max_length=13)
    parent_email = models.EmailField(unique=True)
    status = models.CharField(max_length=20, choices=STATUS)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_detail_url(self):
        return reverse('students:detail', args=[
            self.pk,
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug,
        ])

    def get_update_url(self):
        return reverse('students:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('students:delete', args=[self.pk])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name)
        super(Student, self).save(*args, **kwargs)