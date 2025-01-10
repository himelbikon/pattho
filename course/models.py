from django.db import models


class CourseCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    image = models.ImageField(upload_to='course/course_category/', null=True, blank=True)

    def __str__(self):
        return self.name
