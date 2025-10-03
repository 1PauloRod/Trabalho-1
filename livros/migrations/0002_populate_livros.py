from django.db import migrations

def criar_livros(apps, schema_editor):
    Livro = apps.get_model("livros", "Livro")

    # Evita duplicar se já existirem livros
    if Livro.objects.exists():
        return

    Livro.objects.create(titulo="Python Básico", autor="João Silva", ano=2020, disponivel=True)
    Livro.objects.create(titulo="Django Essencial", autor="Maria Souza", ano=2021, disponivel=True)
    Livro.objects.create(titulo="Estruturas de Dados", autor="Ana Lima", ano=2019, disponivel=True)
    Livro.objects.create(titulo="Algoritmos em C", autor="Carlos Pereira", ano=2018, disponivel=True)

class Migration(migrations.Migration):

    dependencies = [
        ("livros", "0001_initial"),  # depende da primeira migração
    ]

    operations = [
        migrations.RunPython(criar_livros),
    ]
