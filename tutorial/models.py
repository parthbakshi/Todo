from django.db import models

# Create your models here.

class Todolist(models.Model):
    """
    Todolist class
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class items(models.Model):
    todolist = models.ForeignKey(Todolist, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    complete =  models.BooleanField()
    due_date = models.DateField()

    def __str__(self):
        return self.text







