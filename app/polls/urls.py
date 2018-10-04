from django.urls import path, include

# from . import views
from .views import cbv, fbv as views

app_name = 'polls'

urlpatterns_cbv = [
    path('', cbv.IndexView.as_view(), name='index'),
]
urlpatterns = [
    # /polls/
    path('', views.index, name='index'),
    # r'^(?P<question_id>\d+)/$'
    path('<int:question_id>/', views.detail, name='detail'),
    # r'^(?P<question_id>\d+)/results/$'
    path('<int:question_id>/results/', views.results, name='results'),
    # r'^(?P<question_id>\d+)/vote/$'
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # /polls/cbv/로 시작하는 URL요청은
    # 위의 urlpatterns_cbv리스트 내의 내용에서 처리
    path('cbv/', include(urlpatterns_cbv)),
]
