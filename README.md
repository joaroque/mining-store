# Проект 8.4 — Система учёта продаж

**Sistema de registo de vendas de produtos para o sector mineiro**, em Python, com armazenamento CSV.

## Estrutura

```text
mining_store/
├── main.py           # Menu e interacção com o utilizador
├── inventory.py      # Lista de produtos, pesquisa e actualização de stock
├── sales.py          # Registar vendas, histórico e total
├── csv_storage.py    # Ler, escrever e inicializar ficheiros CSV
├── data/
│   ├── products.csv  # Catálogo de produtos e stock actualizado
│   └── sales.csv     # Histórico das vendas
├── tests/
│   └── test_store.py # Testes automáticos
└── README.md
```

**Todas as funções e variáveis estão em inglês.** O menu apresentado ao utilizador está em russo, para a apresentação na universidade. Os dados são guardados em CSV (separador `;`, codificação UTF-8 com BOM quando alterados pelo programa).

## Como executar

1. Instalar Python 3.9 ou superior.
2. Extrair o ZIP e abrir a pasta `mining_store` no terminal (ou no VS Code).
3. Executar:

```bash
python main.py
```

No Windows, também podes usar `py main.py`.

Não é necessário instalar bibliotecas externas.

## Menu

- `1` — Mostrar produtos
- `2` — Vender um produto (por ID e quantidade)
- `3` — Mostrar o total das vendas
- `4` — Consultar histórico de vendas
- `0` — Sair

## Exemplo

Escolhe `2`, produto `1`, quantidade `2`.

- Capacete: 1 500 RUB × 2 = 3 000 RUB.
- Stock do capacete passa de 10 para 8.
- Uma linha de venda é adicionada ao `data/sales.csv`.
- O stock actualizado fica guardado no `data/products.csv`.

**Persistência:** ao sair e abrir novamente o programa, o stock e as vendas anteriores continuam guardados. Para repor os exemplos, substitui os CSV pelos originais do ZIP.

## Para explicar em russo (A1–A2)

> Это программа на Python для магазина. Она показывает товары и цены. Можно продать товар. Программа сохраняет продажи в CSV-файл и изменяет количество товаров на складе.

Tradução: Este é um programa Python para uma loja. Mostra produtos e preços. É possível vender um produto. O programa guarda as vendas num CSV e actualiza as quantidades no armazém.

## Limites

Trabalho demonstrativo simples: pensado para **um utilizador de cada vez** e para preços em rublos inteiros. Não é um sistema de caixa comercial, nem inclui autenticação ou operações simultâneas.

## Testes

Executa `python -m unittest discover -s tests -v` para verificar vendas, stock e persistência.
