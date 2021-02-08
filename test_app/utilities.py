from datetime import datetime
from os.path import splitext

from dynamic_creation_fields.settings import MEDIA_DIR


def get_timestamp_path(instance, filename):
    return '%s/%s%s' % (MEDIA_DIR, datetime.now().timestamp(), splitext(filename)[1])
