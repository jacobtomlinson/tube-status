from time import time
import requests
import xml.etree.ElementTree as et

from .Line import Line

class Status(object):
    """
    Line Status connection object
    """
    def __init__(self):
        self.update_url = "http://cloud.tfl.gov.uk/TrackerNet/LineStatus"
        self.lines = {}
        self.last_update = 0
        self.last_request = None
        self.update_time = 30 #TfL asks for 30 seconds between requests

    def update_status(self):
        if (time() - self.last_update) > self.update_time:
            self.last_request = requests.get(self.update_url)
            self.last_update = time()

        root = et.fromstring(self.last_request.content)
        for child in root:
            current_line = Line()
            current_line.name = child[1].get('Name')
            current_line.status_code = child[2].get('ID')
            self.lines[current_line.name] = current_line

    def get_status(self, line_code):
        self.update_status()
        if line_code in self.lines:
            return self.lines[line_code].status_code
        else:
            return None

    def list_lines(self):
        self.update_status()
        return self.lines.keys()
