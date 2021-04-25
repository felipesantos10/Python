#Manipulando String
********************

#Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().

frase = 'curso em video python'

# A string "curso em video python" fica armazenado em um espaço na memoria(frase)
# Detro desse espaço da memoria, a stringtambém esta subdividida em pequenos pedações incluindo os espaços em branco.
# Observe que cada letra ocupa um pequeno espaço
# O campo 5,8,14 representa os espaços em branco.

*************************************************************************
[c][u][r][s][o]   [e][m]   [v] [i] [d] [e] [o]    [p] [y ][ t][h ][o ][ n]
[0][1][2][3][4][5][6][7][8][9][10][11][12][13][14][15][16][17][18][19][20]
**************************************************************************

Analise de String

#conta o comprimento da frase
len(frase)

#conta quanda vezes aparece a letra "o"
frase.count("o")

#conta quantas vezes ele encontrou o "deo"
frase.find('deo')

#Dentro da variavel frase existe a palavra curso
'curso' in frase

Transformação

#Sustituição, nesse caso ele trocaria python por android
frase.replace('python','android')

#coloca toda a string em letra maiuscula
frase.upper()

#coloca toda a string em letra minuscula
frase.lower()

#Coloca todas as letras em minusculo com excessão da primera.
frase.capitalize()

#Ver quantas palavras possuem a frase, e coloca em maiusculo o inicio de cada uma delas
frase.title()

#Remove todos os espaçõs inuteis no inicio e no final da frase
frase.strip()

#Os espaços do lado direito são removidos
frase.rstrip()

#Remove os espaços da esquerda
frase.lstrip()

Divisão

#Ocorre uma divisão dentro da string considerando os espaços
#Divide uma string em uma lista
frase.split()
[c][u][r][s][o]   [e][m]   [v][i][d][e][o]    [p][y][t][h][o][n]
[0][1][2][3][4]   [0][1]   [0][1][2][3][4]    [0][1][2][3][4][5]

Junção
#juntar todos os elementos de frase e separa por "-"
'-'.jon(frase)