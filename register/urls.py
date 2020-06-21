"""register URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from register import views
from django.conf.urls import url



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^home/$', views.home),
    url(r'^$', views.home),
    url(r'^banished/$', views.banished),
    url(r'^checking/$', views.checking),
    url(r'^contact/$', views.contact),
    url(r'^court_proceedings/$', views.court_proceedings),
    url(r'^documents/$', views.documents),
    url(r'^question/$', views.question),
    url(r'^address/$', views.address),
    url(r'^work_material/$', views.work_material),
    url(r'^work_material_1/$', views.work_material_1),
    url(r'^work_material_2/$', views.work_material_2),
    url(r'^work_material_3/$', views.work_material_3),
    url(r'^work_material_6/$', views.work_material_6),
    url(r'^data/$', views.data_about_checking),
    url(r'^public_council/$', views.public_council),
    url(r'^public_council_2/$', views.public_council_2),
    url(r'^public_council_3/$', views.public_council_3),
    url(r'^public_council_4/$', views.public_council_4),
    url(r'^public_council_5/$', views.public_council_5),
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
    url(r'^admin_checking/$', views.admin_checking),
    url(r'^admin_checking/delete/(?P<id>\w+)$', views.admin_checking_delete),
    url(r'^admin_checking/update/(?P<id>\w+)$', views.admin_checking_update),
    url(r'^admin_checking/move/(?P<id>\w+)$', views.admin_checking_move),
    url(r'^admin_checking/add/$', views.admin_checking_add),
    url(r'^admin_register/$', views.admin_register),
    url(r'^admin_register/delete/(?P<id>\w+)$', views.admin_register_delete),
    url(r'^admin_register/update/(?P<id>\w+)$', views.admin_register_update),
    url(r'^admin_register/add/$', views.admin_register_add),
    url(r'^admin_users/$', views.admin_users),
    url(r'^admin_users/admin_deadmin/(?P<username>\w+)$', views.admin_users_admin_deadmin),
    url(r'^admin_users/ban_deban/(?P<username>\w+)$', views.admin_users_ban_deban),
    url(r'^admin_users/delete/(?P<username>\w+)$', views.admin_users_delete),
    url(r'^logout/$', views.logout)
]



