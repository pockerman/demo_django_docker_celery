from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import TaskModel

# Create your views here.

def index(request):

    template = loader.get_template('my_app/index.html')
    context = {}
    
    if request.methd == 'POST':
    
    	# get the time to sleep
    	value_to_sleep = request.POST.get("value-input")
    	
    	# create the task
    	task_id = TaskModel.create_and_launch(data=value_to_sleep)
    	
    	return redirect('tasks/{0}'.format(task_id))
    
    
    return HttpResponse(template.render(context, request))


def get_result_view(request, task_id):
    pass
