from django.db import models

class Instructor(models.Model):
    user = models.OneToOneField('user.User', on_delete=models.CASCADE)
    categories = models.ManyToManyField('course.CourseCategory', blank=True)
    start_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ' - ' + self.user.email

    class Meta:
        ordering = ['-id']