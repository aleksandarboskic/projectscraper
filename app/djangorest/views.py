from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from djangorest.serializers import ArticleSerializer
from djangorest.models import Article

class ArticleItemsView(APIView):
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data = serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Article.objects.get(symbol_item_id=id)
            serializer = ArticleSerializer(item)
            return Response(data = serializer.data, status=status.HTTP_200_OK)

        items = Article.objects.all()
        serializer = ArticleSerializer(items, many=True)
        return Response(data = serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        if id:
            item = Article.objects.get(id=id)
            item.delete()
            return Response(data = "Item Deleted", status=status.HTTP_200_OK)
