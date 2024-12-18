from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_400_BAD_REQUEST)
from rest_framework.views import APIView

from .models import Task
from .utilities.test_helpers import create_new_task, fetch_all_tasks


class TasksView(APIView):
    model = "task_views"

    def get(self, request):
        data = fetch_all_tasks(Task)
        if "error" in data:
            return Response(data=data["error"], status=HTTP_200_OK)
        return Response(data=data, status=HTTP_200_OK)

    def post(self, request):
        data = create_new_task(Task, request.data)
        if "error" in data:
            data = {"error": data["error"]}
            return Response(data=data["error"], status=HTTP_400_BAD_REQUEST)
        return Response(data=data, status=HTTP_201_CREATED)
