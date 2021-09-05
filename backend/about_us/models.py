from django.core.validators import FileExtensionValidator
from django.utils.safestring import mark_safe
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class ContentModel(models.Model):
    heading = RichTextField(blank=True,null=True)
    content = RichTextUploadingField(blank=True,null=True)

    video = models.FileField(
        upload_to="about_us/video",
        blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['mp4']
            )
        ]
    )

    order = models.PositiveSmallIntegerField(default=1)

    class Meta:
        abstract = True
        

class MainContent(ContentModel):
    title = models.CharField(max_length=255,null=True)  
    active = models.BooleanField(default=True) 

    def __str__(self):  
        return self.title 

    class Meta:
        ordering = ('order',)

class SubContent(ContentModel):
    main_content = models.ForeignKey(MainContent,on_delete=models.CASCADE,related_name="sub_contents")

    def __str__(self):
        return f"{self.pk} subcontent"
