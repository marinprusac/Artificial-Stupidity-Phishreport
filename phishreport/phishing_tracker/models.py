from django.db import models

# Create your models here.

class PhishingEventModel(models.Model):
    event_id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)
    date = models.DateField()
    affected_brand = models.CharField(max_length=100)
    description = models.TextField()
    malocious_campaign_url = models.URLField()
    malicious_domain_registartion_date = models.DateField()

    malicious_domain_dns_record_a = models.GenericIPAddressField()
    malicious_domain_dns_record_ns = models.GenericIPAddressField()
    malicious_domain_dns_record_mx = models.GenericIPAddressField()

    list_of_matching_keywords = models.TextField()
    STATUS_TYPES = {
        ('TODO', 'To Do'), 
        ('INPROGRESS', 'In Progress'), 
        ('DONE', 'Done')
    }
    status = models.CharField(max_length=100, choices=STATUS_TYPES, default='TODO')

class AnalystCommentModel(models.Model):
    analyst_comment_id = models.AutoField(primary_key=True)
    event = models.ForeignKey(PhishingEventModel, on_delete=models.CASCADE)
    date = models.DateField()
    comment = models.TextField()