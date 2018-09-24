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
                        count = 0
                        temp_list = []
                        for i in row:
                            if (count < 3):
                                temp_list += [i.upper()] 
                                count += 1
                            else:
                                temp_list += [i.upper()] 
                                self.initial_table += [temp_list]
                                temp_list = []
                                count = 0
                    elif (line_count == 1):
                        count = 0
                        temp_list = []
                        for i in row:
                            if (count < 3):
                                temp_list += [i.upper()] 
                                count += 1
                            else:
                                temp_list += [i.upper()] 
                                self.goal_table += [temp_list]
                                temp_list = []
                                count = 0
                    line_count += 1
                if (line_count > 2):
                    print ("The file had more lines. Just take the two first")
        except:
            print("The file not existed")

    def PrintInitialTable(self):
        print()
        print("Initial Table")
        for fila in self.initial_table:
            text = ""
            for i in fila:
                text += str(i) + " "
            print(text)
        print(" - - - - - - - ")

    def PrintGoalTable(self):
        print()
        print("Goal Table")
        for fila in self.goal_table:
            text = ""
            for i in fila:
                text += str(i) + " "
            print(text)
        print(" - - - - - - - ")

            
    # Check the format of Initial table
    def CorrectFormatInitial(self):
        r_color = 0         # it must be 4
        g_color = 0         # it must be 4
        b_color = 0         # it must be 4
        y_color = 0         # it must be 4
        x_color = 0         # it must be 3
        o_color = 0         # it must be 1
        for row in self.initial_table:
            r_color += row.count("R")
            g_color += row.count("G")
            b_color += row.count("B")
            y_color += row.count("Y")
            x_color += row.count("X")
            o_color += row.count("O")
        if (r_color == 4 and g_color == 4 and b_color == 4 and
            y_color == 4 and x_color == 3 and o_color == 1):
            return True
        else:
            return False

    # Check the format of Goal table
    def CorrectFormatGoal(self):
        r_color = 0         # it must be 4
        g_color = 0         # it must be 4
        b_color = 0         # it must be 4
        y_color = 0         # it must be 4
        x_color = 0         # it must be 3
        o_color = 0         # it must be 1
        for row in self.goal_table:
            r_color += row.count("R")
            g_color += row.count("G")
            b_color += row.count("B")
            y_color += row.count("Y")
            x_color += row.count("X")
            o_color += row.count("O")
        if (r_color == 4 and g_color == 4 and b_color == 4 and
            y_color == 4 and x_color == 3 and o_color == 1):
            return True
        else:
            return False
        
    def CorrectFormat(self):
        return (self.CorrectFormatInitial() and self.CorrectFormatGoal())

    # return -2 => Wrong path
    # return -1 => Wrong format
    # return 0  => Good
    def LoadCSV(self, path):
        self.setPath(path)
        if not (self.IsPath()):
            return -2           # wrong path
        self.LoadData()
        self.PrintInitialTable()
        self.PrintGoalTable()
        if not (self.CorrectFormat()):
            return -1           # wrong format
        return 0
        

csv_file = CSV_Manager()
print(csv_file.LoadCSV("./data.by"))

