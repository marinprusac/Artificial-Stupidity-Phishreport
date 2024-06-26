# Generated by Django 5.0.6 on 2024-05-15 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phishing_tracker', '0002_remove_phishingevent_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='phishingevent',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='phishingevent',
            name='malicious_domain_dns_record_a',
            field=models.GenericIPAddressField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='phishingevent',
            name='malicious_domain_dns_record_mx',
            field=models.GenericIPAddressField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='phishingevent',
            name='malicious_domain_dns_record_ns',
            field=models.GenericIPAddressField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='phishingevent',
            name='malicious_domain_registartion_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='phishingevent',
            name='status',
            field=models.CharField(choices=[('INPROGRESS', 'In Progress'), ('DONE', 'Done'), ('TODO', 'To Do')], default='TODO', max_length=100),
        ),
    ]
