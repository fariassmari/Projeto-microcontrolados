# 🧰 Nivelador de Obras Digital

Um aplicativo em Python que utiliza uma interface gráfica com **Tkinter** para exibir um **nível digital**, lendo dados de sensores via **porta serial** (como acelerômetros/giroscópios conectados a um Arduino).

## 📷 Visão geral

O projeto simula o funcionamento de um nível de bolha digital, exibindo visualmente a inclinação nos eixos **X** e **Y** em tempo real.

## ⚙️ Funcionalidades

- Conexão com dispositivos via porta serial (ex: Arduino)
- Leitura de ângulos em tempo real
- Representação gráfica do nível em um canvas
- Interface interativa com atualização dinâmica
- Encerramento seguro com fechamento automático da porta serial

## 🧠 Como funciona

O Arduino (ou dispositivo semelhante) envia dados seriais no seguinte formato:

O programa lê essa linha, extrai os ângulos, e atualiza a interface gráfica desenhando um círculo e uma linha que representa a inclinação.

## 🖥️ Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [pyserial](https://pypi.org/project/pyserial/)
- [Math](https://docs.python.org/3/library/math.html)

