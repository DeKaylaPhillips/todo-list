from ..serializers import TaskSerializer


def fetch_all_tasks(Task):
    tasks = Task.objects.all().order_by("id")
    if not tasks.exists():
        return {"error": "No tasks found in list."}
    return TaskSerializer(tasks, many=True).data


def validate_and_create_a_task(Task, request_data):
    serializer = TaskSerializer(data=request_data)
    if serializer.is_valid():
        task = Task.objects.create(**serializer.validated_data)
        return TaskSerializer(task).data
    return {"error": serializer.errors["title"][0]}
