# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Message, MessageFolder, Task, Project, TaskState, OfficeContactInfo
from office.models import ObjectCost, ObjectPayment, CostType, PaymentType


class TaskStateAdmin(admin.ModelAdmin):
    pass

class OfficeContactInfoAdmin(admin.ModelAdmin):
    pass

class MessageAdmin(admin.ModelAdmin):
    search_fields = ["subject", "user_from","user_to","delivery","readed"]
    display_fields = ["subject", "created", "comment_count", ]

class TaskInline(admin.StackedInline):
    model = Task
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'owner',
        'get_tasks_worker',
        'date_start',
        'date_end',
        )
    inlines = [TaskInline, ]

class PaymentTypeAdmin(admin.ModelAdmin):
    pass

class CostTypeAdmin(admin.ModelAdmin):
    pass

class ObjectPaymentAdmin(admin.ModelAdmin):
    pass

class ObjectCostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Message, MessageAdmin)
admin.site.register(MessageFolder)
admin.site.register(Project, ProjectAdmin)
admin.site.register(TaskState, TaskStateAdmin)
admin.site.register(OfficeContactInfo, OfficeContactInfoAdmin)
admin.site.register(PaymentType,PaymentTypeAdmin)
admin.site.register(CostType,CostTypeAdmin)
admin.site.register(ObjectPayment,ObjectPaymentAdmin)
admin.site.register(ObjectCost,ObjectCostAdmin)
