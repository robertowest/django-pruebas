from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class Comment(models.Model):
    comm = models.CharField(max_length=50)
    content_type = models.ForeignKey(ContentType, models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Article(models.Model):
    content = models.CharField(max_length=100)
    comments = GenericRelation(Comment)


class Post(models.Model):
    content = models.CharField(max_length=100)
    comments = GenericRelation(Comment)


# To relate a Comment to an Article instance:
# >>> art = Article.objects.get(id=1)
# >>> c = Comment(content_object=art, comm='asdf')
# >>> c.save()
# >>> c.content_object
# <Article: article1>
#
# To relate a Comment to a Post instance:
# >>> pos= Post.objects.get(id=1)
# >>> c= Comment(content_object=pos, comm='new comment')
# >>> c.save()
# >>> c.content_object
# <Post: post1>
#
# >>> art.comments.all()
# <QuerySet [<Comment: asdf>, <Comment: test>]>
#
# >>> pos.comments.all()
# <QuerySet [<Comment: new_comment>, <Comment: test2>]>

