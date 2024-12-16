from ..models import Task


def create_new_task(title="Default Task", completed="False"):
    return Task.objects.create(title=title, completed=completed)
