import os
BASE_DIR = os.getcwd()
LOGGING_DIR = os.path.join(BASE_DIR, "logs")
if not os.path.exists(LOGGING_DIR):
    os.makedirs(LOGGING_DIR)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'error_logs': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_DIR, "error.log"),
            'formatter': 'verbose',
        },
        'warn_logs': {
            'level': 'WARN',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_DIR, "warn.log"),
            'formatter': 'verbose',
        },
        'info_logs': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_DIR, "info.log"),
            'formatter': 'verbose',
        }
    },
    'loggers': {
        '': {
            'handlers': ['error_logs', 'warn_logs', 'info_logs'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}