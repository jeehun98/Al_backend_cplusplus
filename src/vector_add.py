import os

os.add_dll_directory("C:\\msys64\\mingw64\\bin")

import vector_add

# 두 벡터를 정의합니다.
vec1 = [1, 2, 3]
vec2 = [4, 5, 6]

# C++에서 정의한 add_vectors 함수를 호출합니다.
result = vector_add.add_vectors(vec1, vec2)

print("Result of vector addition:", result)