import time

from celery import shared_task


@shared_task(name="create_task")
def create_task(task_time, task_id):
    print("INFO: starting task...")
    #task_id = create_task.request.id
    run_task(task_id=task_id, task_time=task_time)
    print("INFO: Task finished...")
    return True


def run_task(task_id, task_time):

    from .models import TaskModel

    task = TaskModel.objects.get(task_id=task_id)
    task.result = TaskModel.RESULT_OPTIONS[1][1]
    try:
        time.sleep(int(task_time) * 10)
        task.result = TaskModel.RESULT_OPTIONS[2][2]
    except Exception as e:
        print("INFO: An exception occurs {}".format(str(e)))
        task.result = TaskModel.RESULT_OPTIONS[3][3]
        
    task.save()

