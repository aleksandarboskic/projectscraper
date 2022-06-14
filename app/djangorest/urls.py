from django.urls import path
from djangorest.views import ArticleItemsView, ArticleItemView

'''
    Default URL patterns for REST API.
'''

urlpatterns = [
    path('articles/', ArticleItemsView.as_view()),
    path('articles/<int:id>', ArticleItemView.as_view()),
]