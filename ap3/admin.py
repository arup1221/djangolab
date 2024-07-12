from django.contrib import admin
from ap3.models import Course, Student
# admin.site.register(Student)
admin.site.register(Course)
@admin.register(Student)


class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_name", "student_usn", "student_sem")
    ordering = ("student_name",)
    search_fields = ("student_name",)
