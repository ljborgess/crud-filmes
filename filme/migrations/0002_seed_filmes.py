from django.db import migrations


FILMES = [
    {
        'titulo': 'A Origem',
        'genero': 'Ficção Científica',
        'sinopse': 'Um ladrão especializado em roubar segredos através de sonhos recebe a missão inversa: plantar uma ideia na mente de um executivo.',
    },
    {
        'titulo': 'O Poderoso Chefão',
        'genero': 'Drama',
        'sinopse': 'A saga da família Corleone mostra a ascensão de Michael, herdeiro relutante de um dos maiores impérios do crime organizado.',
    },
    {
        'titulo': 'Interestelar',
        'genero': 'Ficção Científica',
        'sinopse': 'Um grupo de exploradores viaja através de um buraco de minhoca em busca de um novo lar para a humanidade.',
    },
    {
        'titulo': 'Parasita',
        'genero': 'Suspense',
        'sinopse': 'A família de um homem desempregado se infiltra na rotina de uma família rica, com consequências inesperadas.',
    },
    {
        'titulo': 'Cidade de Deus',
        'genero': 'Drama',
        'sinopse': 'A história de dois jovens que crescem em uma favela do Rio de Janeiro e seguem caminhos opostos diante da violência.',
    },
]


def criar_filmes(apps, schema_editor):
    Genero = apps.get_model('filme', 'Genero')
    Filme = apps.get_model('filme', 'Filme')

    generos_cache = {}
    for dados in FILMES:
        nome_genero = dados['genero']
        if nome_genero not in generos_cache:
            genero, _ = Genero.objects.get_or_create(nome=nome_genero)
            generos_cache[nome_genero] = genero

        Filme.objects.create(
            titulo=dados['titulo'],
            genero=generos_cache[nome_genero],
            sinopse=dados['sinopse'],
        )


def remover_filmes(apps, schema_editor):
    Genero = apps.get_model('filme', 'Genero')
    Filme = apps.get_model('filme', 'Filme')
    titulos = [f['titulo'] for f in FILMES]
    generos = {f['genero'] for f in FILMES}
    Filme.objects.filter(titulo__in=titulos).delete()
    Genero.objects.filter(nome__in=generos).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(criar_filmes, remover_filmes),
    ]
