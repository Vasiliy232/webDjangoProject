from django.contrib import admin
from education.models import (
    Instructor,
    Student,
    Course,
    Category
)


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = "instructor", "work", "bio_short", "registered_at"

    def bio_short(self, obj: Instructor):
        if len(obj.bio) < 40:
            return obj.bio
        return f"{obj.bio[:36]}..."


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = "student", "birthday", "gender", "level", "bio_short"

    def bio_short(self, obj: Student):
        if len(obj.bio) < 40:
            return obj.bio
        return f"{obj.bio[:36]}..."


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = "name", "started_at", "duration", "description_short", "price", "category"

    def description_short(self, obj: Course):
        if len(obj.description) < 40:
            return obj.description
        return f"{obj.description[:36]}..."


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "name", "get_course_count"

    # def get_course_count(self, obj: Category):
    #     obj.get_course_count()
    #     return obj.course_count
    #
    # get_course_count.short_description = "number of courses"