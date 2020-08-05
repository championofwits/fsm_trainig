class state_machine :
    def __init__(self,states_functions):
        r = 0
        self.arr =[]
        for j in states_functions :
            r = r + 1
            self.arr.append(state(r,j))

    def printall(self):
        for i in range(len(self.arr)):
            print(self.arr[i-1].name ,self.arr[i-1].funct)

    def run_engine(self,start,check,inpp):
        self.current = start
        for i in inpp :
            self.current = self.arr[self.current-1].feed_input(i)
        self.output = self.current
        if (self.output == check):
            return True
        else :
            return False

class state :
    def __init__(self,n,functionss):
        self.name = n
        self.funct = functionss  
    def feed_input(self,inp):
        return self.funct[inp]



num_inp = 5
inpp = [1,0,0,0,1]

function_l = [{0:2,1:2},{0:1,1:1},{0:3,1:4},{0:1,1:2},{0:2,1:2}]

f1 = state_machine(function_l)
f1.printall()
f1.run_engine(1,2,inpp)
print(f1.output)
