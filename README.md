# ✅ To-Do List em Python

Este é um projeto simples de **lista de tarefas (To-Do List)** feito em **Python** com interação por terminal.  
Ele permite que o usuário adicione, remova, liste e marque tarefas como concluídas, com persistência em um arquivo `.txt`.

## 📂 Estrutura

```
ToDolist_python/
│
├── tarefas/
│   └── lista1.txt       # Arquivo onde as tarefas são salvas
│
├── prompt.py            # Arquivo principal do programa
└── README.md            # Este arquivo
```

## ⚙️ Funcionalidades

- [x] Listar tarefas  
- [x] Adicionar nova tarefa  
- [x] Remover tarefa  
- [x] Marcar tarefa como concluída  
- [ ] Interface gráfica (futuramente)

## 🧠 Como funciona

As tarefas são salvas em um arquivo `.txt` (`tarefas/lista1.txt`).  
Cada linha representa uma tarefa, que pode estar marcada como:

- `[ ]` Não concluída  
- `[x]` Concluída

## 🚀 Como executar

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/ToDolist_python.git
```

2. **Entre na pasta do projeto:**

```bash
cd ToDolist_python
```

3. **Execute o script principal:**

```bash
python prompt.py
```

## 💡 Exemplo de uso

```
-----Bem-Vindo-----

1 - Listar Tarefas
2 - Adicionar tarefa
3 - Remover tarefa
4 - Marcar tarefa concluida
5 - Sair

Escolha uma opção: 1

1 - [ ] Comprar pão
2 - [x] Estudar Python
```

## 👨‍💻 Autor

**Yago Emanuel**  
Desenvolvedor iniciante com experiencia em javascript.  
[linkedin]: https://www.linkedin.com/in/yago-emanuel-brito-de-moura-417385275/

## 📌 Melhorias futuras

- Interface gráfica com Tkinter ou Web  
- Suporte para múltiplas listas  
- Ordenação por prioridade ou data  
- Marcação de tarefas com datas e horários
