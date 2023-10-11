from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import *
from rest_framework import generics
from .models import Student, Professor, Department, Course, Consultation, Report, ConsultationBooking, Announcement, Assignment
from .serializers import (
    StudentSerializer, ProfessorSerializer, DepartmentSerializer, CourseSerializer,
    ConsultationSerializer, ReportSerializer, ConsultationBookingSerializer,
    AnnouncementSerializer, AssignmentSerializer
)

class StudentListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreateUpdateDeleteView(generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ProfessorListView(generics.ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class ProfessorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class ProfessorCreateUpdateDeleteView(generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer    

class DepartmentListView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
class DepartmentCreateUpdateDeleteView(generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer    

class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseCreateUpdateDeleteView(generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class ConsultationListView(generics.ListCreateAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

class ConsultationCreateUpdateDeleteView(generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

class ConsultationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

class ReportListView(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ReportCreateUpdateDeleteView(generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    
class ConsultationCreateView(generics.CreateAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

class ConsultationBookingListView(generics.ListCreateAPIView):
    queryset = ConsultationBooking.objects.all()
    serializer_class = ConsultationBookingSerializer
class ConsultationBookingCreateUpdateDeleteView(generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = ConsultationBooking.objects.all()
    serializer_class = ConsultationBookingSerializer    

class ConsultationBookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConsultationBooking.objects.all()
    serializer_class = ConsultationBookingSerializer

class AnnouncementListView(generics.ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    
class AnnouncementCreateUpdateDeleteView(generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

class AnnouncementDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

class AssignmentListView(generics.ListCreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class AssignmentCreateUpdateDeleteView(generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class AssignmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
