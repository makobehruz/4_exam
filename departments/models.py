from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

from .base_model import BaseModel


class Boss(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.name

class Department(BaseModel):
    STATUS = [
        ('ac', 'Active'),
        ('in', 'Inactive'),
    ]
    name = models.CharField(max_length=100)
    boss = models.ForeignKey(Boss, models.CASCADE, related_name='departments')
    desc = models.TextField()
    location = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13)
    status = models.CharField(max_length=2, choices=STATUS, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Department, self).save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('departments:detail', args=[
            self.pk,
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug,
        ])

    def get_update_url(self):
        return reverse('departments:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('departments:delete', args=[self.pk])


