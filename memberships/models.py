from django.db import models
from django.contrib.auth.models import User
from organizations.models import Organization


class Membership(models.Model):

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('member', 'Member'),
        ('viewer', 'Viewer'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'organization')

    def __str__(self):
        return f"{self.user.username} - {self.organization.name} ({self.role})"