Filtrarea Colaborativa:
-are la baza factorizarea matricilor
-ideea de baza: Un utilizator i-ar placea filmele apreciate de alti utilizatori cu gusturi asemanatoare cu ale lui
-abordare inversa fata de Filtrarea continutului
-folosim datele utilizatorilor pe care le avem (ratingurile filmelor vizionate) sa determinam criteriile (gen, actori etc), iar apoi sa facem previziuni
asupra ratingurilor lipsa (ale filmelor pe care un utilizator nu le-a vazut inca)

Metoda 1:
-transformam matricea cu date incomplete in doua matrici, printr-o factorizare aproximativa
-ratingurile din cele doua matrici sunt alese random
-cu ajutorul unei abordari de tip Machine Learning ratingurile generate random cresc sau scad, in functie de o eroare, calculata prin Metoda Gradientului 

Metoda 2:
-am comparat ratingurile filmelor pentru 2 cate 2 filme, pentru 2 cate 2 utilizatori (am comparat coloanele 2 cate 2 – doar pentru valorile
nenule(ratingurile pe care le avem)) pentru a putea calcula gradul de asemanare, prin folosirea functiei spatial.distance.cosine, functie care
calculeaza unghiul dintre 2 distante euclidiene 
-cu cat acest ungi este mai mic, cu atat distanta este mai mica, deci gradul de asemanare este mai mare si utilizatorul este mai probabil sa aibe
aceleasi preferinte cu utilizatorul cu care este comparat



###################
Collaborative Filtering:
-based on factorization of matrices
-basic idea: A user would like movies appreciated by other users with tastes similar to his
-inverse approach to Content Filtering
-we use the data of the users we have (ratings of the movies watched) to determine the criteria (genre, actors, etc.), and then to make predictions
on missing ratings (of movies that a user hasn't seen yet)

Method 1:
- we transform the matrix with incomplete data into two matrices, by an approximate factorization
-rates from the two matrices are chosen randomly
-with the help of a Machine Learning approach, randomly generated ratings increase or decrease, depending on an error, calculated by the Gradient Method

Method 2:
-I compared movie ratings for 2 by 2 movies, for 2 by 2 users (I compared 2 by 2 columns - only for values
(the ratings we have)) to be able to calculate the degree of similarity, by using the function spatial.distance.cosine, a function that
calculate the angle between 2 Euclidean distances
-the smaller this nail is, the shorter the distance, so the greater the degree of similarity and the more likely the user is to have
the same preferences as the user with whom it is compared
