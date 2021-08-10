from savReaderWriter import SavReader, SavWriter, SavHeaderReader, SPSSIOError
import pandas as pd

class SavFile:
    """A SPSS file processor."""

    def __init__(self, file_name):

        ### PRIVATE CLASS ATTRIBUTES
        self.__name = file_name

        with SavReader(file_name, returnHeader=True, ioUtf8=True) as reader, SavHeaderReader(file_name, ioUtf8=True) as headerReader:
            self.data = pd.DataFrame(reader.all()[1:], columns=reader.all()[0])
            self.metadata = headerReader.all()
            self.report = str(headerReader)

        ### PUBLIC CLASS ATTRIBUTES

    # def close(self):
    #     self.__header.close()
    #     self.__reader.close()        
