
def read_csv(file):
    data = []
    with open(file, "r", encoding='utf-8') as f:
        titles = f.readline().strip().replace('"', '').split(";")
        line = f.readline()
        while line:
            line = line.strip().replace('"', '').replace('.',' ').replace('/', ' ').replace('(', ' ').replace(')',' ').replace('…', ' ').replace('>', ' ').replace('*', ' ').replace(',', ' ').replace('<', ' ').replace('?', ' ').split(";")
            line.pop()
            line[2] = line[3]  # pt format
            line.pop()
            data.append(line)
            line = f.readline()
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
        words_title  = [x.strip(",:“”!/\*?'. ()[]_’‘-꒰⌯͒•̩̩̩́'ᴗ•̩̩̩̀⌯͒꒱↓~&—+{}").lower() for x in data[i][0].split()]
        words_text = [x.strip(",:“”!/\*?'. ()[]’_‘-꒰⌯͒•̩̩̩́'ᴗ•̩̩̩̀⌯͒꒱↓~&—+{}").lower() for x in data[i][1].split()]
        try:
            if int(data[i][2]) == 0:
                add_to_dict(dict_neg, words_title, words_text)
            else:
                add_to_dict(dict_pos, words_title, words_text)
        except:
            pass

if __name__ == '__main__':
    data = read_csv("Reddit_Combi.csv")
    # print(data[0])
    dict_pos = {}
    dict_neg = {}
    parse_data(data, dict_pos, dict_neg)
    #print(len(dict_pos))
    #print(len(dict_neg))

