import os , errno
from os import listdir
from os.path import isfile , join
import shutil

onlyfiles = [f for f in listdir("E:\Python_Laby\zadanie3") if isfile(join("E:\Python_Laby\zadanie3", f))]
print(onlyfiles)
# isfile(path) returns true if file does exist
ar = [];
#print(onlyfiles[0][0])

for f in onlyfiles:
    if (f[0] in ar) == False :
        ar.append(f[0])
        try:
            os.makedirs("../" + str(f[0]))
            try:
                save_path = "E:/Python_Laby/"
                os.path.join(save_path, str(f))
                shutil.copyfile("E:/Python_Laby/zadanie3/" + str(f),save_path + str(f[0]) + "/" + str(f) )

            except:
                pass

        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
    else:
        try:
            save_path = "E:/Python_Laby/"
            os.path.join(save_path, str(f))
            shutil.copyfile("E:/Python_Laby/zadanie3/" + str(f), save_path + str(f[0]) + "/" + str(f))

        #   os.path.join(save_path, str(f))
        except:
            print("E:/Python_Laby/zadanie3/" + str(f))
            print(save_path + str(f[0]))


