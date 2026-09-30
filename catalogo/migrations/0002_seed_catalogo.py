from django.db import migrations

DIRETORES = [
    ('Christopher Nolan', 'Britânica'),
    ('Francis Ford Coppola', 'Norte-americana'),
    ('Bong Joon-ho', 'Sul-coreana'),
    ('Fernando Meirelles', 'Brasileira'),
]

FILMES = [
    {
        'titulo': 'A Origem',
        'genero': 'Ficção Científica',
        'diretor': 'Christopher Nolan',
        'sinopse': 'Um ladrão especializado em roubar segredos através de sonhos recebe a missão inversa: plantar uma ideia na mente de um executivo.',
        'avaliacoes': [
            ('Marina', 5, 'Assisti três vezes e ainda acho detalhe novo.'),
            ('Rafael', 4, 'Roteiro impecável, mas exige atenção total.'),
            ('Bia', 5, 'A trilha sonora carrega o filme inteiro.'),
        ],
    },
    {
        'titulo': 'O Poderoso Chefão',
        'genero': 'Drama',
        'diretor': 'Francis Ford Coppola',
        'sinopse': 'A saga da família Corleone mostra a ascensão de Michael, herdeiro relutante de um dos maiores impérios do crime organizado.',
        'avaliacoes': [
            ('Marina', 5, 'Envelheceu melhor que quase tudo do cinema.'),
            ('Diego', 5, 'Atuação do Brando em outro patamar.'),
        ],
    },
    {
        'titulo': 'Interestelar',
        'genero': 'Ficção Científica',
        'diretor': 'Christopher Nolan',
        'sinopse': 'Um grupo de exploradores viaja através de um buraco de minhoca em busca de um novo lar para a humanidade.',
        'avaliacoes': [
            ('Rafael', 5, 'A cena do planeta da água me deixou sem ar.'),
            ('Bia', 4, 'Emocionante, ainda que a física confunda em partes.'),
        ],
    },
    {
        'titulo': 'Parasita',
        'genero': 'Suspense',
        'diretor': 'Bong Joon-ho',
        'sinopse': 'A família de um homem desempregado se infiltra na rotina de uma família rica, com consequências inesperadas.',
        'avaliacoes': [
            ('Diego', 5, 'Muda de gênero no meio e acerta nos dois.'),
            ('Marina', 4, 'O roteiro é cirúrgico.'),
            ('Lucas', 5, 'Merecido o Oscar.'),
        ],
    },
    {
        'titulo': 'Cidade de Deus',
        'genero': 'Drama',
        'diretor': 'Fernando Meirelles',
        'sinopse': 'A história de dois jovens que crescem em uma favela do Rio de Janeiro e seguem caminhos opostos diante da violência.',
        'avaliacoes': [
            ('Lucas', 5, 'Melhor filme brasileiro que já vi.'),
            ('Bia', 4, 'Pesado, mas necessário.'),
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
    Genero.objects.filter(nome__in={f['genero'] for f in FILMES}).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(criar_dados, remover_dados),
    ]
