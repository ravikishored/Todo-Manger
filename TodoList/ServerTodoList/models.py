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

class Comments(models.Model):
    
    commentId = models.AutoField(primary_key=True, db_column='CommentId')
    todoId = models.ForeignKey(TodoList, db_column='taskId')
    commets = models.TextField(db_column='comments')
    
    def __unicode__(self):
        return u'%s %s' % (self.todoId,self.commets)
    
admin.site.register(TodoList)
admin.site.register(Comments)
