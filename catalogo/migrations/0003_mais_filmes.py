from django.db import migrations

DIRETORES = [
    ('Quentin Tarantino', 'Norte-americana'),
    ('David Fincher', 'Norte-americana'),
    ('Lana Wachowski', 'Norte-americana'),
    ('Peter Jackson', 'Neozelandesa'),
    ('Kleber Mendonça Filho', 'Brasileira'),
    ('Walter Salles', 'Brasileira'),
    ('José Padilha', 'Brasileira'),
    ('Hayao Miyazaki', 'Japonesa'),
    ('Stanley Kubrick', 'Norte-americana'),
    ('Damien Chazelle', 'Norte-americana'),
]

FILMES = [
    {
        'titulo': 'Pulp Fiction',
        'genero': 'Crime',
        'diretor': 'Quentin Tarantino',
        'sinopse': 'Histórias de gângsteres, um boxeador e um par de assaltantes se cruzam em Los Angeles, contadas fora de ordem.',
        'avaliacoes': [
            ('Marina', 5, 'A estrutura embaralhada é o melhor do filme.'),
            ('Diego', 4, 'Diálogo acima da média em cada cena.'),
        ],
    },
    {
        'titulo': 'Clube da Luta',
        'genero': 'Drama',
        'diretor': 'David Fincher',
        'sinopse': 'Um funcionário insone e um vendedor de sabonetes fundam um clube clandestino que sai do controle.',
        'avaliacoes': [
            ('Rafael', 5, 'A segunda vez que assisti foi um filme completamente diferente.'),
            ('Bia', 4, 'Envelheceu bem, apesar do exagero.'),
        ],
    },
    {
        'titulo': 'Matrix',
        'genero': 'Ficção Científica',
        'diretor': 'Lana Wachowski',
        'sinopse': 'Um programador descobre que a realidade é uma simulação e se junta a um grupo que luta contra as máquinas.',
        'avaliacoes': [
            ('Lucas', 5, 'Mudou o que efeito visual podia ser.'),
            ('Marina', 4, 'A ideia central ainda provoca.'),
            ('Diego', 5, 'Referência obrigatória.'),
        ],
    },
    {
        'titulo': 'O Senhor dos Anéis: A Sociedade do Anel',
        'genero': 'Aventura',
        'diretor': 'Peter Jackson',
        'sinopse': 'Um hobbit recebe a missão de destruir um anel capaz de dominar toda a Terra Média.',
        'avaliacoes': [
            ('Bia', 5, 'A construção de mundo é impecável.'),
            ('Rafael', 5, 'Três horas que passam voando.'),
        ],
    },
    {
        'titulo': 'Bacurau',
        'genero': 'Suspense',
        'diretor': 'Kleber Mendonça Filho',
        'sinopse': 'Um povoado do sertão some do mapa e passa a receber visitas estranhas, que cobram um preço alto.',
        'avaliacoes': [
            ('Lucas', 5, 'Não se parece com nada que eu tinha visto.'),
            ('Marina', 4, 'A virada no meio é brutal.'),
        ],
    },
    {
        'titulo': 'Central do Brasil',
        'genero': 'Drama',
        'diretor': 'Walter Salles',
        'sinopse': 'Uma escrevente de cartas aposentada atravessa o país com um menino em busca do pai que ele nunca conheceu.',
        'avaliacoes': [
            ('Bia', 5, 'A Fernanda Montenegro sustenta o filme inteiro.'),
            ('Diego', 4, 'Simples e devastador.'),
        ],
    },
    {
        'titulo': 'Tropa de Elite',
        'genero': 'Ação',
        'diretor': 'José Padilha',
        'sinopse': 'Um capitão do BOPE procura um substituto enquanto enfrenta o tráfico e a corrupção no Rio de Janeiro.',
        'avaliacoes': [
            ('Rafael', 4, 'Ritmo que não deixa respirar.'),
            ('Lucas', 5, 'Virou vocabulário popular por um motivo.'),
        ],
    },
    {
        'titulo': 'A Viagem de Chihiro',
        'genero': 'Animação',
        'diretor': 'Hayao Miyazaki',
        'sinopse': 'Uma menina fica presa num mundo de espíritos e precisa trabalhar numa casa de banhos para resgatar os pais.',
        'avaliacoes': [
            ('Marina', 5, 'Cada quadro poderia ser um quadro na parede.'),
            ('Bia', 5, 'Assisto de novo todo ano.'),
            ('Rafael', 4, 'Estranho no melhor sentido.'),
        ],
    },
    {
        'titulo': 'O Iluminado',
        'genero': 'Terror',
        'diretor': 'Stanley Kubrick',
        'sinopse': 'Um escritor aceita cuidar de um hotel isolado durante o inverno e perde o controle diante do que habita o lugar.',
        'avaliacoes': [
            ('Diego', 5, 'O silêncio assusta mais que o susto.'),
            ('Lucas', 4, 'Os corredores ficam na cabeça.'),
        ],
    },
    {
        'titulo': 'Whiplash: Em Busca da Perfeição',
        'genero': 'Drama',
        'diretor': 'Damien Chazelle',
        'sinopse': 'Um baterista talentoso enfrenta um professor que acredita que só a humilhação produz grandeza.',
        'avaliacoes': [
            ('Bia', 5, 'A cena final é um soco.'),
            ('Marina', 4, 'Termina e eu continuo tenso.'),
        ],
    },
    {
        'titulo': 'Kill Bill: Volume 1',
        'genero': 'Ação',
        'diretor': 'Quentin Tarantino',
        'sinopse': 'Uma ex-assassina desperta de um coma e sai atrás dos antigos colegas que tentaram matá-la.',
        'avaliacoes': [
            ('Lucas', 4, 'Coreografia de briga como dança.'),
            ('Bia', 5, 'A sequência da Casa das Folhas Azuis é inesquecível.'),
        ],
    },
    {
        'titulo': 'Se7en: Os Sete Crimes Capitais',
        'genero': 'Crime',
        'diretor': 'David Fincher',
        'sinopse': 'Dois detetives caçam um assassino que escolhe as vítimas segundo os sete pecados capitais.',
        'avaliacoes': [
            ('Diego', 5, 'O final não sai da cabeça.'),
            ('Marina', 5, 'Chove o filme inteiro e isso importa.'),
        ],
    },
    {
        'titulo': 'Laranja Mecânica',
        'genero': 'Ficção Científica',
        'diretor': 'Stanley Kubrick',
        'sinopse': 'Um jovem violento é submetido a um tratamento experimental que pretende curá-lo à força.',
        'avaliacoes': [
            ('Rafael', 4, 'Desconfortável de propósito.'),
            ('Lucas', 5, 'Ninguém compõe um plano como o Kubrick.'),
        ],
    },
    {
        'titulo': 'Meu Amigo Totoro',
        'genero': 'Animação',
        'diretor': 'Hayao Miyazaki',
        'sinopse': 'Duas irmãs se mudam para o campo e descobrem criaturas que só as crianças conseguem ver.',
        'avaliacoes': [
            ('Bia', 5, 'O filme mais gentil que existe.'),
            ('Marina', 5, 'A cena do ponto de ônibus é perfeita.'),
        ],
    },
    {
        'titulo': 'La La Land: Cantando Estações',
        'genero': 'Romance',
        'diretor': 'Damien Chazelle',
        'sinopse': 'Uma atriz iniciante e um pianista de jazz se apaixonam enquanto perseguem carreiras que os afastam.',
        'avaliacoes': [
            ('Marina', 4, 'O epílogo redime o filme todo.'),
            ('Diego', 3, 'Bonito, mas me deixou frio.'),
        ],
    },
]


