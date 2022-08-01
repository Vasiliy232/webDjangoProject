from django.shortcuts import render
from django.views.generic import ListView, DetailView
from education.models import Course


class PageTitleMixin:
    page_title = None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['page_title'] = self.page_title
        return context


class CourseListView(PageTitleMixin, ListView):
    model = Course
    page_title = 'Courses'


class CourseDetailView(PageTitleMixin, DetailView):
    model = Course
    page_title = 'Course'
