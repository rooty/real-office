import os

from django.core.files import File

from .robots import *

def read_fixture_file(path, file):
    return File(open(
        os.path.join(os.path.dirname(os.path.abspath(path)), '..',
                     'fixtures', file), 'r'))
