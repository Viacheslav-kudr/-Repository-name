# TODO реализовать функцию
def get_sentences_list(words):
    sentences_list=[]
    for sentences in words.split("."):
        if sentences:
            sentences_list.append(sentences.strip())
    return sentences_list

print(get_sentences_list("Здесь много разных слов. Возможно и много повторений..."))