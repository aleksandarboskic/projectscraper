from rest_framework.pagination import PageNumberPagination

'''
    Custom pagination class with default parameters
'''

class CustomNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page'
