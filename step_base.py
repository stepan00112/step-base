def new(name):
    with open(name,'w') as f:
        f.write(str(base))
def reading(name):
    with open(name) as f:
        base=eval(f.read())
        return base

    
#base=[[[],[]],[[],[]]]
def new_base(row,column):
    global base
    base=[]
    for i in range(row):
        base.append([])
        p=base[i]
        for j in range(column):
            p.append([])
def plus_row(row):
    global base
    
    #base=[]
    lenning=len(base)
    column=len(base[0])
    for i in range(row):
        base.append([])
        p=base[i+lenning]
        for j in range(column):
           p.append([])
           

    #print(base)
def edit(row,column,data):
    base[row][column]=data
def edit_column(row,data):
    global base
    
    for j in range(len(data)):
        base[row][j]=data[j]
        


           
def edit(row,column,data):
    base[row][column]=data
def show_all():
    global base
    for i in base:
        for j in i:
            if j!=[]:
                print(j,end=' | ')
            else:
                print('None',end=' | ')
        print('\n-------------')
