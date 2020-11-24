from django.db import models

class User(models.Model):
    name     = models.CharField(max_length = 32, null = True, blank = True)
    email    = models.CharField(max_length = 64)
    password = models.CharField(max_length = 64)

    class Meta:
        db_table = 'users'

class Post(models.Model):
    title   = models.CharField(max_length = 32)
    content = models.CharField(max_length = 512)
    image   = models.CharField(max_length = 1024, null = True, blank = True)
    user    = models.ForeignKey('user', on_delete = models.CASCADE) # related_name = 'writer'

    class Meta:
        db_table = 'posts'