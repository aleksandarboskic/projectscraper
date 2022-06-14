from rest_framework import serializers
from djangorest.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["symbol_name", "symbol_item_guid", "symbol_item_title", "symbol_item_pubdate", "symbol_item_link", "symbol_item_description", "symbol_timestamp"]