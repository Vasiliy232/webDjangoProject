from django.urls import path
import education.views as education


app_name = 'education'

urlpatterns = [
    path('course/create', education.CourseCreateView.as_view(), name='course_form'),
    path('course/update/<pk>', education.CourseUpdateView.as_view(), name='course_update_form'),
    path('course/delete/<pk>', education.CourseDeleteView.as_view(), name='course_confirm_delete'),
    path('', education.CourseListView.as_view(), name='courses_list'),
    path('course/<pk>', education.CourseDetailView.as_view(), name='course_detail'),
]
