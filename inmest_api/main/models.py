from django.db import models
import datetime
from users import cohort


# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=1000)
    descriptionn= models.TextField(default="N/A", blank=True, null=True)
    date_created = models.DateField(auto_now_add=True, blank=True, null=True)
    date_modified = models.DateField(auto_now=True, blank=True, null=True)
    
 #ClassSchedule (title, description, start_date_and_time, end_date_and_time, is_repeated, repeat_frequency, is_active, organizer, cohort [should reference Cohort model], venue)
#ClassAttendance(class_schedule [Should reference ClassSchedule model], attendee [should reference IMUser model], is_present, date_created, date_modified, author [should reference IMUser model])
##Query (title, description, submitted_by [should reference IMUser], assigned_to [should reference IMUser], resolution_status [PENDING, IN_PROGRESS, DECLINED, RESOLVED], date_created, date_modified, author [should reference IMUser model])
#QueryComment (query [should reference Query model], comment, date_created, date_modified, author [should reference IMUser model])
        
class ClassSchedule(models.Model):
    title = models.CharField(max_lenth=50),
    description = models.TextField(default="N/A", BLANK=True, null=True),
    start_date_and_time=models.DateTimeField(auto_now=True, blank=True, null=True),
    end_date_and_time=models.DateTimeField(auto_now=True, blank=True, null=True),
    is_repeated=models.BooleanField(default=False),
    repeat_frequency=models.BooleanField(default=False),
    is_active=models.BooleanField(default=True),
    organizer=models.CharField(max_lenth=20),
    cohort=models.ForeignKey(cohort),
    

class ClassAttendance(models.Model):
    ClassSchedule=models.ForeignKey(ClassSchedule),
    attendance=models.ForeignKey()
    
    
    