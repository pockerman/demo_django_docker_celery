from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist

#from app.hello_world_django import celery_app as app
from .models import TaskModel

# Create your views here.


def index(request):

    template = loader.get_template('my_app/index.html')
    context = {}
    
    if request.method == 'POST':
        # get the time to sleep
        value_to_sleep = request.POST.get("value-input")

        # create the task
        task_id = TaskModel.create_and_launch(data=value_to_sleep)
        return redirect('get_result_view', task_id=task_id)

    return HttpResponse(template.render(context, request))


def get_result_view(request, task_id):
    template = loader.get_template('my_app/result_view.html')

    task = TaskModel.objects.get(task_id=task_id)
    context = {"task": task}
    return HttpResponse(template.render(context, request))

