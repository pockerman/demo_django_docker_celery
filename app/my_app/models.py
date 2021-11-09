from django.db import models

# Create your models here.
from .tasks import create_task

DEFAULT_ERROR_EXPLANATION = "No Error"

class TaskModel(models.Model)

	RESULT_OPTIONS = (("PENDING", "PENDING"),
                          ("SUCCESS", "SUCCESS"),
                          ("FAILURE", "FAILURE"),)

    	# the task id of the computation
    	task_id = models.CharField(max_length=300, primary_key=True)
    	result = models.CharField(max_length=50, choices=RESULT_OPTIONS)
    	error_explanation = models.CharField(max_length=500, default=DEFAULT_ERROR_EXPLANATION)
    	
	class Meta:
        	db_table = 'tasks'
        	
        @staticmethod
        def create_and_launch(data):
        	return TaskModel.launch(data)
        	
        @staticmethod
    	def launch(data):
    		return create_task.delay(data)

        
