from django.conf.urls import url, include
from primer import views

urlpatterns = [

	
    url(r'^index/$', views.index, name='index'),

    url(r'^index2/$', views.index2, name='index2'),

    url(r'^add_list/$', views.add_list, name='add_list'),

    url(r'^thanks/$', views.thanks, name='thanks'),

    url(r'^zayavki/$', views.test, name='zayavki'),

    url(r'^login/$', views.login, name='login'),

    url(r'^comments/$', views.comments, name='comments'),

    url(r'^export/csv/$', views.export_users_csv, name='export_users_csv'),

    url(r'^export/csv/сomps$', views.export_comps_csv, name='export_comps_csv'),


    url(r'^computers_and_other/$', views.computers_and_other, name='computers_and_other'),

    ]