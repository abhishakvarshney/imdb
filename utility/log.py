"""
    logging File to access logs
"""
import logging
from datetime import datetime
from django.conf import settings


class log:
    """
        logging File to access logs
    """
    DEBUG_LOGS = True
    BLOCKED_LOG_TAGS = []

    @classmethod
    def exception(cls, e):
        """

        @param e:
        """
        logger = logging.getLogger(settings.GENERAL_LOGGER)
        logger.exception(e)

    @classmethod
    def info(cls, e):
        """

        @param e:
        """
        logger = logging.getLogger(settings.GENERAL_LOGGER)
        logger.info(e)

    @classmethod
    def error(cls, e):
        """

        @param e:
        """
        logger = logging.getLogger(settings.GENERAL_LOGGER)
        logger.error(e)

    @classmethod
    def warning(cls, e):
        """

        @param e:
        """
        logger = logging.getLogger(settings.GENERAL_LOGGER)
        logger.warning(e)


    @classmethod
    def d(cls, logText):
        """

        @param TAG:
        @param logText:
        """
        logger = logging.getLogger(settings.GENERAL_LOGGER)
        logger.debug('|D| ' + str(datetime.now()) + ' | ' + '| ' + logText + '|')
