from django.db import models
from django.contrib import admin

class TodoList(models.Model):
    
    taskId = models.AutoField(primary_key=True, db_column='taskId')
    title = models.CharField(max_length=100,db_column='title')
    description = models.TextField(db_column='description')
    startDate = models.DateTimeField(null=True,auto_now_add=True,db_column='StartDate')
    endDate = models.CharField(max_length=100,db_column='EndDate')
    completed = models.BooleanField(db_column='completed')
    
    def __unicode__(self):
        return self.title


    
admin.site.register(TodoList)

