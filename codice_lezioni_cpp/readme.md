## If you use CodeBlocks

- Copy main.cbp into a subfolder
- Open the new cbp file with CodeBlocks
- Add all other cpp and h files to the project
  (Menu: Project - Add files recursively)
- Menu: Settings - Compiler - Follow C++14 standard

## If you use Geany

- Menu: Set build commands - Build
- g++ -std=c++14 -Wall -o "%e" *.cpp

## Create a Python module in Windows

- Execute getswigwin.py
- Copy cpp2py.bat into a subfolder
- Execute the copied bat file (double click)

## Create a Python module in Linux

- Open the subfolder in Terminal
- sudo apt install swig
- ../cpp2py.sh

