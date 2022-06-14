from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .pagination import CustomNumberPagination
from rest_framework import status
from djangorest.serializers import ArticleSerializer
from djangorest.models import Article

'''
    Views implementation. Single and multiple objects.
'''


class ArticleItemsView(APIView, PageNumberPagination):
    serializer_class = ArticleSerializer
    pagination_class = CustomNumberPagination

    def get(self, request):
        queryset = Article.objects.all()
        #queryset = self.get_queryset()
        page = self.request.query_params.get('page')
        if page is not None:
            paginated_queryset = self.paginate_queryset(queryset, request)
            serializer = self.serializer_class(paginated_queryset, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)        

class ArticleItemView(APIView):
    def get(self, request, id=None):
        if id:
            item = Article.objects.get(symbol_item_id=id)
            serializer = ArticleSerializer(item)
            return Response(data = serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data = "Invalid ID", status=status.HTTP_404_NOT_FOUND)
    '''
        This is just a sample for delete single item from database.
    '''
    def delete(self, request, id=None):
        if id:
            item = Article.objects.get(symbol_item_id=id)
            item.delete()
            return Response(data = "Item Deleted", status=status.HTTP_200_OK)
