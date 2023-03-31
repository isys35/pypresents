>>> from django.forms import BaseFormSet, formset_factory
>>> from myapp.forms import ArticleForm
>>> class BaseArticleFormSet(BaseFormSet):
...     def get_ordering_widget(self):
...         return HiddenInput(attrs={'class': 'ordering'})

>>> ArticleFormSet = formset_factory(ArticleForm, formset=BaseArticleFormSet, can_order=True)