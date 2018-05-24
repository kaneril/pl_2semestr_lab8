from random import seed, randint

class Matrix:
    def __init__(self, rows, columns=None, elements=None):
        
        def verificateListNumericData(elements):
            for i in elements:
                try: float(i)
                except ValueError: return False
            return True

        def verificateMatrixData(rows, columns, elements):
            if (str(rows).isdecimal()==False):
                return False
            if ((columns!=None) and (str(columns).isdecimal()==False)):
                return False
            if (columns==None):
                columns=rows
            if ((elements!=None) and ((len(elements)!=(int(rows)*int(columns))) or (verificateListNumericData(elements)==False))):
                return False
            return True

        if (verificateMatrixData(rows, columns, elements)==True):
            self.rows=rows
            if (columns==None):
                self.columns=rows
            else: self.columns=columns
            if (elements==None):
                seed()
                self.elements=[randint(-10,10) for i in range (self.rows*self.columns)]
            else:self.elements=elements
        else: 
            print('Ошибка ввода данных')
            self.rows=None
            self.columns=None
            self.elements=None

    def __add__(self, other):
        if (type(other) is Matrix): 
            if ((self.rows!=other.rows) or (self.columns!=other.columns)):
                print('Нельзя складывать матрицы разных размерностей')
                return None
            else:
                newElements=[]
                for i in range(self.rows*self.columns):
                    newElements.append(self.elements[i]+other.elements[i])
            return Matrix(self.rows,self.columns,newElements)
        else: 
            if ((type(other) is float) or (type(other) is int)):
                newElements=[]
                for i in range(self.rows*self.columns):
                    newElements.append(self.elements[i]+other)
                return Matrix(self.rows,self.columns,newElements)
            else: 
                print('Матрицу можно складывать только с матрицей или числом')
                return None

    def __sub__(self, other):
        if (type(other) is Matrix): 
            if ((self.rows!=other.rows) or (self.columns!=other.columns)):
                print('Нельзя вычитать матрицы разных размерностей')
                return None
            else:
                newElements=[]
                for i in range(self.rows*self.columns):
                    newElements.append(self.elements[i]-other.elements[i])
            return Matrix(self.rows,self.columns,newElements)
        else: 
            if ((type(other) is float) or (type(other) is int)):
                newElements=[]
                for i in range(self.rows*self.columns):
                    newElements.append(self.elements[i]-other)
                return Matrix(self.rows,self.columns,newElements)
            else: 
                print('Из матрицы можно вычитать только матрицу или число')
                return None

    def __mul__(self, other):
        if (type(other) is Matrix): 
            if (self.columns!=other.rows):
                print('Операция умножения двух матриц выполнима только в том случае, если число столбцов в первом сомножителе равно числу строк во втором')
                return None
            else:
                newElements=[]
                for i in range(self.rows):
                    for j in range(other.columns):
                        element=0
                        for k in range(self.columns):
                            element+=self.elements[i*self.columns+k]*other.elements[k*other.columns+j]
                        newElements.append(element)
            return Matrix(self.rows,other.columns,newElements)
        else: 
            if ((type(other) is float) or (type(other) is int)):
                newElements=[]
                for i in range(self.rows*self.columns):
                    newElements.append(self.elements[i]*other)
                return Matrix(self.rows,self.columns,newElements)
            else:
                print('Матрицу можно умножить только на матрицу или число')
                return None

    def __repr__(self):
        if (self.elements==None):
            return('None')
        else:
            string=''
            for  i in range(len(self.elements)):
                string=string+str('{0:6.2f}'.format(self.elements[i]))+' '
                if (((i+1)%self.columns)==0):
                    string=string+'\n'
            return string

    def transpose(self):
        newElements=[]
        for i in range(self.columns):
            for j in range(self.rows):
                newElements.append(self.elements[j*self.columns+i])
        return Matrix(self.columns,self.rows,newElements)   

    def determinate(self):
        if (self.columns!=self.rows):
            print('Определитель можно вычислить только для квадратной матрицы')
            return None
        else: 
            if (self.columns==1):
                return (self.elements[0])
            else:
                deter=0
                for i in range(self.columns):
                    newElements=[]
                    for j in range(1,self.rows):
                        newElements=newElements+self.elements[(j*self.columns):(j*self.columns+i)]+self.elements[(j*self.columns+i+1):((j+1)*self.columns)]
                    deter=deter+(pow(-1,i)*self.elements[i]*(Matrix((self.columns-1),(self.rows-1),newElements)).determinate())
                return(deter)   
                
   
if __name__ == "__main__":
    a=Matrix(3,2,[0,1,2,3,4,5])
    print(a)
    a=Matrix(2,elements=[0,1,2,3])
    print(a)
    a=Matrix(2)
    print(a)
    a=Matrix(-2)
    print(a)
    a=Matrix(2,-2)
    print(a)
    a=Matrix(2.3)
    print(a)
    a=Matrix(2,3,[0,1])
    print(a)
    a=Matrix(2,1,[-3.1,0,0,0])
    print(a)
    a=Matrix(2)
    print(a)
    b=Matrix(2)
    print(b)
    c=a+b
    print(c)
    c=c+2
    print(c)
    a=Matrix(2,2,[0,1,2,3])
    print(a)
    b=Matrix(2,3,[0,1,2,3,4,5])
    print(b)
    c=a*b
    print(c)
    c=a*2
    print(c)
    c=Matrix(2)
    print(c)
    print(c)
    
