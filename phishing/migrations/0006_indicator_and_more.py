# Generated by Django 5.0 on 2024-06-01 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phishing', '0005_gif'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('indicator_type', models.CharField(choices=[('sender', 'Sender'), ('subject', 'Subject'), ('content', 'Content')], max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='phishingtemplate',
            name='indicators_of_compromise',
        ),
        migrations.AddField(
            model_name='phishingtemplate',
            name='indicators_of_compromise',
            field=models.ManyToManyField(to='phishing.indicator'),
        ),
    ]
