import click
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import warnings

warnings.filterwarnings("ignore")

@click.command()
@click.option("--text")
def translate(text) -> str:
    translate_input = input("Phrase in English: ")
    tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-fr")
    model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-fr")
    input_ids = tokenizer.encode(translate_input, return_tensors="pt")
    outputs = model.generate(input_ids, max_length=512)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("Phrase in French: ")
    print(decoded)
    return decoded

if __name__ == '__main__':
    translate()