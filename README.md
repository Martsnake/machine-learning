# Aprendizagem Automatica

Repositorio de apoio a trabalhos, aulas e projetos da unidade curricular de Aprendizagem Automatica.

> O conteudo das aulas, os datasets e os metodos estudados devem ser adicionados de acordo com o programa e os materiais da disciplina.

## Requisitos

- Python 3.11 ou superior
- Git
- JupyterLab

## Preparar o ambiente

Na raiz do repositorio, cria e ativa um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```


No Windows PowerShell, ativa-o com:

```powershell
.venv\Scripts\Activate.ps1
```

Instala as dependencias:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Inicia o JupyterLab:

```bash
jupyter lab
```

## Organizacao

- `notebooks/`: notebooks do projeto.
- `data/raw/`: dados originais; nao guardar dados privados ou ficheiros grandes no GitHub.
- `data/processed/`: dados preparados; normalmente tambem ficam fora do Git.
- `src/`: codigo Python reutilizavel.
- `reports/figures/`: graficos e resultados para relatorios.
- `tests/`: testes do codigo em `src/`.

Os diretorios de dados e de resultados contem apenas ficheiros `.gitkeep` para manter a estrutura. Adiciona instrucoes para obter os dados, em vez de versionar datasets grandes.

## Executar testes (quando forem adicionados)

```bash
pytest
```

## Antes de publicar no GitHub

1. Confirma que nao incluiste dados pessoais, credenciais ou datasets com restricoes.
2. Atualiza este README com o objetivo, os datasets e os metodos realmente usados no projeto.
3. Regista as dependencias adicionais em `requirements.txt`.
