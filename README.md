# CurriculumForge

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Status](https://img.shields.io/badge/status-stable-green)

Uma ferramenta Python robusta que converte currículos de texto simples (TXT) em documentos HTML/PDF com design profissional, limpo e otimizado para impressão A4. Construído com arquitetura limpa (Clean Architecture) e melhores práticas de desenvolvimento.

<p align="center">
  <img src="output/preview_placeholder.png" alt="Exemplo de Currículo Gerado" width="600">
</p>

## Funcionalidades

- **Parser Inteligente**: Detecta automaticamente seções, contatos e listas a partir de arquivos de texto simples.
- **Design Premium**: Gera layouts de alta qualidade, prontos para sistemas de RH (ATS-friendly) e otimizados para impressão.
- **Arquitetura Limpa**: Código organizado com separação clara de responsabilidades (Modelos, Parser, Gerador).
- **Customizável**: Templates Jinja2 e CSS fáceis de editar.

## Estrutura do Projeto

```
curriculo_vitae_create/
├── src/
│   ├── models.py       # Classes de Dados (Resume, Section)
│   ├── parser.py       # Lógica de processamento de texto
│   └── generator.py    # Lógica de geração de HTML
├── templates/          # Templates HTML (Jinja2)
├── static/             # CSS e estilos
├── input/              # Arquivos de texto de entrada
└── output/             # Resultados gerados
```

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/CurriculumForge.git
   cd CurriculumForge
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Como Usar

1. Crie um arquivo de texto com seu currículo (veja `modelo_preenchimento.txt` para o formato ideal).
2. Execute o gerador:

   ```bash
   # Uso padrão (lê o arquivo input/sample.txt)
   python main.py

   # Para um arquivo específico
   python main.py meu_curriculo.txt
   ```

3. O arquivo gerado estará em `output/resume.html`. Abra-o no navegador e imprima como PDF (`Ctrl + P`).

## Como Contribuir

1. Faça um Fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`).
3. Faça commit das mudanças (`git commit -m 'feat: Adiciona MinhaFeature'`).
4. Faça push para a branch (`git push origin feature/MinhaFeature`).
5. Abra um Pull Request.

## Licença

Distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
