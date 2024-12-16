from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from .models import Task
from .serializers import TaskSerializer


class AllTasks(APIView):
    model = "all_tasks"

    def get(self, request):
        all_tasks = Task.objects.all().order_by("id")
        response = TaskSerializer(all_tasks, many=True)
        return Response(data=response.data, status=HTTP_200_OK)
