from django.urls import path
from djangorest.views import ArticleItemsView

urlpatterns = [
    path('articles/', ArticleItemsView.as_view()),
    path('articles/<int:id>', ArticleItemsView.as_view()),
]