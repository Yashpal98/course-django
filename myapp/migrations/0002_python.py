# Generated by Django 2.2.4 on 2019-10-20 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Python',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(max_length=300)),
                ('pub_date', models.DateField()),
                ('video', models.FileField(default='', upload_to='videos/python')),
            ],
        ),
    ]
