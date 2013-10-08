from django.conf.urls import patterns, include, url

urlpatterns = patterns('ServerTodoList.views',
	

	
        url(r'^create', 'createTodo', name='todo'),
        url(r'^done$', 'done', name='done'),
       

)
