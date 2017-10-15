import operator, os, sys
import time
import numpy as np
from mpi4py import MPI
comm = MPI.COMM_WORLD
root = 0

words2ignore = ["a", "able", "about", "above", "according", "accordingly", "across", "actually", "after",
                "afterwards", "again", "against", "all", "allow", "allows", "almost", "alone", "along",
                "already", "also", "although", "always", "am", "among", "amongst", "an", "and", "another",
                "any", "anybody", "anyhow", "anyone", "anything", "anyway", "anyways", "anywhere", "apart",
                "appear", "appreciate", "appropriate", "are", "around", "as", "aside", "ask", "asking",
                "associated", "at", "available", "away", "awfully", "b", "be", "became", "because", "become",
                "becomes", "becoming", "been", "before", "beforehand", "behind", "being", "believe", "below",
                "beside", "besides", "best", "better", "between", "beyond", "both", "brief", "but", "by", "c",
                "came", "can", "cannot", "cant", "cause", "causes", "certain", "certainly", "changes",
                "clearly", "co", "com", "come", "comes", "concerning", "consequently", "consider",
                "considering", "contain", "containing", "contains", "corresponding", "could", "course",
                "currently", "d", "definitely", "described", "despite", "did", "different", "do", "does",
                "doing", "done", "down", "downwards", "during", "e", "each", "edu", "eg", "eight", "either",
                "else", "elsewhere", "enough", "entirely", "especially", "et", "etc", "even", "ever", "every",
                "everybody", "everyone", "everything", "everywhere", "ex", "exactly", "example", "except", "f",
                "far", "few", "fifth", "first", "five", "followed", "following", "follows", "for", "former",
                "formerly", "forth", "four", "from", "further", "furthermore", "g", "get", "gets", "getting",
                "given", "gives", "go", "goes", "going", "gone", "got", "gotten", "greetings", "h", "had",
                "happens", "hardly", "has", "have", "having", "he", "hello", "help", "hence", "her", "here",
                "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "hi", "him", "himself", "his",
                "hither", "hopefully", "how", "howbeit", "however", "i", "ie", "if", "ignored", "immediate",
                "in", "inasmuch", "inc", "indeed", "indicate", "indicated", "indicates", "inner", "insofar",
                "instead", "into", "inward", "is", "it", "its", "itself", "j", "just", "k", "keep", "keeps",
                "kept", "know", "knows", "known", "l", "last", "lately", "later", "latter", "latterly",
                "least", "less", "lest", "let", "like", "liked", "likely", "little", "ll", "look", "looking",
                "looks", "ltd", "m", "mainly", "many", "may", "maybe", "me", "mean", "meanwhile", "merely",
                "might", "more", "moreover", "most", "mostly", "much", "must", "my", "myself", "n", "name",
                "namely", "nd", "near", "nearly", "necessary", "need", "needs", "neither", "never",
                "nevertheless", "new", "next", "nine", "no", "nobody", "non", "none", "noone", "nor",
                "normally", "not", "nothing", "novel", "now", "nowhere", "o", "obviously", "of", "off",
                "often", "oh", "ok", "okay", "old", "on", "once", "one", "ones", "only", "onto", "or", "other",
                "others", "otherwise", "ought", "our", "ours", "ourselves", "out", "outside", "over",
                "overall", "own", "p", "particular", "particularly", "per", "perhaps", "placed", "please",
                "plus", "possible", "presumably", "probably", "provides", "q", "que", "quite", "qv", "r",
                "rather", "rd", "re", "really", "reasonably", "regarding", "regardless", "regards",
                "relatively", "respectively", "right", "s", "said", "same", "saw", "say", "saying", "says",
                "second", "secondly", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self",
                "selves", "sensible", "sent", "serious", "seriously", "seven", "several", "shall", "she",
                "should", "since", "six", "so", "some", "somebody", "somehow", "someone", "something",
                "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "specified", "specify",
                "specifying", "still", "sub", "such", "sup", "sure", "t", "take", "taken", "tell", "tends",
                "th", "than", "thank", "thanks", "thanx", "that", "thats", "the", "their", "theirs", "them",
                "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein",
                "theres", "thereupon", "these", "they", "think", "third", "this", "thorough", "thoroughly",
                "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too",
                "took", "toward", "towards", "tried", "tries", "truly", "try", "trying", "twice", "two", "u",
                "un", "under", "unfortunately", "unless", "unlikely", "until", "unto", "up", "upon", "us",
                "use", "used", "useful", "uses", "using", "usually", "uucp", "v", "value", "various", "ve",
                "very", "via", "viz", "vs", "w", "want", "wants", "was", "way", "we", "welcome", "well",
                "went", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter",
                "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while",
                "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "willing", "wish",
                "with", "within", "without", "wonder", "would", "would", "x", "y", "yes", "yet", "you", "your",
                "yours", "yourself", "yourselves", "z", "zero"]

