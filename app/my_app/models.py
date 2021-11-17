import uuid
from django.db import models

# Create your models here.
from .tasks import create_task

DEFAULT_ERROR_EXPLANATION = "No Error"


class TaskModel(models.Model):
    RESULT_OPTIONS = (("PENDING", "PENDING"),
                      ("RUNNING", "RUNNING"),
                      ("SUCCESS", "SUCCESS"),
                      ("FAILURE", "FAILURE"),)

    # the task id of the computation
    task_id = models.CharField(max_length=200, primary_key=True)
    result = models.CharField(max_length=50, choices=RESULT_OPTIONS)
    error_explanation = models.TextField(default=DEFAULT_ERROR_EXPLANATION)

    class Meta:
        db_table = 'tasks'

    @staticmethod
    def create_and_launch(data):
        task_id = str(uuid.uuid4())
        task = TaskModel()
        task.task_id = task_id
        task.result = TaskModel.RESULT_OPTIONS[0][0]
        task.save()

        # launch the task
        create_task.delay(data, task_id)
        return task_id

    @staticmethod
    def launch(data, task_id):
        return create_task.delay(data)
