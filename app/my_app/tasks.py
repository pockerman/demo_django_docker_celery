import time

from celery import shared_task


@shared_task(name="create_task")
def create_task(task_time, task_id):
    print("INFO: starting task...")

    run_task(task_id=task_id, task_time=task_time)
    print("INFO: Task finished...")
    return True


def run_task(task_id, task_time):

    from .models import TaskModel

    task = TaskModel.objects.get(task_id=task_id)
    task.result = "RUNNING"
    try:
        time.sleep(int(task_time) * 10)
        task.result = "SUCCESS"
    except Exception as e:
        print("INFO: An exception occured {}".format(str(e)))
        task.result = 'FAILURE' #TaskModel.RESULT_OPTIONS[3][1]
        task.error_explanation = str(e)
    finally:
        task.save()

