# Generated by Django 5.1.3 on 2024-12-04 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminEmployeeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminemployeecredentials',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='adminemployeecredentials',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='adminemployeecredentials',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='adminemployeecredentials',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='adminemployeecredentials',
            name='profilePhoto',
            field=models.ImageField(blank=True, null=True, upload_to='Images/Admin/'),
        ),
        migrations.AlterField(
            model_name='adminemployeecredentials',
            name='role',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
