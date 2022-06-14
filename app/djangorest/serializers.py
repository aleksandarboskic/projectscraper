from rest_framework import serializers
from djangorest.models import Article

'''
    Default serializer class, all the fields are included
'''

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"