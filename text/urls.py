from django.conf.urls import url

from .views import textListView, textDetailView 
urlpatterns = [
    url(r'^$',textListView.as_view()),
	url(r'^(?P<pk>[0-9]+)$', textDetailView.as_view()),
]	
