
#Relevance Ranking Algorithm to fetch tweepy by api v2
import math

def bm25_score(query, document, k1=1.2, b=0.75):
    score = 0
    doc_terms = document.split()
    doc_length = len(doc_terms)

    for term in query:
        if term in doc_terms:
            term_frequency = doc_terms.count(term)
            score += math.log10((doc_length + 1) / (term_frequency + 0.5)) * ((k1 + 1) * term_frequency) / (k1 * (1 - b + b * (doc_length / average_doc_length)) + term_frequency)

    return score