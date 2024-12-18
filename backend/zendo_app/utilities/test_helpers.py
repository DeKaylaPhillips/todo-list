from ..serializers import TaskSerializer


def get_all_tasks(Task):
    errors = {"no_tasks_found_error": "No tasks found in list."}
    all_tasks = Task.objects.all().order_by("id")
    if all_tasks.count() == 0:
        data = errors["no_tasks_found_error"]
        return data
    data = TaskSerializer(all_tasks, many=True).data
    return data


def create_new_task(Task, request_data):
    serializer = TaskSerializer(data=request_data)
    if serializer.is_valid():
        validated_data = serializer.validated_data
        task = Task.objects.create(**validated_data)
        data = TaskSerializer(task).data
        return data
    data = {"error": serializer.errors["title"][0]}
    return data
