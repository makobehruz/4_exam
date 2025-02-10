from django.db import models
from django.utils.text import slugify

from departments.base_model import BaseModel
from departments.models import Department
from django.shortcuts import reverse


class Prerequisite(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subject(BaseModel):
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
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='subjects')
    desc = models.TextField()
    credit_hours = models.PositiveIntegerField()
    grade = models.CharField(max_length=25, choices=GRADE_LEVELS)
    prerequisites = models.ManyToManyField(Prerequisite, blank=True, related_name="next_subjects")
    status = models.CharField(max_length=100, choices=STATUS, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Subject, self).save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('subjects:detail', args=[
            self.pk,
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug,
        ])

    def get_update_url(self):
        return reverse('subjects:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('subjects:delete', args=[self.pk])


