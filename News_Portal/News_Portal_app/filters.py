from django.forms import DateInput
from django_filters import FilterSet, DateFilter
from .models import Post, Author


class PostFilter(FilterSet):
    date = DateFilter(field_name='time_in', widget=DateInput(attrs={'type': 'date'}), label='Поиск по дате',
                      lookup_expr='date__gte')
    # author = ModelChoiceFilter(field_name='author__auth__username',
    #     queryset=Author.objects.all().values('auth__username'),
    #     label='Author'
    # )

    class Meta:
        model = Post
        fields = {
            'heading': ['icontains'],
            'author__auth__username': ['iexact'],
            #'time_in': ['gt'],
        }