# cx_freeze example




import sys
from cx_Freeze import setup, Executable

setup(
    options={'build.exe': {'include_files': ['Utilities.ico']}},
    name = "test",
    version = "0.1",
    description = "test",
    executables = [Executable("test.py", base = "Win32GUI", icon='Utilities.ico')])


#Console :
#python setup.py bdist_msi   # 실행 파일 만들기
#python setup.py build    # Exe 만들기
