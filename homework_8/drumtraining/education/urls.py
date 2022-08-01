from django.urls import path
import education.views as education


app_name = 'education'

urlpatterns = [
    path('', education.CourseListView.as_view(), name='courses_list'),
    path('course/<pk>', education.CourseDetailView.as_view(), name='course_detail')
]
