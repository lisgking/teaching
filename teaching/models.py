import uuid

from django.db import models

class SignUpList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student_id = models.ForeignKey('UserInfo')
    course_id = models.ForeignKey('CourseInfo')

class UserInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=200)
    user_pass = models.CharField(max_length=200)
    name = models.CharField(max_length=200,blank=False)
    user_type = models.IntegerField(blank=False)
    photo = models.CharField(max_length=200,blank=True)
    telephone = models.CharField(max_length=200,blank=True)
    email = models.CharField(max_length=200,blank=True)
    address = models.CharField(max_length=200,blank=True)
    age =  models.IntegerField(blank=True)
    sex = models.CharField(max_length=200,blank=True)
    content = models.CharField(max_length=200,blank=True)
    

class CourseInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    teacher_id = models.ForeignKey('UserInfo')
    course_type = models.IntegerField(blank=False)
    is_fid = models.IntegerField(blank=False)
    course_name = models.CharField(max_length=200)
    course_big_user = models.IntegerField(blank=False)
    course_score = models.IntegerField(blank=False)
    building_id = models.ForeignKey('Building')
    room_id = models.ForeignKey('Rooms')
    course_begin_time = models.CharField(max_length=200)
    course_end_time = models.CharField(max_length=200)
    course_time = models.CharField(max_length=200)
    course_content = models.TextField(blank=True)

class Building(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)

class Rooms(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    building_id = models.ForeignKey('Building')
    name = models.CharField(max_length=200)