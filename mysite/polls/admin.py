from django.contrib import admin
from .models import Question, Choice

# customizing admin Question form

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):

    # all question list modifications

    fieldsets = [
        (None, {'fields': ['text']}),
        ('Date Information', {'fields': ['pub_date']})
    ]

    inlines = [ChoiceInLine]

    list_filter = ['pub_date']

    search_fields = ['question_text']
    
    # change question modifications
    list_display = ('text', 'pub_date', 'was_published_recently')


admin.site.register(Question, QuestionAdmin)
