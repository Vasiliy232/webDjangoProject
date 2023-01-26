from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from .models import Course, Instructor
from .forms import CourseForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['instructors'] = self.object.instructor_set.all().values_list('instructor__username', flat=True)
        context['courses'] = self.object.category.course_set.all()
        return context


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


class InstructorListView(PageTitleMixin, ListView):
    model = Instructor
    page_title = 'Instructors'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['instructors'] = Instructor.objects.values_list('instructor__username', 'pk')
        return context


class InstructorDetailView(PageTitleMixin, DetailView):
    model = Instructor
    page_title = 'Instructor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = self.object.course.all()
        context['students'] = self.object.student.all().select_related('student')
        return context


# class ContactsTemplateView(PageTitleMixin, TemplateView):
#     page_title = 'Contacts'
#     template_name = 'education/contacts.html'
