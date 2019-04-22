from django.db import models

# for storing images in filefield for MDTouch image upload or document upload.
class File(models.Model):
    file = models.FileField(blank=False, null=False)
#    remark = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=2,default='p')
    userid = models.IntegerField(default=1)

    def __str__(self):
        return str(self.userid)
