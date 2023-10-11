from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import*


class ConsultationBookingAdmin(admin.ModelAdmin):
    list_display = ('student', 'consultation', 'is_confirmed')
    list_filter = ('is_confirmed',)
    actions = ['confirm_bookings', 'unconfirm_bookings']

    def confirm_bookings(self, request, queryset):
        queryset.update(is_confirmed=True)

    confirm_bookings.short_description = 'Подтвердить выбранные бронирования'

    def unconfirm_bookings(self, request, queryset):
        queryset.update(is_confirmed=False)

    unconfirm_bookings.short_description = 'Отменить выбранные бронирования'


# Register your models here.
admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Department)
admin.site.register(Consultation)
admin.site.register(Course)
admin.site.register(Report)
admin.site.register(ConsultationBooking, ConsultationBookingAdmin)
admin.site.register(Announcement)
admin.site.register(Assignment)
#admin.site.register(ConsultationBooking, ConsultationBookingAdmin)