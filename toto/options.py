from tornado.options import define
import logging


def safe_define(*args, **kwargs):
    try:
        define(*args, **kwargs)
    except Exception as e:
        logging.error(str(e))
