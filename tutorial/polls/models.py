from django.db import models

class Article(models.Model):
    article_title = models.CharField('название статьи', max_length=255)
    article_text = models.TextField('текст')
    pub_date = models.DateTimeField('дата публикации')

    def __str__(self):
        return self.article_title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    auth_name = models.CharField('автор', max_length=50)
    comment_text = models.CharField('коментарий', max_length=200)

    def __str__(self):
        return self.auth_name

