import unittest

from tests.QuakeLogTest import TestQuakeLog
from tests.ReadFileTest import TestReadFile

def __init__(self, *args, **kwargs): # pragma: no cover
  TestQuakeLog.__init__(self, *args, **kwargs)
  TestReadFile.__init__(self, *args, **kwargs)