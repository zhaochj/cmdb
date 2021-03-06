# Generated by Django 2.2 on 2020-09-05 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=48)),
            ],
            options={
                'db_table': 'entity',
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48)),
                ('meta', models.TextField(blank=True, null=True)),
                ('reference', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'field',
            },
        ),
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48, unique=True)),
                ('desc', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'schema',
            },
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('deleted', models.BooleanField(default=False)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dbapi.Entity')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dbapi.Field')),
            ],
            options={
                'db_table': 'value',
            },
        ),
        migrations.AddField(
            model_name='field',
            name='schema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dbapi.Schema'),
        ),
        migrations.AddField(
            model_name='entity',
            name='schema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dbapi.Schema'),
        ),
    ]
