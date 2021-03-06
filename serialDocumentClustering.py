import operator, os, sys
import numpy as np
import time

def getT(rootDir):
    T = []
    for dirName, subdirList, fileList in os.walk(rootDir):
        print('Directorio encontrado: %s' % dirName)
        for archivo in fileList:

            file = open(rootDir + archivo, 'r')

            stopwordsman = ["a", "able", "about", "above", "according", "accordingly", "across", "actually", "after",
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
            mainwords = {}

            # print(str(archivo))

            for line in file:

                for word in line.split():
                    word = word.strip().lower().replace(",", "").replace(":", "").replace(";", "").replace("-",
                                                                                                           "").replace(
                        ".", "").replace("\"", "").replace("]", "").replace("[", "").replace(")", "").replace("(", "")
                    if word not in stopwordsman:
                        if word in mainwords and word != '':
                            mainwords[word] += 1
                        else:
                            mainwords[word] = 1

            sorted_mainwords = sorted(mainwords.items(), key=operator.itemgetter(1))[::-1]
            
            finalwords = {}
            for i in range(10):
                finalwords[sorted_mainwords[i][0]] = sorted_mainwords[i][1]
            T.extend([element for element in list(finalwords.keys()) if element not in T])
            
    return T


# Devuelve mapa con los resultados de ft(d,t)
def ft(T):
    mapa = {}

    for dirName, subdirList, fileList in os.walk(rootDir):
        for archivo in fileList:
            result = []
            for i in range(len(T)):
                result.append(0)

            file = open(rootDir + archivo, 'r')

            for line in file:
                for word in line.split():
                    word = word.strip().lower().replace(",", "").replace(":", "").replace(";", "").replace("-",
                                                                                                           "").replace(
                        ".", "").replace("\"", "").replace("]", "").replace("[", "").replace(")", "").replace("(", "")
                    if word in T:
                        result[T.index(word)] += 1

            mapa[archivo] = result

    return mapa


def preJaccard(fdt):
    tam = len(fdt)

    matrixC = np.empty((tam, tam))
    listaFiles = list(fdt.keys())

    for i in range(tam):
        for j in range(tam):
            matrixC[i][j] = 1.0 - (jaccard_similarity(fdt[listaFiles[i]], fdt[listaFiles[j]]))

    return matrixC

def jaccard_similarity(x, y):
    intersection_cardinality = len(set(x).intersection(set(y)))
    union_cardinality = len(set(x).union(set(y)))
    return intersection_cardinality / float(union_cardinality)


def kMeans2(X, K, maxIters=10, plot_progress=None):

    centroids = X[np.random.choice(np.arange(len(X)), K), :]

    if len(centroids) > 1:
        while centroids[0][0] == centroids[1][0]:
            centroids = X[np.random.choice(np.arange(len(X)), K), :]
            
    C = []
    for i in range(maxIters):
        argminList = []
        for x_i in X:
            dotList = []
            for y_k in centroids:
                dotList.append(np.dot(x_i - y_k, x_i - y_k))
            argminList.append(np.argmin(dotList))
        C = np.array(argminList)
        centroidesTemp = [] 
        for k in range(K):
            truefalseArr = C == k
            if True in truefalseArr:
                propiosKArr = X[truefalseArr]
                promedioArr = propiosKArr.mean(axis=0)
                centroidesTemp.append(promedioArr)
                
            else:
                centroidesTemp.append(centroids[k])

        centroids = centroidesTemp
    return np.array(centroids), C

if __name__ == '__main__':
    timeini = time.time()
    k = 4
    rootDir = sys.argv[1]
    T = getT(rootDir)
    fdt = ft(T)
    matrizJaccard = preJaccard(fdt)
    centroides, finalList = kMeans2(matrizJaccard, k)
    listaFiles = list(fdt.keys())
    clusters = []
    for i in range(len(centroides)):
        clusters.append([])

    for i in range(len(listaFiles)):
        clusters[int(finalList[i])].append(listaFiles[i])
    print("Tiempo transcurrido: ", time.time() - timeini)
    for i in range(len(clusters)):
        print("cluster ",i,":",clusters[i])
