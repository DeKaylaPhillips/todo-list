from ..serializers import TaskSerializer


def fetch_all_tasks(Task):
    tasks = Task.objects.all().order_by("id")
    if not tasks.exists():
        return {"error": "No tasks found in list."}
    return TaskSerializer(tasks, many=True).data


def create_new_task(Task, request_data):
    serializer = TaskSerializer(data=request_data)
    if serializer.is_valid():
        validated_data = serializer.validated_data
        task = Task.objects.create(**validated_data)
        data = TaskSerializer(task).data
        return data
    data = {"error": serializer.errors["title"][0]}
    return data
