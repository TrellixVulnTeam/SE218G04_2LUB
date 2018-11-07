# Generated by Django 2.1.3 on 2018-11-02 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('max_degree', models.IntegerField()),
                ('study_years', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=3)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Class.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('course', models.ManyToManyField(to='Class.Course')),
            ],
        ),
        migrations.AddField(
            model_name='grade',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Class.Student'),
        ),
    ]