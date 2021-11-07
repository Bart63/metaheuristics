class InputManager:
    def __init__(self):
        self.vertices = 0
        self.edges = []
        self.start = 0
        self.end = 0

    def input_to_dict(self):
        return vars(self)

    def get_input(self):
        return self.input_to_dict()

    def is_id_in_range(self, value):
        return value>=0 and value<self.vertices

    def check_if_int(self, value):
        try:
            res = int(value)
        except:
            print("Error while converting, try again")
            return -1
        return res

    def check_id(self, val):
        res = self.check_if_int(val)
        if res==-1:
            return -1
        if not self.is_id_in_range(res):
            print(f"Id out of range: from 0 to {self.vert_len-1}")
            return -1
        return res
