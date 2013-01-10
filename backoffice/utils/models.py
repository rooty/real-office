from django.db import models


class QuerySetManager(models.Manager):

    def __init__(self, queryset_class, *args, **kwargs):
        self.queryset_class = queryset_class
        super(QuerySetManager, self).__init__(*args, **kwargs)

    def get_query_set(self):
        return self.queryset_class(self.model, using=self._db)

    def __getattr__(self, key):
        return getattr(self.get_query_set(), key)
