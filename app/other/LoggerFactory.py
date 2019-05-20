import logging
import os


def get_logger(file='', name=''):

    formatter = logging.Formatter(
        '%(asctime)-15s %(message)s')

    log = logging.getLogger(
        os.path.basename(__file__))
    log.setLevel(logging.DEBUG)

    if log.hasHandlers():
        log.handlers.clear()

    if file and name:
        path_to = file
        if not os.path.exists(path_to):
            os.makedirs(path_to)

        handler = logging.FileHandler(
            filename=path_to + name)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)
        log.addHandler(handler)

    handler1 = logging.StreamHandler()
    handler1.setLevel(logging.INFO)
    handler1.setFormatter(formatter)
    log.addHandler(handler1)

    return log
