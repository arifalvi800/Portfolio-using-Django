from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header="Arif Alvi"
admin.site.site_title="Arif Alvi"
admin.site.index_title="Welcome to Arif Alvi Portfolio Panel"

urlpatterns = [
    path('',views.index,name='index')
]
