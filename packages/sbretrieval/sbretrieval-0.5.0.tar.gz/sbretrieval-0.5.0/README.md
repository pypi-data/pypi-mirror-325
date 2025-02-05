# Summary Based Retrieval

Indexação e busca de documentos baseada em sumário (gerado por uma LLM), utilizando **PostgreSQL** e **pgvector**, com
suporte à modelos da **OpenAI** e **Google Gemini**. Busca semântica (embeddings) e limitada por quantidade de tokens.

## Busca Baseada em Sumários

Com o recente avanço de diferentes modelos de deep learning, já é comum o uso de *embeddings* para casos de uso como
sistemas de recomendação e RAG (Retrieval-Augmented Generation).

No entanto, nem todo documento performa bem nesse tipo de busca, há casos em que o conteúdo *ipsis litteris* do
documento possui pouco valor semântico (código-fonte legado mal documentado, por exemplo).

A técnica abordada nessa biblioteca consiste em, com o auxílio de uma LLM (Large Language Model), gerar um sumário do
documento e então gerar um embedding deste sumário (ao invés do próprio conteúdo original).

## Busca Limitada por Quantidade de Tokens

As buscas por embeddings tipicamente são limitadas por um número de registros. "Me dê os 25 resultados mais relevantes"
por exemplo, "25" sendo a quantidade desejada de resultados.

Vários dos casos de uso de embeddings são para realização de RAG, isto é, a obtenção de dados para 'aumentar' o contexto
de informações ao enviar um prompt à um LLM. Ora não só não sabemos a exata quantidade de registros que queremos como
também gostariamos de incluir o máximo de informação.

Máximo esse normalmente medido em *tokens*, a quantidade máxima de tokens da LLM que você irá utilizar. Nesta
biblioteca, não só geramos e indexamos os embeddings para realizar a busca semântica como também realizamos a contagem
de tokens e salvamos esse valor para cada registro.

