from django.db import models, IntegrityError

'''
   Simple model of published article. This is classic use of Django ORM and database object generator.
   Method save is overriden to pass IntegrityError. Item GUID is unique for any article in RSS feed, so
   we needed to make unique constraint on GUID field. Every time when scrap_all task is executed, it can
   have collect articles that are existing in database. If IntegrityError occurs, we just ignore that error.
'''

class Article(models.Model):
    symbol_name = models.CharField(max_length=6, db_index=True)
    symbol_item_id = models.BigAutoField(primary_key=True)
    symbol_item_guid = models.CharField(unique=True, max_length=128)
    symbol_item_title = models.TextField(max_length=1000)
    symbol_item_pubdate = models.DateTimeField() 
    symbol_item_link = models.URLField(max_length=400) 
    symbol_item_description = models.TextField(max_length=4000)
    symbol_timestamp =  models.DateTimeField(auto_now_add=True, blank=False) 
    
    def __str__(self):
        return self.symbol_item_title
    
    def save(self, *args, **kwargs):
        try:
            super(Article, self).save(*args, **kwargs)
        except IntegrityError:
            pass
        except Exception as ex:
            raise ex
