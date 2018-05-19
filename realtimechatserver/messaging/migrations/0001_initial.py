# Generated by Django 2.0.4 on 2018-05-14 19:21

from django.db import migrations, models
import django.db.models.deletion
import realtimechatserver.helper


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash_id', models.CharField(default=realtimechatserver.helper.create_hash, max_length=32, unique=True)),
                ('date', models.IntegerField(default=realtimechatserver.helper.time_stamp)),
                ('text', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='MessageThread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash_id', models.CharField(default=realtimechatserver.helper.create_hash, max_length=32, unique=True)),
                ('title', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='UnreadReceipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField(default=realtimechatserver.helper.time_stamp)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receipts', to='messaging.Message')),
            ],
        ),
    ]
