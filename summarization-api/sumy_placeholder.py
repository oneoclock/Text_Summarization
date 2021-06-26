from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

def summarize(document_content):
    LANGUAGE = "english"
    SENTENCES_COUNT = 2

    #parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
    parser = PlaintextParser(document_content, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    
    sentences_list = []
    
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        #print(sentence._text)
        sentences_list.append(sentence._text)
        
    sentences = ' '.join(sentences_list)
    return sentences
        
#print(summarize('After deciding to sell their zoo in India and move to Canada,'))# Santosh and Gita Patel board a freighter with their sons and a few remaining animals. Tragedy strikes when a terrible storm sinks the ship, leaving the Patels teenage son, Pi (Suraj Sharma), as the only human survivor. However, Pi is not alone; a fearsome Bengal tiger has also found refuge aboard the lifeboat. As days turn into weeks and weeks drag into months, Pi and the tiger must learn to trust each other if both are to survive.'))