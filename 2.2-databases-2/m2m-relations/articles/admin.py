from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if not form.cleaned_data:
                continue
            if form.cleaned_data['is_main']:
                count += 1
            if count > 1:
                raise ValidationError('Основной раздел может быть только один!')
        if count == 0:
            raise ValidationError('Укажите основной раздел:')
        return super().clean()  # вызываем базовый код переопределяемого метода

class ScopeInline(admin.TabularInline):
    model = Scope


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    formset = ScopeInlineFormset

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]