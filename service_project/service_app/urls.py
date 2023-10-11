from django.urls import path
from rest_framework.routers import Route
from rest_framework import routers
from . import views

app_name = 'service_app'  

urlpatterns = [
    
    path('students/create/', views.StudentCreateUpdateDeleteView.as_view(), name='student-create'),

    path('students/create/', views.StudentCreateUpdateDeleteView.as_view(), name='student-create'),
    path('students/<int:pk>/update/', views.StudentCreateUpdateDeleteView.as_view(), name='student-update'),
    path('students/<int:pk>/delete/', views.StudentCreateUpdateDeleteView.as_view(), name='student-delete'),

 
    path('professors/create/', views.ProfessorCreateUpdateDeleteView.as_view(), name='professor-create'),

    path('professors/create/', views.ProfessorCreateUpdateDeleteView.as_view(), name='professor-create'),
    path('professors/<int:pk>/update/', views.ProfessorCreateUpdateDeleteView.as_view(), name='professor-update'),
    path('professors/<int:pk>/delete/', views.ProfessorCreateUpdateDeleteView.as_view(), name='professor-delete'),

    
    path('departments/create/', views.DepartmentCreateUpdateDeleteView.as_view(), name='department-create'),

    path('departments/create/', views.DepartmentCreateUpdateDeleteView.as_view(), name='department-create'),
    path('departments/<int:pk>/update/', views.DepartmentCreateUpdateDeleteView.as_view(), name='department-update'),
    path('departments/<int:pk>/delete/', views.DepartmentCreateUpdateDeleteView.as_view(), name='department-delete'),

    
    path('courses/create/', views.CourseCreateUpdateDeleteView.as_view(), name='course-create'),

    path('courses/create/', views.CourseCreateUpdateDeleteView.as_view(), name='course-create'),
    path('courses/<int:pk>/update/', views.CourseCreateUpdateDeleteView.as_view(), name='course-update'),
    path('courses/<int:pk>/delete/', views.CourseCreateUpdateDeleteView.as_view(), name='course-delete'),

    
    path('consultations/create/', views.ConsultationCreateUpdateDeleteView.as_view(), name='consultation-create'),

    path('consultations/create/', views.ConsultationCreateUpdateDeleteView.as_view(), name='consultation-create'),
    path('consultations/<int:pk>/update/', views.ConsultationCreateUpdateDeleteView.as_view(), name='consultation-update'),
    path('consultations/<int:pk>/delete/', views.ConsultationCreateUpdateDeleteView.as_view(), name='consultation-delete'),

    path('reports/create/', views.ReportCreateUpdateDeleteView.as_view(), name='report-create'),
    path('reports/<int:pk>/update/', views.ReportCreateUpdateDeleteView.as_view(), name='report-update'),
    path('reports/<int:pk>/delete/', views.ReportCreateUpdateDeleteView.as_view(), name='report-delete'),
    path('consultation_bookings/create/', views.ConsultationBookingCreateUpdateDeleteView.as_view(), name='consultation-booking-create'),
    path('consultation_bookings/<int:pk>/update/', views.ConsultationBookingCreateUpdateDeleteView.as_view(), name='consultation-booking-update'),
    path('consultation_bookings/<int:pk>/delete/', views.ConsultationBookingCreateUpdateDeleteView.as_view(), name='consultation-booking-delete'),

    # Маршруты для создания, обновления и удаления объявления
    path('announcements/create/', views.AnnouncementCreateUpdateDeleteView.as_view(), name='announcement-create'),
    path('announcements/<int:pk>/update/', views.AnnouncementCreateUpdateDeleteView.as_view(), name='announcement-update'),
    path('announcements/<int:pk>/delete/', views.AnnouncementCreateUpdateDeleteView.as_view(), name='announcement-delete'),

    # Маршруты для создания, обновления и удаления задания
    path('assignments/create/', views.AssignmentCreateUpdateDeleteView.as_view(), name='assignment-create'),
    path('assignments/<int:pk>/update/', views.AssignmentCreateUpdateDeleteView.as_view(), name='assignment-update'),
    path('assignments/<int:pk>/delete/', views.AssignmentCreateUpdateDeleteView.as_view(), name='assignment-delete'),

   



]