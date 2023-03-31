>>> from django.forms import BaseFormSet, formset_factory
>>> from myapp.forms import ArticleForm
>>> class BaseArticleFormSet(BaseFormSet):
...     ordering_widget = HiddenInput

>>> ArticleFormSet = formset_factory(ArticleForm, formset=BaseArticleFormSet, can_order=True)