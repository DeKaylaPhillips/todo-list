from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255, null=False, verbose_name="Task Description")
    completed = models.BooleanField(default=False, verbose_name="Task Status")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "tasks"