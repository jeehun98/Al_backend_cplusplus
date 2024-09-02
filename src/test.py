import ctypes
import os

try:
    # vector_add.pyd의 절대 경로를 명시합니다.
    dll_path = r"c:\Users\owner\Desktop\Al_backend_cplusplus\src\vector_add.pyd"
    ctypes.CDLL(dll_path)
    print("DLL loaded successfully.")
except OSError as e:
    print("Failed to load DLL:", e)