def criar_dados(apps, schema_editor):
    Genero = apps.get_model('catalogo', 'Genero')
    Diretor = apps.get_model('catalogo', 'Diretor')
    Filme = apps.get_model('catalogo', 'Filme')
    Avaliacao = apps.get_model('catalogo', 'Avaliacao')

    for nome, nacionalidade in DIRETORES:
        Diretor.objects.get_or_create(nome=nome, defaults={'nacionalidade': nacionalidade})

    for dados in FILMES:
        genero, _ = Genero.objects.get_or_create(nome=dados['genero'])
        diretor = Diretor.objects.get(nome=dados['diretor'])

        filme, criado = Filme.objects.get_or_create(
            titulo=dados['titulo'],
            defaults={
                'genero': genero,
                'diretor': diretor,
                'sinopse': dados['sinopse'],
            },
        )
        if not criado:
            continue

        for autor, nota, comentario in dados['avaliacoes']:
            Avaliacao.objects.create(
                filme=filme, autor=autor, nota=nota, comentario=comentario
            )


def remover_dados(apps, schema_editor):
    Genero = apps.get_model('catalogo', 'Genero')
    Diretor = apps.get_model('catalogo', 'Diretor')
    Filme = apps.get_model('catalogo', 'Filme')

    # As avaliações saem em cascata junto com os filmes.
    Filme.objects.filter(titulo__in=[f['titulo'] for f in FILMES]).delete()
    Diretor.objects.filter(nome__in=[nome for nome, _ in DIRETORES]).delete()
    # Só remove gêneros que ficaram sem nenhum filme.
    for nome in {f['genero'] for f in FILMES}:
        genero = Genero.objects.filter(nome=nome).first()
        if genero and not genero.filmes.exists():
            genero.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_seed_catalogo'),
    ]

    operations = [
        migrations.RunPython(criar_dados, remover_dados),
    ]
