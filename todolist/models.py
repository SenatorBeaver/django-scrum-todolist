import dateutil.relativedelta
from django.db import models
from django.urls import reverse
from django.utils import timezone

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
        return f"{self.name}"

    def __repr__(self):
        return f"{self.id}"

class PeriodType():
    NONE = 0
    EVERY_DAY = 1
    EVERY_WEEK = 2
    EVERY_MONTH = 3
    EVERY_YEAR = 4

    CHOICES = [
        (NONE, 'Brak'),
        (EVERY_DAY, 'Co dzień'),
        (EVERY_WEEK, 'Co tydzień'),
        (EVERY_MONTH, 'Co miesiąc'),
        (EVERY_YEAR, 'Co rok'),
    ]


class TodoItem(models.Model):
    text = models.CharField(unique=False, max_length=1024)
    label_id = models.ForeignKey(Label, on_delete=models.CASCADE, null=True)
    due_date = models.DateField(null=True)
    due_time = models.TimeField(null=True, blank=True)
    period_value = models.PositiveSmallIntegerField(null=False, default=0)
    period_type = models.PositiveSmallIntegerField(null=False, default=0, choices=PeriodType.CHOICES)

    PRIORITY_CHOICES = [
        (0, 'Najważeniejszy'),
        (1, 'Prawie najważniejszy'),
        (2, 'Wysoki'),
        (3, 'Normalny'),
        (4, 'Niski'),
    ]

    priority = models.PositiveSmallIntegerField(choices=PRIORITY_CHOICES, default=3)
    project = models.ForeignKey(Project, related_name='project_todoitems', on_delete=models.CASCADE, null=True)
    done_date = models.DateTimeField(null=True)


    def done(self):
        if self.period_type == PeriodType.NONE:
            self.done_date = timezone.now()
            self.save()
        else:
            if timezone.now().date() > self.due_date:
                switcher = {
                    PeriodType.EVERY_DAY : 'days',
                    PeriodType.EVERY_WEEK: 'weeks',
                    PeriodType.EVERY_MONTH: 'months',
                    PeriodType.EVERY_YEAR: 'years',
                }
                kwargs = { switcher.get(self.period_type): self.period_value}
                self.due_date += dateutil.relativedelta.relativedelta(**kwargs)
                self.save()

    def get_absolute_url(self):
        return reverse('todolist:todoitem_detail', kwargs={'pk':self.id})

    def __repr__(self):
        return f"TodoItem({self.id}) '{self.text}'"

    def __str__(self):
        return self.__repr__()


