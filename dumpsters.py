import csv
from fileinput import filename
class CSVDumpster:
    """
    This should store a collection of userstats persistently and add new via writedata method
    Then when list reaches 100 elements, it's written in csv file and cleared
    """
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.events = []
    def writedata(self, data):
        self.events.append(data)
        if len(self.events)>=100:
            self.dedupe()
            with open(self.filename, 'a') as hireme_file:
                hireme_writer = csv.writer(hireme_file)
                hireme_writer.writerows(self.events)
            self.events.clear()
    def dedupe(self) -> list:
        """
        This method checks for duplicated forms in self.events and removes duplicates
        """
        self.events = list(set(self.events))