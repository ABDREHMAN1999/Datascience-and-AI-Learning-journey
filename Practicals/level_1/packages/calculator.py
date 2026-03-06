##calculator code 
import time
class claculator:
    def __init__(self):
        print("This is a calculator functionality")
        self.__history = []
       
    def add(self, *args):
        total = 0
        for i in args:
            total = total + i
        t1 = time.time()
        self.__history.append(f"add{t1:2f}: args({args} total = {total})")
        return total
    
    def get_history(self):
        return self.__history
     
     
    
    
    
    
    
    
    
    
    
    
                