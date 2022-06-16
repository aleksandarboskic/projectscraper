from datetime import datetime
from django.test import TestCase
from djangorest import models
from django.utils import timezone
  
class ModelTest(TestCase):
      def test_tag_model_str(self):
        article = models.Article.objects.create(
            symbol_name = "TEST",
            symbol_item_id = 1,
            symbol_item_guid = "{aaaaa-bbbbb-ccccc-ddddd-eeeee}",
            symbol_item_title = "This is test",
            symbol_item_pubdate = datetime.now(tz=timezone.utc),
            symbol_item_link = "https://www.google.com",
            symbol_item_description = "This is test scenario for testing data model.",
        )
  
        self.assertEqual(str(article), article.symbol_item_title)
