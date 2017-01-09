from django.conf.urls import patterns, url

from user_bizz import views

urlpatterns = patterns('',
  url(r'^$', views.book_list, name='book_list'),
  url(r'^new$', views.book_create, name='book_new'),
  url(r'^edit/(?P<pk>\d+)$', views.book_update, name='book_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.book_delete, name='book_delete'),  
  url(r'^export/csv/$', views.export_users_csv, name='export_users_csv'),
)