from django.conf.urls import patterns, include, url
from TodoList import settings


urlpatterns = patterns('',
    
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),    
     url(r'^', include('ServerTodoList.urls')),
    
)
