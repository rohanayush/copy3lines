# open both files
import os
os.chdir("./")
files = os.listdir('dira')
content=""
for i in files:
    with open('./dira/'+i, 'r') as src:
        for j, val in enumerate(src):
            print(j,"for",i,"==",val)
            if(j<=2 and i=='file2.txt'):
                content +=val
            elif(j>2):
                with open('./dirb/'+i,'r') as out:
                    data = out.readlines()
                data=''.join(data)
                content += data 
                print("content here",content)

                with open('./dirc/'+i,"w+") as wr:
                    wr.write(content)
                content=""
print(files)


