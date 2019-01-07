import click
from utils import language_recognizer

@click.command()
@click.option('--word', '-w')
def main(word):
    print('Trying to recognize the word "{word}"'.format(word=word))
    result = language_recognizer(word)
    print('Result: {result}'.format(result=result))

if __name__ == "__main__":
    main()