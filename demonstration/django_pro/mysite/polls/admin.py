from django.contrib import admin
from .models import Question,Choice

admin.site.site_header = "Django Boomcamp"
admin.site.site_title = "Django Boomcamp Area"
admin.site.index_title = "Welcome Django Boomcamp Admin Area"

class ChoiceInline(admin.TabularInline):
    
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['question_text']
    list_filter = ['pub_date']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [(None,{'fields':['question_text']}),
    ('Date Information',{'fields':['pub_date'],'classes':['collapse']}), ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
