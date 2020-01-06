from django.contrib import admin

from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'questions_text']

    list_display = ('questions_text', 'pub_date', 'was_published_recently')

    # fieldsets = [
    #     (None, {'fields': ['questions_text']}),
    #     ('Date Information', {'fields':['pub_date']}),
    # ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['questions_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)