# Clasificator Bayes multinomial

Într-o lume în care rata depresiei și a altor afecțiuni emoționale sunt în continuă creștere, e important să fim constant atenți la sentimentele și semnalele pe care cei din jur ni le oferă. De cele mai multe ori, comunicarea se desfășoară pe rețelele de socializare, astfel încât, postările sau mesajele trimise pe acestea ajung să ascundă adevărate strigăte de ajutor.

Acest proiect implementează un clasificator Bayes multinomial, care primește un dataset de antrenament (Reddit_Combi.csv) cu titlul și textul unor postări de pe Reddit, în limba engleză, urmate de un label, cu următoarea semnificație: 1 - True, 0 - False. Ulterior, primește un dataset de test (database.csv) și clasifică mesajele pe baza concluziilor trase în urma prelucrării dataset-ului de antrenament.

Pe datele utilizate de noi, clasificatorul reușește cu o acuratețe de 82.14% să identifice dacă autorul unei postări de pe Reddit prezintă sentimente negative, semne de anxietate sau depresie.

## Formatul datelor

În fișierele .csv, fiecare linie va reprezenta o postare sub forma _title;body;Body Title;label;_ 

## Funcții folosite

În cadrul proiectului sunt folosite următoarele funcții:

- read_csv (file)

Returnează obiectul data asociat fișierului .csv de forma title;body;Body Title;label; eliminând coloana _Body Title_ și spațiile de la final.

- *_parse_data (file, dict_pos, dict_neg)_*

Se parcurge dataset-ul de antrenament și în funcție de label-ul mesajului curent (1 sau 0) cuvintele acestuia se introduc într-un dicționar: *_dict_pos_* - dacă label-ul e 1, *_dict_neg_* - în caz contrar. De asemenea, se numără câte mesaje din setul de antrenament sunt marcate cu 1 (*_no_msg_pos_*) și câte cu 0 (*_no_msg_neg_*), ca ulterior să se facă raportarea la numărul total de mesaje (*_no_msg_total_*) pe care a fost antrenat și a se calcula probabilitățile apriori ca o postare să aibă label-ul 1, respectiv 0.

- *_prob_word (dict)_*

Pentru fiecare cuvânt word din dicționar se calculează probabilitatea acestuia ca fiind numărul său de apariții / numărul total de apariții ale cuvintelor din dict și rezultatul obținut i se atribuie lui *_dict[word]_*. Astfel, după apelul funcției *_prob_word (dict_pos)_*, *_dict[word]_* va reprezenta probabilitatea condiționată a lui word de a apărea într-o postare cu label-ul 1, *_P [word | Pos]_*. Analog pentru prob_word (dict_neg).

Funcția va returna numărul total de apariții ale cuvintelor din dict: *_no_words_pos_*, respectiv *_no_words_neg_*.

- *_testing (file, dict_pos, dict_neg, no_words_pos, no_words_neg)_*

Pentru un fișier dat și pe baza rezultatelor calculate anterior, funcția ia fiecare postare din file și îi pune acesteia un label. Pentru fiecare postare se iau în calcul cele două variante: la o primă vedere, fără a analiza conținutul ei, postarea poate avea:

Label-ul 1, cu probabilitatea *_P(Pos)_* = no_msg_pos / no_msg_total
Label-ul 0, cu probabilitatea *_P(Neg)_* = no_msg_neg / no_msd_total

Se parcurg cuvintele acesteia și probabilitatea de a i se atribui un anumit label este influențată de probabilitatea condiționată a cuvântului respectiv a apărea în mesajele cu label-ul respectiv: *_dict_pos[word] / dict_neg[word]_*.

În final, postării i se atribuie label-ul a cărui probabilitate e mai mare și se compară cu label-ul de facto pentru a măsura acuratețea.

## Resurse

- Dataset: https://www.kaggle.com/datasets/mexwell/stress-detection-from-social-media-articles

- Naive Bayes Classifier: https://www.youtube.com/watch?v=O2L2Uv9pdDA

## Instrucțiuni de utilizare

Se descarcă codul din fișierul main.py și dataset-ul de antrenament. Apoi se creează un nou fișier cu aceeași structură ca dataset-ul de antrenament și se rulează programul într-un editor de text ce are acces la un interpretor Python. Exemple de astfel de fișiere sunt Reddit_Combi.csv și database.csv.

 
