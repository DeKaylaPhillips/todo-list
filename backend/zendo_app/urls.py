from django.urls import path, register_converter

from .converter import IntOrStrConverter
from .views import TasksView

register_converter(converter=IntOrStrConverter, type_name="int_or_str")

urlpatterns = [
    # https://127.000.000/api/v1/zendo/
    path(route="tasks/", view=TasksView.as_view(), name="task_views"),
]
