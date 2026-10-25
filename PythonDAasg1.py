#--------------NUMPY ARRAY OPERATIONS
##----1. Create a 1D NumPy Array
import numpy as np
print("1.Array[1D] temperatures_w1 :")
temperatures_w1 = np.array([22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9])
print(temperatures_w1)
##----2. Inspection and Properties
print("2.Inspection and Properties :")
print("Shape : ", (temperatures_w1.shape))
print("Datatype : ", (temperatures_w1.dtype))
print("Elements : ", (temperatures_w1.size))
##---- 3. Array Operations
print("3.Array Operations :")
Fahrenheit = ((temperatures_w1 * 9/5) + 32)
print("Fahrenheit : ",Fahrenheit)
print("Minimum Temperature : ",np.min(Fahrenheit))
print("Maximum Temperature : ",np.max(Fahrenheit))
print("Mean Temperature : ",round(np.mean(Fahrenheit),2))
##---- 4. Array Slicing and Indexing
print("4. Array Slicing and Indexing :")
print("First three days : ",Fahrenheit[0:3])
print("Weekend two days : ",Fahrenheit[-2:])
print("Middle three days : ",Fahrenheit[2:5])
##---- 5. Create a 2D Array
print("5.Create a 2D Array :")
temperatures = np.array([[22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9],
                       [19.2, 22.5, 21.3, 24.0, 23.5, 22.8, 20.1]])
print(temperatures)
##---- 6. Inspect and Slice the 2D Array
print("6.Inspect and Slice the 2D Array :")
print("Shape : ", (temperatures.shape))
print("Datatype : ", (temperatures.dtype))
print("Elements : ", (temperatures.size))
print("1st Week : ", temperatures[0:1,:])
print("2nd Week : ", temperatures[1:2,:])
print("Weekends :\n", temperatures[0:,-2:])

#----------------PANDAS SERIES
import pandas as pd
#----1. Creating Pandas Series
print("1. Creating Pandas Series ")
Marks=pd.Series([95, 92, 89, 85, 80],index=['Rank1', 'Rank2', 'Rank3', 'Rank4', 'Rank5'])
print(Marks)
#----2. Indexing and Slicing
print("2. Indexing and Slicing ")
print("1st Rank : ",Marks.iloc[0])
print("\nTop 3 Rank :\n",Marks.loc["Rank1":"Rank3"])
print("\n3rd Rank : ", Marks.iloc[2])
result = Marks[Marks > 90]
print("\nRanks Greater than 90 marks are :\n",result)
#----3. Manipulating Series
print("\n3. Manipulating Series ")
Marks.update(pd.Series({'Rank1': 100}))
print("Updated Marks:\n",Marks)
Marks= Marks.drop("Rank5")
print("Removed & Updated Marks:\n",Marks)
Marks= Marks/10
print("CGPA:\n",Marks)

#-------------PANDAS DATAFRAME
#----1. Creating Pandas DataFrame
print("1. Creating Pandas DataFrame")
transactions = pd.DataFrame({
    'TransactionID' : [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'ProductCategory' : ['Electronics', 'Clothing', 'Electronics', 
                         'Furniture','Clothing', 'Electronics', 
                         'Furniture', 'Clothing', 'Furniture', 'Electronics'],
    'Region' : ['North', 'South', 'North', 'East', 'West', 'North', 'East', 
                'West', 'South', 'North'],
    'Amount' : [200, 150, 300, 450, 200, 250, 300, 180, 350, 400]
})
#----2. Data Exploration
print("2.Data Exploration")
print(transactions)
print("HEAD")
print(transactions.head())
print("TAIL")
print(transactions.tail())
print("\nSHAPE : ",transactions.shape)
print("\nCOLUMNS : ",transactions.columns)
print("\nDATATYPE : ",transactions.dtypes)
##Display only the 'ProductCategory' and 'Amount' columns
print("'ProductCategory' and 'Amount'")
print(transactions[['ProductCategory','Amount']])
##Retrieve the last 3 columns of the DataFrame using iloc or loc
print("Last 3 columns of the DataFrame using iloc")
print(transactions.iloc[:,-3:])
##Filter rows where the 'Region' is 'North' and 'Amount' is greater than 200
print("'Region' is 'North' and 'Amount' is greater than 200")
print(transactions[(transactions['Region'] == 'North') & 
                   (transactions['Amount'] > 200)])
##Find the value counts for the 'ProductCategory' column
print("Value Counts")
print(transactions['ProductCategory'].value_counts())
##Find the unique values in the 'Region' column
print("Unique Values of Region")
print(transactions['Region'].unique())
##Group by 'Region' and find the mean amount for each region
print("Groupby & Mean")
print(transactions.groupby('Region')['Amount'].mean())

#----3. Manipulating the DataFrame
print("3. Manipulating the DataFrame")
#Modify the 'Amount' for the transaction with TransactionID 102 to 165
print("Modify the 'Amount' for the transaction with TransactionID 102 to 165")
transactions.loc[transactions['TransactionID'] == 102, 'Amount'] = 165
print(transactions)
#Add a new column 'Discount' by calculating 10% of the 'Amount'.
print("Add a new column 'Discount' by calculating 10% of the 'Amount'")
transactions['Discount'] = transactions['Amount']* 0.10
print(transactions)
#Remove the row with TransactionID 109
print("Remove the row with TransactionID 109")
transactions = transactions.drop(transactions[transactions['TransactionID']==109].index)
print(transactions)
#Delete the 'Discount' column from the DataFrame
print("Delete the 'Discount' column from the DataFrame")
transactions = transactions.drop('Discount', axis=1)
print(transactions)