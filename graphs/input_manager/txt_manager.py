from ntpath import realpath
from input_manager.input_manager import InputManager
from os import listdir
from os.path import join, dirname, realpath, isfile

class TXTManager(InputManager):
    def __init__(self):
        super(TXTManager, self).__init__()
        self.input_path = join(dirname(dirname(realpath(__file__))), 'input')

    def get_input(self):
        self.filename = self.choosefile()
        path = join(self.input_path, self.filename)
        self.file = open(path)
        self.vertices = self.get_vertex_input()
        self.edges = self.get_edges_input()
        self.start = self.get_start_input()
        self.end = self.get_end_input()
        self.file.close()
        return super().get_input()

    def choosefile(self):
        txtfiles = [
            filename 
            for filename in listdir(self.input_path) 
            if isfile(join(self.input_path, filename))
                and filename.endswith('.txt')
        ]
        while True:
            print('Select file: ')
            for i, filename in enumerate(txtfiles):
                print(f"{i+1}. {filename}")
            choice = input("Choice: ")
            choice = self.check_if_int(choice)
            if choice == -1:
                continue
            if choice>0 or choice<=len(txtfiles):
                return txtfiles[choice-1]
            print("Wrong number")

    def readline(self):
        res = self.file.readline()
        if res[-1] == '\n':
            res = res[:-1]
        return res

    def get_vertex_input(self):
        res = self.readline()
        res = self.check_if_int(res)
        if res==-1:
            quit()
        if res<2:
            print("Too few vertices/nodes. Input more")
            quit()
        print(f"{res} vertices/nodes will be created from id 0 to {res-1}", end="\n\n")
        return res

    def get_edges_input(self):
        edges = []
        res = ''
        
        while True:
            res = self.readline()
            if res == "q":
                break
            temp_list = []
            try:
                temp_list = list(map(int, res.split()))
            except:
                print("Error while converting, try again")
                continue
            if len(temp_list)!=2:
                print("Wrong number of integers")
                quit()
                continue
            if not self.is_id_in_range(temp_list[0]) or not self.is_id_in_range(temp_list[1]):
                print(f"Id numbers are not in range 0 to {self.vertices-1}")
                continue
            edges.append(temp_list.copy())    
        return edges

    def get_start_input(self):
        res = self.readline()
        res = self.check_id(res)
        if res==-1:
            quit()
        return res

    def get_end_input(self):
        res = self.readline()
        res = self.check_id(res)
        if res==-1:
            quit()
        return res