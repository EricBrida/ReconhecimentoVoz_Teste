# Integrantes 

- **Eric Bueno Corrêa Brida** | *Email Institucional: [eric.brida@fatec.sp.gov.br](mailto:eric.brida@fatec.sp.gov.br)*
- **Luigi Cordeiro de Oliveira** | *Email Institucional: [luigi.oliveira01@fatec.sp.gov.br](mailto:luigi.oliveira01@fatec.sp.gov.br)*
- **Rubia de Souza Moreira** | *Email Institucional: [rubia.moreira@fatec.sp.gov.br](mailto:rubia.moreira@fatec.sp.gov.br)*

# Sobre o código

Uma aplicação básica que faz o reconhecimento da voz após um *"beep"*, captura o mesmo em uma variável e faz uma pesquisa no google

# Tecnologias Utilizadas

[![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/docs)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://docs.python.org/pt-br/3/)

### Dependências:
- **[speech_recognition](https://pypi.org/project/SpeechRecognition/)**: Biblioteca para reconhecimento de voz, permitindo transcrever áudio em texto.
- **[webbrowser](https://docs.python.org/3/library/webbrowser.html)**: Módulo padrão do Python para abrir URLs no navegador padrão do sistema.
- **[tkinter](https://docs.python.org/3/library/tkinter.html)**: Biblioteca padrão para criar interfaces gráficas  (GUIs) em Python.
- **[winsound](https://docs.python.org/3/library/winsound.html)**: Modulo padrão do Python para gerar sons simples em sistemas Windows.
- **[pyaudio](https://people.csail.mit.edu/hubert/pyaudio/docs/)**: É uma biblioteca que fornece bindings para o PortAudio, permitindo a gravação e reprodução de áudio em tempo real em aplicações Python.

# Como Utilizar

#### No terminal e no diretório de sua escolha, de o seguinte comando:
```
git clone https://github.com/EricBrida/ReconhecimentoVoz_Teste.git
cd ReconhecimentoVoz_Teste
```

#### Após a clonagem do repositório, é uma boa índole criar um ambiente virtual para a instalação das dependências:

> [!NOTE]
> ***.venv** ou **.env** são opções viáveis para o nome de seu ambiente virtual.* </br>
> *Você pode selecionar o ambiente virtual pelo atalho **CTRL + SHIFT + P**, procurar por **"Python: Select Interpreter"** e buscar pelo .exe do venv.* </br>
> *O comando "pip install -r requirements.txt" fará a instalação de todas as dependências utilizadas no projeto.*

```
python -m venv <nome_ambiente_virtual>
<nome_ambiente_virtual>\Scripts\activate
pip install -r requirements.txt
```

> [!IMPORTANT]
> *Para rodar a aplicação é necessário que você execute diretamente pelo arquivo **"main.py"***

#### Caso execute pelo terminal: 
```
python main.py
```

#### Caso tenha as extensões do Python baixada em seu VSCode:
![RUN_PYTHON](img\RUN_PYTHON.png)
