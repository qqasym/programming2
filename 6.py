import string, os
if not os.path.exists("Textfiles"):
   os.makedirs("Textfiles")
for Textfiles in string.ascii_uppercase:
   with open(Textfiles + ".txt", "w") as f:
       f.writelines(Textfiles)