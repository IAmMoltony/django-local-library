# Generated by Django 5.0.6 on 2024-06-25 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_book_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('M', 'Maintenance'), ('O', 'On loan'), ('A', 'Available'), ('R', 'Reserved')], default='M', help_text='Book availability', max_length=1),
        ),
    ]