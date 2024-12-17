from ..models import Task


def create_new_task(validated_data):
    return Task.objects.create(**validated_data)
