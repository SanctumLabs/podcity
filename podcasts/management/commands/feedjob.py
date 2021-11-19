import logging

from django.core.management.base import BaseCommand
from django.conf import settings

import feedparser
from dateutil import parser
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

from podcasts.models import Episode


logger = logging.getLogger(__name__)


def save_new_episode(feed):
    """
    Saves new episodes to the database.

    Checks the episode GUID against the episodes currently stored in teh database. if not found, then a new Episode is
    added to the database.

    :param feed: feedparser object
    :return: None
    """
    podcast_title = feed.channel.title
    podcast_image = feed.channel.image.href

    for item in feed.entries:
        if not Episode.objects.filter(guid=item.guid).exists():
            episode = Episode(
                title=item.title,
                description=item.description,
                pub_date=parser.parse(item.published),
                link=item.link,
                image=podcast_image,
                podcast_name=podcast_title,
                guid=item.guid
            )
            episode.save()


def fetch_realpython_episodes():
    _feed = feedparser.parse("https://realpython.com/podcasts/rpp/feed")
    save_new_episode(_feed)


def fetch_talkpython_episodes():
    _feed = feedparser.parse("https://talkpython.fm/episodes/rss")
    save_new_episode(_feed)


def delete_job_executions(max_age=604_800):
    """
    Deletes all apscheduler job execution logs older than max_age seconds.

    :param max_age: maximum age in seconds
    :return: None
    """
    DjangoJobExecution.objects.delete_old_job_executions(max_age=max_age)


class Command(BaseCommand):
    help = "Runs apscheduler to fetch podcast feeds"

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            func=fetch_realpython_episodes,
            trigger='interval',
            # todo: make this configurable and set to a week in a production environment, minutes in a day * 7
            minutes=2,
            id="The Real Python Podcast",
            max_instances=1,
            replace_existing=True
        )
        logger.info("Added job: The Real Python Podcast")

        scheduler.add_job(
            func=fetch_talkpython_episodes,
            trigger='interval',
            # todo: make this configurable and set to a week in a production environment, minutes in a day * 7
            minutes=2,
            id="Talk Python Feed",
            max_instances=1,
            replace_existing=True
        )
        logger.info("Added job: Talk Python Feed")

        scheduler.add_job(
            func=delete_job_executions,
            trigger=CronTrigger(
                # Midnight on Monday, before start of next work week
                day_of_week="mon", hour="00", minute="00"
            ),
            id="Delete Old Job Executions",
            max_instances=1,
            replace_existing=True
        )
        logger.info("Added weekly job: Delete Old Job Executions")

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shutdown successfully.")
