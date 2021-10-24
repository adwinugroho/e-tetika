# Generated by Django 3.0 on 2021-10-24 04:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, max_length=155, null=True)),
                ('no_hp', models.CharField(blank=True, max_length=13, null=True)),
                ('is_performer', models.BooleanField(default=False)),
                ('is_partner', models.BooleanField(default=False)),
                ('joined', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('group_name', models.CharField(blank=True, max_length=155, null=True)),
                ('group_description', models.CharField(blank=True, max_length=255, null=True)),
                ('group_category', models.CharField(blank=True, max_length=155, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
