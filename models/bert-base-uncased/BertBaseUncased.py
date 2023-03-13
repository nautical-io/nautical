from transformers import pipeline


def BertBaseUncased(input: str):
    unmasker = pipeline("fill-mask", model="bert-base-uncased")
    return unmasker(input)
