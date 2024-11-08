
def read_csv(file):
    data = []
    f=open(file,"r",encoding='utf-8')
    titles = f.readline().strip().split(";")
    line=f.readline()
    while line:
        line = line.strip().split(";")
        line.pop()
        line[2]=line[3] #pt format
        line.pop()
        data.append(line)
        line=f.readline()
    return data

if __name__ == '__main__':
    data = read_csv("Reddit_Combi.csv")
    print(data[0][0])