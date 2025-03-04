from abc import ABC, abstractmethod
import numpy as np
class LinearProgramming(ABC):
    
    @abstractmethod
    def create_table(self):
        pass
    
    @abstractmethod
    def variable_in_out(table:np.ndarray):
        pass
    
    @abstractmethod
    def solve_table(self, table:np.ndarray, enter_the_base, leave_the_base):
        pass

    def run(self):
        self.table = self.__create_table()
        in_base, out_base = self.variable_in_out(self.table)
        
        
        