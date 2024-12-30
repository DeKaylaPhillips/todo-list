from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_400_BAD_REQUEST)
from rest_framework.views import APIView

from .models import Task
from .utilities.test_helpers import fetch_all_tasks, validate_and_create_a_task


class TasksView(APIView):
    model = "task_views"

    def get(self, request):
        data = fetch_all_tasks(Task)
        return self._handle_response(data, HTTP_200_OK)

    def post(self, request):
        data = validate_and_create_a_task(Task, request.data)
        return self._handle_response(data, HTTP_201_CREATED)

    def _handle_response(self, data, success_status):
        if "error" in data:
            if data.get("error") == "No tasks found in list.":
                return Response(data["error"], HTTP_200_OK)
            return Response(data["error"], HTTP_400_BAD_REQUEST)
        return Response(data, success_status)
