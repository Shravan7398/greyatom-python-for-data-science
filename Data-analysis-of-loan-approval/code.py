# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank = pd.read_csv(path)


#Code starts here

#Identifying Dtypes of dataset
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var.head(5))


numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var.head(5))

#missing values

banks = bank.drop( 'Loan_ID',axis = 1)
banks.isnull().sum()
bank_mode = banks.mode()

banks.fillna(bank_mode, inplace = True)
print(np.shape(banks))


#average loan amount

avg_loan_amount = banks.pivot_table(index = ['Gender','Married'],values = ['LoanAmount'],aggfunc=np.mean)
print(avg_loan_amount.head(5))

#percentage loan approved based on employment type


loan_approved_se = len((banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y'))

loan_approved_nse = len((banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y'))

percentage_se = loan_approved_se*100/614
print(percentage_se)

percentage_nse = loan_approved_nse*100/614
print(percentage_nse)

#applicants with long loan amount term

loan_term = banks['Loan_Amount_Term'].apply(lambda x : float(x) / 12)

big_loan_term = len(loan_term>=25)
print(big_loan_term)

#average income of an applicant and the average loan given

loan_groupby = banks.groupby('Loan_Status')

loan_groupby = loan_groupby['ApplicantIncome','Credit_History']

mean_values = loan_groupby.agg([np.mean])
print(mean_values)




