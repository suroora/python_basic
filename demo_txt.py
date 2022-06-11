file=open("demo.txt",'a')
demo=file.write("am append")
file.close()

file=open("demo.txt",'r')
demo1=file.read()
print(demo1)
file.close()

