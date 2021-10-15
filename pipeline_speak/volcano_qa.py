# -*- coding: iso-8859-15 -*-
import os, sys
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from transformers import pipeline
from query_speak import askQuestion, getAnswer

def main():

    # get the volcano corpus
    with open('volcanic.corpus', encoding="utf8") as file:
        context = file.read().replace('\n', '')

    # endless loop - keep soliticitng for questions
    while(True):
        # say greeting
        question = askQuestion()

        # Generating an answer to the question in context
        qa = pipeline("question-answering")
        answer = qa(question=question, context=context)

        getAnswer(answer)


if __name__ == "__main__":
    main()
