from django.db import models


class Themes(models.Model):

    title = models.CharField(max_length=255)
    user = models.ForeignKey(
        'accounts.Users', on_delete=models.CASCADE
    )


    class Meta:
        db_table = 'themes'


class Comments(models.Model):

    comment = models.CharField(max_length=1000)
    user = models.ForeignKey(
        'accounts.Users', on_delete=models.CASCADE
    )
    theme = models.ForeignKey(
        'Themes', on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'comments'