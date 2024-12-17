from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_400_BAD_REQUEST)
from rest_framework.views import APIView

from .models import Task
from .serializers import TaskSerializer
from .utilities.test_helpers import create_new_task


class TasksView(APIView):
    model = "task_views"

    def get(self, request):
        all_tasks = Task.objects.all().order_by("id")
        response = TaskSerializer(all_tasks, many=True)
        return Response(data=response.data, status=HTTP_200_OK)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            new_task = create_new_task(serializer.validated_data)
            data = TaskSerializer(new_task).data
            return Response(data=data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
