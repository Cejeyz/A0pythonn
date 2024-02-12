import tarfile
import os.path

name_of_file = "A0.tar"

file = tarfile.open(name_of_file, "w")


file.add("C:/Users/foxhe/IdeaProjects/A0", arcname="A0")
file.add("C:/Users/foxhe/IdeaProjects/A0/a0.exe", arcname="a0.exe")
    #arcname=A0.exe)

file.close()