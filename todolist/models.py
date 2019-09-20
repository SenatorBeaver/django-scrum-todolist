from django.db import models
from django.urls import reverse


class Label(models.Model):
    label_id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=100, unique=True)

    def __repr__(self):
        return f"Label({self.label_id}) text:'{self.text}'"

    def __str__(self):
        return self.__repr__()

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('todolist:project_details', kwargs={'pk':self.id})

    def __str__(self):
        return f"Project ID:{self.id} NAME:'{self.name}'. Description:'{self.description}'"

    def __repr__(self):
        return self.__str__()


class TodoItem(models.Model):
    text = models.CharField(unique=False, max_length=1024)
    label_id = models.ForeignKey(Label, on_delete=models.CASCADE, null=True)
    due_date = models.DateTimeField()
    PRIORITY_CHOICES = [
        (0, 'Najważeniejszy'),
        (1, 'Prawie najważniejszy'),
        (2, 'Wysoki'),
        (3, 'Normalny'),
        (4, 'Niski'),
    ]
    priority = models.PositiveSmallIntegerField(choices=PRIORITY_CHOICES, default=3)
    project = models.ForeignKey(Project, related_name='project_todoitems', on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse('todolist:todoitem_detail', kwargs={'pk':self.id})

    def __repr__(self):
        return f"TodoItem({self.id}) '{self.text}'"

    def __str__(self):
        return self.__repr__()


