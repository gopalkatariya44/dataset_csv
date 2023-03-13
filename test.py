# Driver function
import os

# if _name_ == "_main_":
for (root, dirs, files) in os.walk(r"D:\dataset2\UOT32\archive (2)\Scraped Images", topdown=True):
    # print(root)
    for i in files:
        if i.endswith(".txt") and i != "classes.txt":
            # print(f"{root}\{i}")
            file = open(f"{root}/{i}", "r+")
            rfile = file.readlines()
            for j in range(len(rfile)):
                rfile[j] = rfile[j].split(" ")
                print(rfile[j])
                rfile[j][0] = "0"
                print(rfile[j])
                rfile[j] = " ".join(rfile[j])
                # rfile[j]=rfile[j]+"\n"
                print(rfile[j])
            print(rfile, ">>>>>>>>>>>")
            rfile = "".join(rfile)
            file.seek(0, 0)
            file.write(rfile)
            file.close()
    print('--------------------------------')
