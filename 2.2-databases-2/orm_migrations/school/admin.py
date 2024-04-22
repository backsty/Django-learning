from django.contrib import admin

from .models import Student, Teacher


class StudentInLine(admin.TabularInline):
    model = Student
    extra = 1

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_dislpay = ('name', 'group')
    list_filter = ('group',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_dislpay = ('name', 'subject')
    list_filter = ('subject',)
