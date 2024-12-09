from django.urls import path, register_converter

from .converter import IntOrStrConverter
from .views import AllTasks

register_converter(converter=IntOrStrConverter, type_name="int_or_str")

urlpatterns = [
    # https://127.000.000/api/v1/zendo/
    path(route="", view=AllTasks.as_view(), name="all_tasks"),
]
