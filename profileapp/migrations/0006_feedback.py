# Generated by Django 4.0.4 on 2022-05-20 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0005_delete_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, null=True)),
                ('email', models.CharField(default='', max_length=200, null=True)),
                ('subject', models.CharField(default='', max_length=200, null=True)),
                ('message', models.CharField(default='', max_length=300, null=True)),
            ],
        ),
    ]
