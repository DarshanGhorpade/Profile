# Generated by Django 4.0.2 on 2022-05-19 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0003_alter_profile_profile_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, null=True)),
                ('email', models.CharField(default='', max_length=200, null=True)),
                ('feedback_subject', models.CharField(default='', max_length=300, null=True)),
                ('feedback_message', models.CharField(default='', max_length=500, null=True)),
            ],
        ),
    ]