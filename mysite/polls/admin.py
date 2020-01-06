from django.contrib import admin

from .models import Question, Choice

# register a model so that it will appear on the admin side
# admin.site.register(Question)

# para mabago ang admin, pag arog kaini maiinot na ang pub date kaysa sa question text
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}), 
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]

    # kung anong data ang maluwas sa admin
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # panglaag sa right side kung muya mo may filter (filter by)
    list_filter = ['pub_date']
    # pang dagdag ki search fields
    search_fields = ['question_text']
    # pang limit ki pagination; default to 100
    list_per_page = 2

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)