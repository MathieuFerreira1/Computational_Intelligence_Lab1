import csv

with open('Bank_Loan_Status_Dataset/credit_train.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    column_names = next(csvreader)
    print(column_names)