# Clasificator Bayes multinomial

Într-o lume în care rata depresiei și a altor afecțiuni emoționale sunt în continuă creștere, e important să fim constant atenți la sentimentele și semnalele pe care cei din jur ni le oferă. De cele mai multe ori, comunicarea se desfășoară pe rețelele de socializare, astfel încât, postările sau mesajele trimise pe acestea ajung să ascundă adevărate strigăte de ajutor.

Acest proiect implementează un clasificator Bayes multinomial, care primește un dataset de antrenament (Reddit_Combi.csv) cu titlul și textul unor postări de pe Reddit, în limba engleză, urmate de un label, cu următoarea semnificație: 1 - True, 0 - False. Ulterior, primește un dataset de test (database.csv) și clasifică mesajele pe baza concluziilor trase în urma prelucrării dataset-ului de antrenament.

Pe datele utilizate de noi, clasificatorul reușește cu o acuratețe de 82.14% să identifice dacă autorul unei postări de pe Reddit prezintă sentimente negative, semne de anxietate sau depresie.

## Formatul datelor

În fișierele .csv, fiecare linie va reprezenta o postare sub forma title;body;Body Title;label; 

## Funcții folosite

În cadrul proiectului sunt folosite următoarele funcții:

read_csv (file)

Returnează obiectul data asociat fișierului .csv de forma title;body;Body Title;label;, eliminând coloana Body Title și spațiile de la final.

parse_data (file, dict_pos, dict_neg)

Se parcurge dataset-ul de antrenament și în funcție de label-ul mesajului curent (1 sau 0) cuvintele acestuia se introduc într-un dicționar: dict_pos - dacă label-ul e 1, dict_neg - în caz contrar. De asemenea, se numără câte mesaje din setul de antrenament sunt marcate cu 1 (no_msg_pos) și câte cu 0 (no_msg_neg), ca ulterior să se facă raportarea la numărul total de mesaje (no_msg_total) pe care a fost antrenat și a se calcula probabilitățile apriori ca o postare să aibă label-ul 1, respectiv 0.

prob_word (dict)

Pentru fiecare cuvânt word din dicționar se calculează probabilitatea acestuia ca fiind numărul său de apariții / numărul total de apariții ale cuvintelor din dict și rezultatul obținut i se atribuie lui dict[word]. Astfel, după apelul funcției prob_word (dict_pos), dict[word] va reprezenta probabilitatea condiționată a lui word de a apărea într-o postare cu label-ul 1, P [word | Pos]. Analog pentru prob_word (dict_neg).

Funcția va returna numărul total de apariții ale cuvintelor din dict: no_words_pos, respectiv no_words_neg.

testing (file, dict_pos, dict_neg, no_words_pos, no_words_neg)

Pentru un fișier dat și pe baza rezultatelor calculate anterior, funcția ia fiecare postare din file și îi pune acesteia un label. Pentru fiecare postare se iau în calcul cele două variante: la o primă vedere, fără a analiza conținutul ei, postarea poate avea:

Label-ul 1, cu probabilitatea P(Pos) = no_msg_pos / no_msg_total
Label-ul 0, cu probabilitatea P(Neg) = no_msg_neg / no_msd_total

Se parcurg cuvintele acesteia și probabilitatea de a i se atribui un anumit label este influențată de probabilitatea condiționată a cuvântului respectiv a apărea în mesajele cu label-ul respectiv: dict_pos[word] / dict_neg[word].

În final, postării i se atribuie label-ul a cărui probabilitate e mai mare și se compară cu label-ul de facto pentru a măsura acuratețea.

## Resurse

Dataset: https://www.kaggle.com/datasets/mexwell/stress-detection-from-social-media-articles

Naive Bayes Classifier: https://www.youtube.com/watch?v=O2L2Uv9pdDA

## Instrucțiuni de utilizare

Se descarcă codul din fișierul main.py și dataset-ul de antrenament. Apoi se creează un nou fișier cu aceeași structură ca dataset-ul de antrenament și se rulează programul într-un editor de text ce are acces la un interpretor Python. Exemple de astfel de fișiere sunt Reddit_Combi.csv și database.csv.

 
	
