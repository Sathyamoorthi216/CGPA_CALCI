import csv
import json

R2019 = []

with open('R2019.csv', 'r',encoding='utf-8') as f:
    reader = csv.reader(f,delimiter=',')
    for row in reader:
        R2019.append(row)

class cgpaCalci:

    def __init__(self):
        self.data = []

    def loadCSV(self,fileName):
        for i in fileName:
            with open(i, 'r',encoding='utf-8') as csvf:
                r = csv.reader(csvf)
                for i in r:
                    self.data.append(i)

        for sublist in self.data:
            grade_map = {'O': 10, 'A+': 9, 'A': 8, 'B+': 7, 'B': 6, 'C': 5, 'RA': 0, 'SA': 0, 'W': 0}
            if sublist[2].lower() == 'grade':
                sublist.append('grade points')
            if sublist[2] in grade_map:
                sublist.append(grade_map[sublist[2]])  
                        
        return self.data
    
    def gpa_cal(self):
            
            tot_C = 0
            tot_CGp = 0
            GPA = [0,0,0,0,0,0,0,0,0,0,0,0]

            for i in range(10):
                for sublist1 in R2019[1:]:
                    for sublist2 in self.data[1:]:
                        print(i)
                        if sublist1[:2] == sublist2[:2]:
                                if int(sublist2[0])==i+1:
                                    if sublist2[2].lower() != 'ra':
                                        tot_C += int(sublist2[3])
                                        tot_CGp += sublist2[4]*int(sublist2[3])
                                        GPA[i] = round(tot_CGp/tot_C,2)
                tot_C = 0                      
                tot_CGp = 0
            
            return GPA
    
    def cgpa_cal(self):

        total_C = 0
        total_CGp = 0

        for sublist1 in R2019[1:]:
                for sublist2 in self.data[1:]:
                    if sublist1[:2] == sublist2[:2]:
                            if sublist2[2].lower() != 'ra':
                                total_C += int(sublist2[3])
                                total_CGp += sublist2[4]*int(sublist2[3])
        cgpa = round(total_CGp/total_C,2)
        return cgpa

name = input("Enter name :")
n = int(input("Enter no. of input files :"))

files =  []

for i in range(n):
     a =  input("Enter the name of file:")
     files.append(a)

sample = cgpaCalci()
data = sample.loadCSV(files)
gpa = sample.gpa_cal()
cgpa = sample.cgpa_cal()

X = {
     "name":name,
     "gpa":gpa,
     "cgpa":cgpa
}

y = json.dumps(X)

print(y)
