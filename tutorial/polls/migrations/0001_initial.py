# Generated by Django 3.2 on 2021-04-19 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=255, verbose_name='название статьи')),
                ('article_text', models.TextField(verbose_name='текст')),
                ('pub_date', models.DateTimeField(verbose_name='дата публикации')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_name', models.CharField(max_length=50, verbose_name='автор')),
                ('comment_text', models.CharField(max_length=200, verbose_name='коментарий')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.article')),
            ],
        ),
    ]
