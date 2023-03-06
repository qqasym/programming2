import os
print(os.access("./404/2.py", os.F_OK))    
print(os.access("./404/2.py", os.R_OK))    
print(os.access("./404/2.py", os.X_OK))  
print(os.access("./404/2.py", os.W_OK))      