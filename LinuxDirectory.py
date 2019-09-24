from Directory import *
class Error(Exception):
    def __str__(self):
        return "Invalid opertation"

class LinuxDirectory(Error):
    def __init__(self):
        self.root=Directory()

    def childNode(self, path):
        dirList = path.split('/')
        childNode = dirList[-1]
        return childNode

    def dirTraveral(self, path):
        dirList=path.split("/")
        directory = self.root
        for dir in dirList[1:-1]:
            child=directory.child
            if dir in child.keys():
                directory = child[dir]
            if dir != directory.name:
                break
        try:
            if dirList[-2] != directory.name:
                raise Error
            return directory
        except Error as e:
            print(e)
            return False

    def createDirectory(self,path):
        location=self.dirTraveral(path)
        if location is False:
            return ((path,False))
        name=self.childNode(path)
        location.child[name]=Directory(name)
        return ((path,True))

    def recursiveTravel(self,node,str,list):
        if node.name == str:
            for x in list:
                print(' /', x, end='')
            print()
        for child in node.child.values():
                list.append(child.name)
                self.recursiveTravel(child,str,list)
                list.pop()


    def pathSearch(self,path,endStr):
        result=self.endPath(path)
        directory=result[0]
        listPaths=[]
        self.recursiveTravel(directory,endStr,listPaths)





    def createFile(self,path):
        try:
            location=self.dirTraveral(path)
            if location is False:
                return ((path,False))
            if location.is_file is True:
                raise Error
            name=self.childNode(path)
            location.child[name]=Directory(name,True)
            return ((path,True))
        except Error as e:
            print(e)
            return ((path,False))

    def checkPath(self,path):
        result= self.endPath(path)

        if result[1]==True:
            return ((path,True))
        else:
            return ((path,False))

    def endPath(self,path):
        dirList = path.split("/")
        directory = self.root
        for dir in dirList[1:]:
            child = directory.child
            if dir in child.keys():
                directory = child[dir]
            if dir != directory.name:
                break
        try:
            if dirList[-1] != directory.name:
                raise Error
            return ((directory,True))
        except Error as e:
            print(e)
            return ((path,False))

    def listDir(self,path):
        result=self.endPath(path)
        if result[1] == True:
            directory=result[0]
            Dict={'file':[],'Directory':[]}
            for child in directory.child.values():
                if child.is_file == True:
                    Dict['file'].append(child.name)
                else:
                    Dict['Directory'].append(child.name)
            return Dict


obj=LinuxDirectory()
print(obj.createDirectory("/a"))
print(obj.createDirectory("/a/b"))
print(obj.createDirectory("/a/c"))
print(obj.createDirectory("/a/d"))
print(obj.createDirectory("/a/b/e"))
print(obj.createDirectory("/a/b/f"))
print(obj.createDirectory("/a/b/g"))
print(obj.createDirectory("/a/b/e/h"))
print(obj.createDirectory("/a/b/e/i"))
print(obj.createDirectory("/a/b/e/j"))
(obj.pathSearch("/a","j"))