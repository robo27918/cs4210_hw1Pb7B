#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

def make_categorical_features():
  '''
Feauture: 'Age'              'Spectacle',          'Astigmatism'      'Tear'
          1= "Young          1= Myope                1="Yes"             1="reduced"  
          2="Presbyopic"     2= Hypermetrope         2="No"              2="Normal" 
          3="Preprebyopic"

       this function returns a 4d list where each column is a feature as shown above
  '''
  # for readability purposes, sepearate each column into own list
  
  age_data = [age_val[0] for age_val in db]
  spec_data = [spec_val[1] for spec_val in db]
  astig_data = [astig_val[2] for astig_val in db]
  tear_data = [tear_val[3] for tear_val in db]
  
 
  
  age = [1 if age =="Young" else 2 if age=="Presbyopic" else 3 for age in age_data] 
  spectacle = [1 if spec=="Myope" else 2 for spec in spec_data]
  astigmatism = [1 if astig=="Yes" else 2 for astig in astig_data]
  tear =[1 if tear=="Reduced" else 2 for tear in tear_data]
  X= [age, spectacle, astigmatism, tear]
  
  return [list (i) for i in zip(*X)]    
#transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here

X = make_categorical_features()

def make_categorial_classes():
  ls = []
  for element in db:
    if element[4] =="Yes":
      ls.append(1)
    if element[4] == "No":
      ls.append(2)
  return ls

#transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here
Y = make_categorial_classes()


#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy' )
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()