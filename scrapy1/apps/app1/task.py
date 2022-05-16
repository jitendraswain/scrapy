from __future__ import absolute_import

import logging
logger = logging.getLogger(__name__)

from celery import shared_task

@shared_task
def add(x, y):
    # Only for testing...
    return x + y