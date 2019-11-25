import string
import nltk

class funcoes:
    def __init__(self):
        print('')

    def removeStopwords(self, array):
        nltk.download('stopwords')
        stopwords = nltk.corpus.stopwords.words('portuguese')
        i = 0
        for reg in array:
            if reg in stopwords:
                del(array[i])
            i = i + 1
        return array

    def montaVetorDuplo(self, text):
        array = []
        text = text.lower()
        for caractere in "!@#$%*,.()<>:|\/?":
            text = text.replace(caractere, "")
        for reg in text.split(" "):
            if reg.find("-"):
                for reg2 in reg.split("-"):
                    array.append(reg2)
            else:
                array.append(reg)
        i = 0
        array2 = []
        for row in array:
            if not ((i+1) == (len(array))):
                array2.append(str(array[i])+' '+str(array[i+1]))
                i = i+1
        return array2

    def montaVetor(self, text):
        array = []
        text = text.lower()
        for caractere in "!@#$%*,.()<>:|\/?":
            text = text.replace(caractere, "")
        for reg in text.split(" "):
            if reg.find("-"):
                for reg2 in reg.split("-"):
                    array.append(reg2)
            else:
                array.append(reg)
        return array

    def RemoveDuplicados(self, list):
        final_list = []
        for num in list:
            if num not in final_list:
                final_list.append(num)
        return final_list


pass
