import csv
import json

from configurations import CONFIGURATIONS

class Util(object):

    def get_dictsites(self, filename):
        dictsites = []
        with open(filename, 'rU') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                dictsites.append(row)
        return dictsites

    def load_config(self, filename=CONFIGURATIONS):
        with open(filename) as settings_file:
            return json.load(settings_file)
