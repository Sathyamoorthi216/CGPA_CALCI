import csv
import json

class cgpaCalci:
    
    # initializing list in constructor
    
    def __init__(self):
        self.data = []

    # loading csv file as list of lists

    def loadCSV(fileName):
        with open(fileName, 'r') as csvf:
            r = csv.reader(csvf)
            for row in r:
                data.append(row)
        return data
    
    # to calculate gpa
    
    def gpa_cal(self):
        
        tot_CGp = 0		#tot_CGp - total(Credit * Gradepoints)
        tot_C = 0		#tot_C - total Credits
        
        for sublist in data:
            for i in sublist:
                
        

R2019_data = cgpacalci.loadCSV('R2019.csv')

