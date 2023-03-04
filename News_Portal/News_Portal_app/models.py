from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse


class Author(models.Model):
    auth = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rate = models.IntegerField(default = 0)

    def update_rating(self):
        rating_of_post_by_author = self.post_set.all().aggregate(post_rating=Sum('post_rating'))['post_rating'] * 3
        rating_of_comments_by_author = self.auth.comment_set.all().aggregate(com_rating=Sum('com_rating'))['com_rating']
        rating_of_comments_to_author = Comment.objects.filter(post_com_id=self.id).aggregate(Sum('com_rating'))['com_rating__sum']
        self.author_rate = rating_of_post_by_author + rating_of_comments_by_author + rating_of_comments_to_author
        self.save()
        return self.author_rate


class Category(models.Model):
    sport = 'SP'
    politico = 'PO'
    education = 'ED'
    society = 'SO'
    technologies = 'TE'
    cat_field = [(sport, 'Cпорт'),
                 (politico, 'Политика'),
                 (education, 'Образование'),
                 (society, 'Общество'),
                 (technologies, 'Технологии')]

    cat_name = models.CharField(max_length=2, choices=cat_field, unique=True)
    subscribers = models.ManyToManyField(User, blank=True, null=True, related_name='categories')

class Post(models.Model):
    article = 'AR'
    news = 'NE'
    cat_ar_ne = [(article, 'статья'),
                 (news, 'новость')]

    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    _type = models.CharField(max_length=2, choices=cat_ar_ne)
    time_in = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through='PostCategory')
    heading = models.CharField(max_length=255)
    text = models.TextField()
    post_rating = models.IntegerField(default=0)

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
            self.post_rating -= 1
            self.save()

    def preview(self):
        return f'{self.text[0:124]}...'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.heading.title()}: {self.text[:20]}'

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

class Comment(models.Model):
    post_com = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    com_text = models.TextField()
    com_datetime = models.DateTimeField(auto_now_add=True)
    com_rating = models.IntegerField(default=0)

    def like(self):
        self.com_rating += 1
        self.save()

    def dislike(self):
        self.com_rating -= 1
        self.save()



