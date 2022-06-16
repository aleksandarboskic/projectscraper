from django.test import TestCase
from django.utils import timezone
from datetime import datetime
from djangorest.serializers import ArticleSerializer


class SerializerTest(TestCase):
    def test_valid_article_serializer(self):
        valid_serializer_data = {
            "symbol_name": "TEST",
            "symbol_item_id": 5,
            "symbol_item_guid": "{aaaaa-bbbbb-ccccc-ddddd-eeeee-fffff}",
            "symbol_item_title": "This is a test",
            "symbol_item_pubdate": datetime.now(tz=timezone.utc),
            "symbol_item_link": "https://www.google.com",
            "symbol_item_description": "This is a test sample for serializer data.",
            "symbol_timestamp": datetime.now(tz=timezone.utc),
        }
        serializer = ArticleSerializer(data=valid_serializer_data)
        serializer.is_valid(raise_exception=True)
        self.assertEqual(serializer.data.get("symbol_item_title", None), "This is a test")
