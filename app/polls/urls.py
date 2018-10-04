from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # /polls/
    path('', views.index, name='index'),
    # r'^(?P<question_id>\d+)/$'
    path('<int:question_id>/', views.detail, name='detail'),
    # r'^(?P<question_id>\d+)/results/$'
    path('<int:question_id>/results/', views.results, name='results'),
    # r'^(?P<question_id>\d+)/vote/$'
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
