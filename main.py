
import random

class Matrix:
    
    def __init__(self):    # 開機自動程式執行初始化
        
        Ax = input("Enter A matrix's rows:")
        Ay = input("Enter A matrix's cols:") 

        self.Ax = Ax
        self.Ay = Ay 
        
        matrix_A = [[random.randint(0, 9) for _ in range(int(Ay))] for _ in range(int(Ax))]  #宣告亂數0..9 3*3 陣列     需加(int)將字串轉為數字
        self.matrix_A = matrix_A    # self.matrix_B = matrix_A   #這樣用A,B內容會一樣

        print('Matrix A(' + (self.Ax) + ',' + (self.Ay) + '):')  #字串與物件用(+)連接
        for i in self.matrix_A:
            for j in i:
                print(j, end = ' ')
            print('')
        print('')    
        # M.display_1()
        
        Bx = input("Enter B matrix's rows:")
        By = input("Enter B matrix's cols:")  
        
        self.Bx = Bx
        self.By = By 
        
        matrix_B = [[random.randint(0, 9) for _ in range(int(By))] for _ in range(int(Bx))]
        self.matrix_B = matrix_B
       
        print('Matrix B(' + (self.Bx) + ',' + (self.By) + '):')
        for i in self.matrix_B: 
            for j in i:
                print(j, end = ' ')
            print('')
        print('')
        # M.display_2()

        matrix_C = [[0 for _ in range(int(Ay))] for _ in range(int(Ax))]  #add結果
        self.matrix_C = matrix_C

        matrix_C1 = [[0 for _ in range(int(Ay))] for _ in range(int(Ax))]  #sub結果 
        self.matrix_C1 = matrix_C1

        matrix_C2 = [[0 for _ in range(int(Ay))] for _ in range(int(Bx))]  #mul結果
        self.matrix_C2 = matrix_C2
 
        matrix_T = [[0 for _ in range(int(Ay))] for _ in range(int(Bx))]  #transpose結果
        self.matrix_T = matrix_T
    
    def add(self):

        for i in range(int(self.Ax)):
            for j in range(int(self.Ay)):
                self.matrix_C[i][j] = self.matrix_A[i][j] + self.matrix_B[i][j]
        #print(self.matrix_C)
        print('========== A + B ==========')
        for i in self.matrix_C:
            for j in i:
                print(j, end = ' ')  # end = ' ' , ''裡多加一格, 數字之間會空格
            print('')                # '' 換行 : 每三個數字換一行，\n 會多換一行 
        print('')                    # 顯示後, 矩陣A 與 === A-B === 間多一行
        return self.matrix_C
        
    
    def sub(self):
        for i in range(int(self.Bx)):
            for j in range(int(self.By)):
                self.matrix_C1[i][j] = self.matrix_A[i][j] - self.matrix_B[i][j]
        #print(self.matrix_C1)
        
        print('========== A - B ==========')
        for i in self.matrix_C1:
            for j in i:
                print(j, end = ' ')
            print('')
        print('')    
        return self.matrix_C1
      
    
    def mul(self):   
        # 
        # 2*2 矩陣分析:
        #    
        #   i  k    k  j      i  k    k  j       i  k    k  j      i  k    k  j
        # A[0, 0]*B[0, 0] + A[0, 1]*B[1, 0]    A[0, 0]*B[0, 1] + A[0, 1]*B[1, 1]
        # A[1, 0]*B[0, 0] + A[1, 1]*B[1, 0]    A[1, 0]*B[0, 1] + A[1, 1]*B[1, 1] 
        
        result = []
        for i in range(int(self.Ax)):                       
            row = []                                                  
            for j in range(int(self.Ay)):
                list_sum = []
                for k in range(int(self.Ax)):
                    list_sum += [self.matrix_A[i][k] * self.matrix_B[k][j]]
                row += [sum(list_sum)]
            result += [row]
            # return result


        print('========== A * B ==========')
        self.matrix_C2 = result
        for i in self.matrix_C2:
            for j in i:
                print(j, end = ' ')
            print('')
        print('')    
        return self.matrix_C2


    def transpose(self):    
        for i in range(int(self.Ax)):
            for j in range(int(self.Ay)):
                self.matrix_T[i][j] = self.matrix_C2[j][i]
        #print(self.matrix_T)
        print('===== the transpose of A*B =====')
        for i in self.matrix_T:
            for j in i:
                print(j, end = ' ')
            print('')
        print('')    
        return self.matrix_T
    
    #  def display_1(self,matrix_A ):    需移至上面
    #      print('Matrix A(, ):')
    #      for i in self.matrix_A:
    #          for j in i:
    #              print(j, end = ' ')
    #          print('')
    #      print('')    
    #      return
        
    # def display_2(self):               需移至上面
    #     print('Matrix B(, ):')
    #     for i in self.matrix_B: 
    #         for j in i:
    #             print(j, end = ' ')
    #         print('')
    #     print('')
    #     return

M = Matrix()
# M.display_1()
# M.display_2()
M.add()
M.sub()
M.mul()
M.transpose()


