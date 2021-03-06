from haystack import indexes
from bambu_blog.models import Post
from datetime import datetime

class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document = True, use_template = True)
    author = indexes.CharField(model_attr = 'author')
    date = indexes.DateTimeField(model_attr = 'date')
    
    def get_model(self):
        return Post
    
    def index_queryset(self, using = None):
        return super(PostIndex, self).index_queryset().live()