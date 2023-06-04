from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import warnings
import logging
import click

logging.disable(logging.WARNING)
warnings.filterwarnings("ignore")

@click.command()
@click.option("--text",prompt="English Phrase")
def translate(text):
    tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-fr")
    model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-fr")
    input_ids = tokenizer.encode(text, return_tensors="pt")
    outputs = model.generate(input_ids, max_length=512)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    click.echo(f"French Phrase: {decoded}")

if __name__ == '__main__':
    translate()