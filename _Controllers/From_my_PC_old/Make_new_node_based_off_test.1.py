import os

p = open('path.txt','r')
line = p.read()
path = line.rstrip('\n')
print("'Old Path: "+str(path)+"'")
#print(path)
node_name = 'new_node'
newpath = path+node_name
print("New Path: "+newpath)
#newpath = r'C:\Users\graytr\Desktop\Test_Folder\new_node' # will eventually fetch this froma txt file

#for x in range(2):
#    if os.path.exists(newpath):
#        print("Exists"+str(os.path.exists(newpath)))
#        f = open(newpath+'\\test1.txt','w')
#        a = newpath
#        f.write(str(a))
#        f.close()
#    
#    else:
#        print("Doesnt Exists")
os.makedirs(node_name)
	
#os.rename( "test1.txt", "test2.py" )
