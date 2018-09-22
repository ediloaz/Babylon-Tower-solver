# File of CSV files manager
# 
# Programmer
#   Edisson López @ediloaz
# September, 2018
#

import csv

class CSV_Manager(object):
    def __init__(self):
        path = ""       # with "babylon tower" extention .by
        initial_table = []
        goal_table = []
        
    def setPath(self, path):
        self.path = path

    def getPath(self):
        return selfpath

    def IsPath(self):
        if (self.path[-3:] == ".by" or self.path[-4:] == ".by/"):
            return True
        else:
            return False
    
    def LoadData(self):
        try:
            with open(self.path) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                self.initial_table = []
                self.goal_table = []
                for row in csv_reader:
                    if (line_count == 0):
                        for i in row:
                            self.initial_table += [i]
                    elif (line_count == 1):
                        for i in row:
                            self.goal_table += [i]
                    line_count += 1
                if (line_count > 2):
                    print ("The file had more lines. Just take the two first")
        except:
            print("No se encontró el archivo")

            
a = CSV_Manager()
a.setPath("./datos.by")
if not (a.IsPath()):
    print("path malo")
else:
    a.LoadData()
