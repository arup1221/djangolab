
from django.contrib import admin
from django.urls import path
from ap1.views import current_dateandtime, four_hours_ahead, four_hours_before
from ap2.views import showList, hello, home, aboutus, contactus
from ap3.views import course_search,reg,add_project
from ap3.views import StudentListView,StudentDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello),
    path('date/', current_dateandtime),
    path('foura/', four_hours_ahead),
    path('fourb/', four_hours_before),
    path('showlist/', showList),
    path('home/', home),
    path('aboutus/', aboutus),
    path('contactus/', contactus),
    path('coursesearch/',course_search ),
    path('reg/', reg),
    path('add_project/',add_project),
    path('student_list/',StudentListView.as_view()),
    path('student_detail/<int:pk>',StudentDetailView.as_view() )
]


admin.site.site_header = "My Site Header"
admin.site.site_title = "My Site Title"
admin.site.index_title = "My Site Index"