from django.forms import ModelForm
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from education.models import Course


class PageTitleMixin:
    page_title = None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['page_title'] = self.page_title
        return context


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = [
            'name',
            'started_at',
            'duration',
            'price',
            'description'
        ]


class CourseListView(PageTitleMixin, ListView):
    model = Course
    page_title = 'Courses'


class CourseDetailView(PageTitleMixin, DetailView):
    model = Course
    page_title = 'Course'


class CourseCreateView(PageTitleMixin, CreateView):
    model = Course
    form_class = CourseForm
    page_title = 'Create course'

    def get_success_url(self):
        return reverse('education:course_detail', kwargs={'pk': self.object.pk})


class CourseUpdateView(PageTitleMixin, UpdateView):
    model = Course
    form_class = CourseForm
    page_title = 'Update course'

    def get_success_url(self):
        return reverse('education:course_detail', kwargs={'pk': self.object.pk})


class CourseDeleteView(PageTitleMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('education:courses_list')
