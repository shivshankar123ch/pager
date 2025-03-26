from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Contact)
admin.site.register(Blogs)
admin.site.register(Certificate)




class InternshipAdmin(admin.ModelAdmin):
    list_display = ('fullname',
                    'usn',
                    'phonenumber',
                    'email',
                    'college_name',
                    'offer_status',
                    'start_date',
                    'end_date',
                    'proj_report',
                    'timeStamp')
    search_fields=('fullname','usn','phonenumber','email')
    list_filter=['college_name','proj_report','offer_status']

admin.site.register(Internship,InternshipAdmin)
