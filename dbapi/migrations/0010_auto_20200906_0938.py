# Generated by Django 2.2 on 2020-09-06 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dbapi', '0009_students_test_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('age', models.IntegerField()),
                ('tel', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='schema',
            name='name',
            field=models.CharField(max_length=48),
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.FloatField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cars', to='dbapi.Person')),
            ],
        ),
    ]