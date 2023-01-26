from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
import education.views as education


app_name = 'education'

urlpatterns = [
    path('course/create', education.CourseCreateView.as_view(), name='course_form'),
    path('course/update/<pk>', education.CourseUpdateView.as_view(), name='course_update_form'),
    path('course/delete/<pk>', education.CourseDeleteView.as_view(), name='course_confirm_delete'),
    path('', education.CourseListView.as_view(), name='courses_list'),
    path('course/<pk>', education.CourseDetailView.as_view(), name='course_detail'),
    path('instructors/', education.InstructorListView.as_view(), name='instructor_list'),
    path('instructor/<pk>', education.InstructorDetailView.as_view(), name='instructor_detail'),
    # path('contacts/', education.ContactsTemplateView.as_view(), name='contacts')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
