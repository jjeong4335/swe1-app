from django.db import migrations
from django.utils import timezone


def seed(apps, schema_editor):
    Question = apps.get_model("polls", "Question")
    Choice = apps.get_model("polls", "Choice")
    if Question.objects.exists():
        return
    q = Question.objects.create(question_text="What's up?", pub_date=timezone.now())
    for text in ("Not much", "The sky", "Just hacking again"):
        Choice.objects.create(question=q, choice_text=text, votes=0)


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed, migrations.RunPython.noop),
    ]
