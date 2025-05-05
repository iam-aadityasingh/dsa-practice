def addBinary(self, a: str, b: str) -> str:
        def binary_add(a, b):
            num1 = int(a, 2)
            num2 = int(b, 2)
            
            total = num1 + num2
            
            total_bin = bin(total)[2:] 
            
            return total_bin
        return binary_add(a,b)
