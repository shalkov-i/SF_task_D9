from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, PostDetail, NewsCreate, ArticleCreate, ArticleUpdate, PostDelete


urlpatterns = [
   path('', PostsList.as_view(), name='post_list'),
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('create/', ArticleCreate.as_view(), name='create_article'),
   path('<int:pk>/edit/', ArticleUpdate.as_view(), name='edit_article'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]