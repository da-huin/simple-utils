import logging


_logger = logging.getLogger()
formatter = logging.Formatter(
    '[%(levelname)s][%(asctime)s] %(message)s', '%Y-%m-%d %H:%M:%S')

handler = logging.StreamHandler()
handler.setFormatter(formatter)
_logger.addHandler(handler)
_logger.setLevel(logging.INFO)

def _get_message(*args):
    return ' '.join([str(s) for s in args])

def debug(*args):
    _logger.debug(_get_message(*args))


def info(*args):
    _logger.info(_get_message(*args))


def warning(*args):
    _logger.warning(_get_message(*args))


def error(*args):
    _logger.error(_get_message(*args))


def critical(*args):
    _logger.critical(_get_message(*args))