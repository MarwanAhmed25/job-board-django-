from .models import Job
from django.forms import ModelForm 

class JobForm(ModelForm):
    
    class Meta:
        model = Job
        fields = ['title','image','location',
        'short_desc','description','category',
         'vacancy','job_type','salary','company','requerment','country']
