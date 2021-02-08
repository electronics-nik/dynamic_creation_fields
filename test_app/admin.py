from django.contrib import admin

from .models import AdvUser
from .models import Question
from .models import Answer


class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_activated', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')

    fields = (
        ('username', 'email'),
        ('first_name', 'last_name'),
        ('send_messages', 'is_active', 'is_activated'),
        ('is_staff', 'is_superuser'),
        'groups', 'user_permissions',
        ('last_login', 'date_joined')
    )
    readonly_fields = ('last_login', 'date_joined')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'author', 'created', 'is_active')
    fields = (
        'author',
        'question',
        'image',
        'is_active',
    )


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'correct', 'created', 'is_active')
    fields = (
        ('question', 'author'),
        'answer',
        'correct',
        'is_active',
    )


admin.site.register(AdvUser, AdvUserAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
