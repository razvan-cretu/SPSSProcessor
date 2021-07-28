from savReaderWriter import SavReader, SavWriter, SavHeaderReader, SPSSIOError
import pandas as pd

class SavFile(object):
    """A SPSS file processor."""

    def __init__(self, file_name ):
        self._name = file_name

