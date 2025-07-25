# Generated by Django 5.0 on 2024-06-16 15:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportingSpam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reported_at', models.DateTimeField(auto_now_add=True)),
                ('clicked_link', models.BooleanField(default=False)),
                ('credentials_entered', models.BooleanField(default=False)),
                ('mail_header', models.TextField()),
                ('mail_content', models.TextField()),
                ('subject', models.CharField(max_length=255)),
                ('sender', models.CharField(max_length=255)),
                ('links', models.TextField(help_text='Alle separierten Links, durch Kommas getrennt.')),
                ('sender_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reportingspam', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
