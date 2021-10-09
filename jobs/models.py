from django.db import models
from profiles.models import Profile
import random 
from django.utils.text import slugify

job_type_choices = [
    ('part time','part-time'),
    ('full time','full-time'),
    ('internship','internship'),
    ('freelance','freelance'),
]
job_category_choices = [
    ('Education & Training','Education & Training'),
    ('Sales and Marketing','Sales and Marketing'),
    ('Computer Programing','Computer Programing'),
    ('Customer Support','Customer Support'),
    ('Design & Multimedia','Design & Multimedia'),
    ('Web Development','Web Development'),
    ('Medical/Pharma','Medical/Pharma'),
    ('Engineer/Architects','Engineer/Architects'),
]

class Job(models.Model):
    title = models.CharField(max_length=300)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='jobs/', null=True, blank=True)
    location = models.CharField(max_length=500)
    short_desc = models.CharField(max_length=500)
    description = models.TextField()
    category = models.CharField(max_length=200, choices=job_category_choices)
    vacancy = models.IntegerField()
    job_type = models.CharField(max_length=50, choices=job_type_choices)
    salary = models.IntegerField()
    pubished_at = models.DateField(auto_now_add=True)
    company = models.CharField(max_length=150, null=True,blank=True)
    country = models.CharField(max_length=150, null=True,blank=True)
    requerment = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        m =''
        temp=''
        
        if not self.slug:
            self.slug=slugify(self.title)
        temp = m = self.slug
        try:
            exist = Job.objects.get(slug=m)
        
            while exist:
                temp=m
                temp+=(str)(random.randint(1,1000000))
                exist = Job.objects.get(slug=temp)
        except:
            print(temp)
            self.slug = temp
            super(Job, self).save(*args, **kwargs)