from models import Pessoas


def insere_pessoas():
    pessoa = Pessoas(nome='LucasX', idade=30)
    print(pessoa)
    pessoa.save()


def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    # pessoa = Pessoas.query.filter_by(nome='Lucas').first()
    # print(pessoa.idade)


def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Lucas').first()
    pessoa.nome = 'Lukaum'
    pessoa.save()


def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='LucasX').first()
    pessoa.delete()


if __name__ == '__main__':
    # insere_pessoas()
    # altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()
