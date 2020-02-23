import os
import shutil


class FileCommander():

    def _create_directory(self, dirName):
        os.mkdir(dirName)
        print(f'Folder "{dirName} created."')

    def _create_file(self, fileName):
        with open(fileName, "w") as f:
            print(f'File "{fileName}" created.')

    def _change_directory(self, newPath):
        os.chdir(newPath)
        print(f"Current directory: {os.path.abspath('')}")

    def _list_directories(self):
        print(f"Current directory: {os.path.abspath('')}")
        for data in os.scandir(""):
            icon = "📁" if data.is_dir() else "📄"
            print(f" {icon}  {data.name}")

    def _read_file(self, fileName):
        if os.path.isfile(fileName):
            file = open(fileName, "r")
            contents = file.read()
            print(contents)
        else:
            print(f'No such file "{fileName} in directory..."')

    def _delete_file(self, fileName):
        if os.path.isfile(fileName):
            os.remove(fileName)
            print(f'File "{fileName} deleted...')
        else:
            print(f'File "{fileName}" does not exist..')

    def _delete_directory(self, dirName):
        if os.path.exists(dirName):
            if len(os.listdir(dirName)) == 0:
                os.rmdir(dirName)
                print(f'Folder "{dirName}" deleted.')
            elif len(os.listdir(dirName)) != 0:
                print(f'Folder "{dirName}" is not empty! Are you sure you want to delete it?')
                choice = input('Type "y" to delete, "n" to quit: ')
                if choice == "y":
                    shutil.rmtree(dirName)
                    print(f'Folder "{dirName}" deleted.')
                else:
                    print(f'Folder "{dirName}" will not be deleted.')
        else:
            print(f'Folder "{dirName}" not found!')

    def _rename_file(self, fileName, newFileName):
        os.rename(fileName, newFileName)
        print(f'Old file "{fileName}" renamed to "{newFileName}"')

    def start(self):
        instr = ""
        print('Possible commands: \n"dir" - create directory \n"cd + dirname" - '
              'change directory \n"ls" - list directories \n"file + filename" - create file \n"cat + '
              'filename" - read file \n"delf + '
              'filename" - delete file \n"deld + folder name" - delete folder \n"ren + old filename, new filename" - '
              'rename a file \n"q" - quit')
        while instr != "q":
            instr = input("Enter command: ")
            if instr.startswith("dir"):
                self._create_directory(instr.split(" ")[1])
            elif instr.startswith("file"):
                self._create_file(instr.split(" ")[1])
            elif instr.startswith("cd"):
                self._change_directory(instr.split(" ")[1])
            elif instr.startswith("ls"):
                self._list_directories()
            elif instr.startswith('cat'):
                self._read_file(instr.split(" ")[1])
            elif instr.startswith('delf'):
                self._delete_file(instr.split(" ")[1])
            elif instr.startswith('deld'):
                self._delete_directory(instr.split(" ")[1])
            elif instr.startswith('ren'):
                self._rename_file(instr.split(" ")[1], instr.split(" ")[2])
            elif instr != "q":
                print(f"Unknown command: {instr}")
        print("Exiting app...")


commander = FileCommander()
commander.start()