def jaccard_similarity(x, y):
    intersection_cardinality = len(set(x).intersection(set(y)))
    union_cardinality = len(set(x).union(set(y)))
    return intersection_cardinality / float(union_cardinality)

def getWordsInFile(file):
    #diccionario que contendra todas las palabras
    mainwords = {}
    for line in file:
        for word in line.split():

            word = word.strip().lower().replace(",", "").replace(":", "").replace(";", "").replace("-",
                                                                                                   "").replace(
                ".", "").replace("\"", "").replace("]", "").replace("[", "").replace(")", "").replace("(", "")
            
            #conteo de palabras diferenciando las palabras que no se incluyen en el conteo
            if word not in words2ignore:
                if word in mainwords and word != '':
                    mainwords[word] += 1
                else:
                    mainwords[word] = 1
    return mainwords

def getTenMainWords(i):
    file = open(rootDir + fileList[i], 'r')
    mainwords = getWordsInFile(file)
    file.close()
    #esta linea se implementa para ordenar los archivos por peso
    sorted_mainwords = sorted(mainwords.items(), key=operator.itemgetter(1))[::-1]#buscar
    #diez palabras mas importantes
    for j in range(10):
        tenMainWords.append(sorted_mainwords[j][0])

def countWords(file):
    for line in file:
        for word in line.split():
            word = word.strip().lower().replace(",", "").replace(":", "").replace(";", "").replace("-",
                                                                                                   "").replace(
                ".", "").replace("\"", "").replace("]", "").replace("[", "").replace(")", "").replace("(", "")
            if word in allMainWords:
                result[allMainWords.index(word)] += 1
    return result

def printResults(listaFiles, z, numerodecentroides):
    clusters = []
    for i in range(numerodecentroides):
        clusters.append([])

    for i in range(len(listaFiles)):
        clusters[int(z[i])].append(listaFiles[i])

    for i in range(len(clusters)):
        print("cluster ",i,":",clusters[i])
    return None