O intuito é, ao invés de limitarmos nossa busca por uma de quantidade de registros ("me dê os 25 resultados mais
relevantes"), nós limitamos a quantidade de tokens do resultado ("me dê os resultados mais relevantes sem ultrapassar 20
mil tokens no total").

## Pré-requisito: PostgreSQL e pgvector

A biblioteca utiliza o banco de dados [PostgreSQL](https://www.postgresql.org) e o pacote [asyncpg](https://github.com/MagicStack/asyncpg).
Antes de utilizar a biblioteca, garanta que a extensão [pgvector](https://github.com/pgvector/pgvector) esteja instalada
e o que o banco de dados (com suas tabelas) esteja criado.

Para criação das tabelas necessárias, é necessário executar o script [create\_tables.sql](sql/create_tables.sql).
Executando com o comando `psql`:

```
$ psql -v embedding_size=768 -h localhost -U meu_usuario -d meu_banco -f create_tables.sql
```

## Pré-requisito: Chave da OpenAI ou do Google Gemini

A biblioteca suporta tanto modelos da OpenAI quanto modelos do Google Gemini para geração de sumários e seus embeddings.

Garanta que a variável de ambiente `OPENAI_API_KEY` esteja configurada ao utilizar modelos da OpenAI, ou a variável
`GEMINI_API_KEY` caso utilize Google Gemini.

Se você preferir, pode-se criar a variável de ambiente dentro do próprio processo ao invés de no shell externo: 

```py
import os

os.environ['OPENAI_API_KEY'] = 'sua_chave_da_openai'  # ou 'GEMINI_API_KEY' para Google Gemini
```

## Modelos Suportados

No momento da escrita desta documentação, os seguintes modelos de embedding de texto estão disponíveis:

Fornecedor    | Nome                        | Tamanho do vetor
----------    | ----                        | ----------------------------
OpenAI        | `text-embedding-3-small`    | 1536 dimensões
OpenAI        | `text-embedding-3-large`    | 3072 dimensões
OpenAI        | `text-embedding-ada-002`    | 1536 dimensões
Google Gemini | `models/text-embedding-004` | 768 dimensões
Google Gemini | `models/embedding-001`      | 768 dimensões

E os seguintes LLMs:

Fornecedor    | Nome                         | Tamanho do contexto
----------    | ----                         | -------------------
OpenAI        | `gpt-4o-mini`                | 128.000 tokens
OpenAI        | `gpt-4o`                     | 128.000 tokens
OpenAI        | `o1-mini`                    | 128.000 tokens
OpenAI        | `o1-preview`                 | 128.000 tokens
Google Gemini | `models/gemini-1.5-flash-8b` | 1.048.576 tokens
Google Gemini | `models/gemini-1.5-flash`    | 1.048.576 tokens
Google Gemini | `models/gemini-1.5-pro`      | 2.097.152 tokens

As tabelas acima podem estar desatualizadas, consulte a documentação do fornecedor para informações mais recentes.

## Indexando um Documento

Para indexar um documento basta chamar a seguinte função da biblioteca:

```py
from asyncpg import connect
from sbretrieval import index_document

my_connection = await connect(...)  # a conexão é de sua responsabilidade

await index_document(
    connection=my_connection,                 # conexão inicializada acima
    document_key='123',                       # chave do documento externo à biblioteca (gerado e mantido por você)
    document_content='Lorem ipsum dolor...',  # conteúdo do documento (texto limpo)
    ai_vendor='openai',                       # fornecedor do modelo de IA
    embedding_model='text-embedding-ada-002', # modelo de embedding conforme definido pelo fornecedor
    summary_model='gpt-4o-mini',              # modelo de LLM conforme definido pelo fornecedor
    summary_prompt='Gere um sumário sem nenhuma formatação do texto abaixo:\n\n{}', # Prompt utilizado para gerar o sumário, note que "{}" é onde o conteúdo do documento será inserido
)
```

O seguinte é realizado na indexação de um documento (chamada acima):

- Uma chamada à LLM é feita, passando o conteúdo do documento e solicitando um sumário do mesmo.
- Uma chamada ao modelo de embedding é feita, passado o sumário obtido no passo acima e obtendo o seu embedding.
- Conta-se os tokens do conteúdo do documento original (e não do sumário).
- A chave do documento, seu sumário, seu embedding, e sua quantidade de tokens são salvos no banco de dados.

Para remover os índices de um documento, basta prover sua chave e efetuar a chamada abaixo:

```py
await remove_document(connection=my_connection, document_key='123')
```

## Buscando Documentos

Para buscar documentos dado um texto qualquer como *query*, chame a seguinte função:

```py
from asyncpg import connect
from sbretrieval import search_documents

my_connection = await connect(...)  # a conexão é de sua responsabilidade

search_result = await search_documents(
    connection=my_connection,                 # conexão inicializada acima
    query='Nulla id facilisis...',            # query de busca
    max_token_count=50000,                    # valor máximo de tokens que a soma dos dos documentos selecionados não deve exceder
    ai_vendor='openai',                       # fornecedor do modelo de IA
    embedding_model='text-embedding-ada-002', # modelo de embedding conforme definido pelo fornecedor
)

for document in search_result.selected_documents:          # "selected_documents" contém os documentos selecionados da tabela "document_embeddings"
    print(f'Document key: {document.key}')                 # "key" contém o valor da coluna "document_key"
    print(f'Document token count: {document.token_count}') # "token_count" contém o valor da coluna "token_count"

# "overflowed_document" contém o próximo documento mais relevante que não foi selecionado pois excederia o limite de tokens
print(f'Overflowed document key: {search_result.overflowed_document.key}')
print(f'Overflowed document token count: {search_result.overflowed_document.token_count}')
```

## Chave Secundária

A biblioteca suporta o uso de uma chave secundária (`document_secondary_key`) para segregar os documentos indexados.
Utilizando-a na indexação:

```py
await index_document(
    connection=my_connection,
    document_key='123',
    document_content='Lorem ipsum dolor...',
    ai_vendor='openai',
    embedding_model='text-embedding-ada-002',
    summary_model='gpt-4o-mini',
    summary_prompt='Gere um sumário sem nenhuma formatação do texto abaixo:\n\n{}',
    document_secondary_key='7d9d3aa', # chave secundária opcional
)
```

E na busca:

```py
search_result = await search_documents(
    connection=my_connection,
    query='Nulla id facilisis...',
    max_token_count=50000,
    ai_vendor='openai',
    embedding_model='text-embedding-ada-002',
    document_secondary_keys=['7d9d3aa'], # chave(s) secundária(s) opcional(is)
)
```

## Referências

OpenAI:

- [Modelos de LLM](https://platform.openai.com/docs/guides/text-generation#choosing-a-model)
- [Modelos de embedding](https://platform.openai.com/docs/guides/embeddings/embedding-models#embedding-models)
- [Contagem de tokens](https://github.com/openai/tiktoken)

Google Gemini:

- [Modelos de LLM](https://ai.google.dev/gemini-api/docs/models/gemini)
- [Modelos de embedding](https://ai.google.dev/gemini-api/docs/models/gemini#text-embedding-and-embedding)
- [Contagem de tokens](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/get-token-count)
