from django.contrib import admin
from django.urls import path
from blog.views import *


urlpatterns = [
    path('', index, name='index'),
    path('blog2/', index2, name='index'),
    path('blog3/', index3, name='index'),
    path('categ/<int:catid>/', categ, name='categ')

]
