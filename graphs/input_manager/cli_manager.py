from input_manager.input_manager import InputManager

class CLIManager(InputManager):
    def __init__(self):
        super(CLIManager, self).__init__()

    def get_input(self):
        self.vertices = self.get_vertex_input()
        self.edges = self.get_edges_input()
        self.start = self.get_start_input()
        self.end = self.get_end_input()
        return super().get_input()

    def get_vertex_input(self):
        res = input("Input number of vertices/nodes (2 or more): ")
        res = self.check_if_int(res)
        if res==-1:
            res = self.get_vertex_input()
        if res<2:
            print("Too few vertices/nodes. Input more")
            res = self.get_vertex_input()
        print(f"{res} vertices/nodes will be created from id 0 to {res-1}", end="\n\n")
        return res

    def get_edges_input(self):
        print("Provide edges/connections between vertices individually.")
        print(f"Format: 'from to' where 'from' and 'to' are integers from 0 to {self.vertices-1}")
        print("E.g. an input '0 1' connects the vertex(id=0) to the vertex(id=1)")
        print("To stop. Type 'q'")

        edges = []
        res = ''
        
        while True:
            res = input("Input: ")
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
                continue
            if not self.is_id_in_range(temp_list[0]) or not self.is_id_in_range(temp_list[1]):
                print(f"Id numbers are not in range 0 to {self.vertices-1}")
                continue
            edges.append(temp_list.copy())    
        return edges

    def get_start_input(self):
        res = input("Input start id: ")
        res = self.check_id(res)
        if res==-1:
            return self.get_start_input()
        return res

    def get_end_input(self):
        res = input("Input end id: ")
        res = self.check_id(res)
        if res==-1:
            return self.get_end_input()
        return res