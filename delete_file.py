import os
file_path = "hello.txt"

#kembangin:kalo file nya ada hapus, kalo filenya gaada yaudah
if os.path.exists(file_path):
    os.remove(file_path)
    print("File {} has been deleted" . format(file_path))
else:
    print("file doesnt exist")

#ini akan digunakan dalam final project