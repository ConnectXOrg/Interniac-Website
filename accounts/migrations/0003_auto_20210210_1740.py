# Generated by Django 3.1.6 on 2021-02-10 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210210_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='awards_achievements',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='extracurriculars',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='hs',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='hs_addy',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='leadership_roles',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='link1',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='link2',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='link3',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='link4',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='skills',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='teacher_or_counselor_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='teacher_or_counselor_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='volunteering_experience',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='work_exp',
            field=models.TextField(blank=True, null=True),
        ),
    ]