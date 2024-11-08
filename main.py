
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


def add_to_dict(dict, *lists):
    for list in lists:
        for word in list:
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1

def parse_data(data, dict_pos, dict_neg):
    for i in range (len(data)):
        words_title  = [x.strip(",:“”!/\*?'. ()[]").lower() for x in data[i][0].split()]
        words_text = [x.strip(",:“”!/\*?'. ()[]").lower() for x in data[i][1].split()]
        if data[i][2] == 0:
            add_to_dict(dict_neg, words_title, words_text)
        else:
            add_to_dict(dict_pos, words_title, words_text)

if __name__ == '__main__':
    data = read_csv("Reddit_Combi.csv")
    # print(data[0])
    dict_pos = {}
    dict_neg = {}
    parse_data(data, dict_pos, dict_neg)
    print(dict_pos)