if __name__ == '__main__':
    iniTime = time.time()
    k = 2 # El numero de clusters a sacar
    maxIters = 10
    rootDir = sys.argv[1]
    fileList = []
    frecuencia = {}
    result = []
    #Get nombre de archivos en la carpeta que pasaron de parametro
    if comm.rank == 0:
        fileList = list(os.walk(rootDir))[0][2]
    #comparte esta lista con cada uno de los nodos
    fileList = comm.bcast(fileList, root)
    tenMainWords = []
    #recorre los textos  que le pertenecen a cada nodo y les saca las palabras
    for i in range(comm.rank, len(fileList), comm.size):
        getTenMainWords(i)

    #lista de listas que contiene las 10 palabras mas importantes procesadas por cada nodo
    mainWordPerCore = comm.gather(tenMainWords,root)
    # Lista que contiene las 10 palabras mas importantes 
    allMainWords = []
    if comm.rank == 0:
        #junta las pabras en una lista 
        for i in range(len(mainWordPerCore)):
            for element in mainWordPerCore[i]: 
                if element not in allMainWords:
                    allMainWords.extend(element)


    #comparte la lista final de palabras a todos los nodos
    allMainWords = comm.bcast(allMainWords, root)
    #conteo buscando las palabras mas importantes
    #frecuencia = {}
    for i in range(comm.rank, len(fileList), comm.size):
        result = []
        for j in range(len(allMainWords)):
            result.append(0)
        file = open(rootDir + fileList[i], 'r')
        result = countWords(file)
        frecuencia[fileList[i]] = result
    #recibe el conteo de las palabras(esto se puede optimizar al sacar solo 10 palabras en este momento se pueden tener mas de 10)
    frecuencia = comm.gather(frecuencia,root)

    frecuenciaPorLibro = {}
    if(comm.rank == 0):
        #print(type(frecuencia[0]))
        #print (frecuencia[0])
        for i in range(len(frecuencia)):
            frecuenciaPorLibro.update(frecuencia[i])
        #print(frecuenciaPorLibro)


    frecuenciaPorLibro = comm.bcast(frecuenciaPorLibro, root)

    filesSize = len(frecuenciaPorLibro)
    jaccardMatrix = np.zeros((filesSize, filesSize)) # Sera la matriz de distancias entre archivos
    listaFiles = list(frecuenciaPorLibro.keys())
    #Jaccard:
    for i in range(comm.rank, len(frecuenciaPorLibro), comm.size):
        for j in range(filesSize):
            jaccardMatrix[i][j] = 1.0 - (jaccard_similarity(frecuenciaPorLibro[listaFiles[i]], frecuenciaPorLibro[listaFiles[j]]))
    jaccardMatrix = comm.gather(jaccardMatrix, root)
    
    centroids = []
    matrizFinal = 0
    if comm.rank == 0:
        for row in jaccardMatrix:
            matrizFinal += row
    #K-means:
        centroids = matrizFinal[np.random.choice(np.arange(len(matrizFinal)), k), :]
        while centroids[0][0] == centroids[1][0]:
            centroids = matrizFinal[np.random.choice(np.arange(len(matrizFinal)), k), :]

    matrizFinal = comm.bcast(matrizFinal,root)
    centroids = comm.bcast(centroids, root)
    filesSize2 = len(matrizFinal)
    for i in range(maxIters):
        argminList = np.zeros(filesSize2)
        for i in range(comm.rank, len(matrizFinal), comm.size):
            dotList = []
            for y_k in centroids:
                dotList.append(np.dot(matrizFinal[i] - y_k, matrizFinal[i] - y_k))
            argminList[i] = np.argmin(dotList)
        recibC = comm.gather(argminList, root)
        librosCentroides = []
        if comm.rank == 0:
            librosCentroides = np.zeros(len(recibC[0]))
            for li in range(len(recibC)):
                librosCentroides += recibC[li]
        allCentroids = comm.bcast(librosCentroides,root)

        centroidesTemp = []
        for i in range(k):
            centroidesTemp.insert(i, [])

        for i in range(comm.rank, k, comm.size):
            truefalseArr = allCentroids == i
            if True in truefalseArr:
                propiosKArr = matrizFinal[truefalseArr]
                promedioArr = propiosKArr.mean(axis=0)
                centroidesTemp[i]=list(promedioArr)                
            else:
                centroidesTemp[i].append(cent[i])

        recibZ = comm.gather(centroidesTemp,root)
        centroidesFinales = []
        for j in range(k):
            centroidesFinales.append([])
        if comm.rank == 0:
            for i in range(len(recibZ)):
                for j in range(len(recibZ[i])):
                    centroidesFinales[j] += recibZ[i][j]
            centroids = centroidesFinales

    if comm.rank == 0:
        print("Tiempo final: ", time.time()-iniTime)
        listaFiles = list(frecuenciaPorLibro.keys())
        printResults(listaFiles, allCentroids,len(centroidesTemp))
