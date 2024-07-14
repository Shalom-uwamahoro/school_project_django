# Generated by Django 5.0.6 on 2024-07-14 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='courses_taught',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='subject_specialisation',
        ),
        migrations.AddField(
            model_name='teacher',
            name='bank_account_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='picture',
            field=models.ImageField(default='jhfgdfjkjl;kj', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='subject_specialization',
            field=models.CharField(default='ttuyyurytruu', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='country',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='education_level',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]