# Generated by Django 2.2 on 2019-04-10 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('content', models.TextField()),
                ('url', models.CharField(max_length=127)),
                ('uploader', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('writer', models.CharField(blank=True, max_length=63, null=True)),
                ('paste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='pasteapp.Paste')),
            ],
        ),
    ]
