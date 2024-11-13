import numpy as np

offset = 26     #pentru a evita underflow-ul/overflow-ul

def read_csv(file):
    data = []
    with open(file, "r", encoding='utf-8') as f:
        titles = f.readline().strip().replace('"', '').split(";")   #n am nevoie de titluri
        line = f.readline()
        unwantedchars = "'", '"', '.', '/', '(', ')', '…', '>', '*', ',', '<', '?'
        while line:
            for c in unwantedchars:
                line = line.replace(c, ' ')
            line = line.strip().split(";")
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
                dict[word] = 2

def parse_data(data, dict_pos, dict_neg):
    global no_msg_pos, no_msg_neg, no_msg_total
    weirdhumanchars = ",*:“”!/?'. ()[]_’‘-꒰⌯͒•̩̩̩́'ᴗ•̩̩̩̀⌯͒꒱↓~&—+{\\}"
    for i in range (len(data)):
        words_title = [x.strip(weirdhumanchars).lower() for x in data[i][0].split()]
        words_text = [x.strip(weirdhumanchars).lower() for x in data[i][1].split()]

        #din cauza fisierului de intrare, am facut o exceptie pentru ca avem uneori caractere care nu ar trebui sa fie acolo inainte de separator
        try:
            if int(data[i][2]) == 0:
                add_to_dict(dict_neg, words_title, words_text)
                no_msg_neg += 1
            else:
                add_to_dict(dict_pos, words_title, words_text)
                no_msg_pos += 1
            no_msg_total += 1
        except:
            pass


def prob_word(dict):
    no_words = sum(dict.values())
    for key in dict.keys():
        dict[key] = np.float64(dict[key] / no_words) * offset
    return no_words

def testing(file, dict_pos, dict_neg, no_words_pos, no_words_neg):
    global no_msg_pos, no_msg_neg, no_msg_total
    data = read_csv(file)
    nrcorecte = 0
    weirdhumanchars = ",*:“”!/?'. ()[]_’‘-꒰⌯͒•̩̩̩́'ᴗ•̩̩̩̀⌯͒꒱↓~&—+{\\}"
    for i in range (len(data)):
        words_title = [x.strip(weirdhumanchars).lower() for x in data[i][0].split()]
        words_text = [x.strip(weirdhumanchars).lower() for x in data[i][1].split()]
        prob_pos = np.float64(no_msg_pos / no_msg_total) * offset
        prob_neg = np.float64(no_msg_neg / no_msg_total) * offset
        for word in words_title:
            if word not in dict_pos:
                dict_pos[word] = np.float64(1 / no_words_pos) * offset
            if word not in dict_neg:
                dict_neg[word] = np.float64(1 / no_words_neg) * offset
            prob_pos = np.float64(prob_pos * dict_pos[word]) * offset
            prob_neg = np.float64(prob_neg * dict_neg[word]) * offset
        for word in words_text:
            if word not in dict_pos:
                dict_pos[word] = np.float64(1 / no_words_pos) * offset
            if word not in dict_neg:
                dict_neg[word] = np.float64(1 / no_words_neg) * offset
            prob_pos = np.float64(prob_pos * dict_pos[word]) * offset
            prob_neg = np.float64(prob_neg * dict_neg[word]) * offset
        ans = prob_pos > prob_neg

        #din cauza fisierului de intrare, am facut o exceptie pentru ca avem uneori caractere care nu ar trebui sa fie acolo inainte de separator
        try:
            nrcorecte += (ans == int(data[i][2]))
        except:
            pass
    return nrcorecte/len(data)

if __name__ == '__main__':

    data = read_csv("Reddit_Combi.csv")
    dict_pos = {}
    dict_neg = {}
    no_msg_pos = no_msg_neg = no_msg_total = 0
    parse_data(data, dict_pos, dict_neg)
    no_words_pos = prob_word(dict_pos)
    no_words_neg = prob_word(dict_neg)
    print(f'Acuratetea modelului este {testing("database.csv", dict_pos, dict_neg, no_words_pos, no_words_neg) * 100}%')