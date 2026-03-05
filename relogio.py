import tkinter as tk
from datetime import datetime


# Dígitos em arte ASCII (7 segmentos), cada dígito tem 5 linhas de altura
DIGITS = {
    '0': [
        " ███ ",
        "█   █",
        "█   █",
        "█   █",
        " ███ ",
    ],
    '1': [
        "  █  ",
        " ██  ",
        "  █  ",
        "  █  ",
        " ███ ",
    ],
    '2': [
        " ███ ",
        "    █",
        " ███ ",
        "█    ",
        " ████",
    ],
    '3': [
        " ███ ",
        "    █",
        " ███ ",
        "    █",
        " ███ ",
    ],
    '4': [
        "█   █",
        "█   █",
        " ████",
        "    █",
        "    █",
    ],
    '5': [
        " ████",
        "█    ",
        " ███ ",
        "    █",
        " ███ ",
    ],
    '6': [
        " ███ ",
        "█    ",
        " ███ ",
        "█   █",
        " ███ ",
    ],
    '7': [
        " ████",
        "    █",
        "   █ ",
        "  █  ",
        " █   ",
    ],
    '8': [
        " ███ ",
        "█   █",
        " ███ ",
        "█   █",
        " ███ ",
    ],
    '9': [
        " ███ ",
        "█   █",
        " ████",
        "    █",
        " ███ ",
    ],
    ':': [
        "     ",
        "  █  ",
        "     ",
        "  █  ",
        "     ",
    ],
}


def build_ascii_time(time_str: str) -> str:
    """Monta a representação ASCII do horário."""
    lines = [""] * 5
    for char in time_str:
        digit_lines = DIGITS.get(char, ["     "] * 5)
        for i in range(5):
            lines[i] += digit_lines[i] + "  "
    return "\n".join(lines)


class RelogioApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Relógio Python")
        self.root.configure(bg="#1a1a2e")
        self.root.resizable(False, False)

        # Título
        self.label_titulo = tk.Label(
            root,
            text="RELÓGIO",
            font=("Courier", 14, "bold"),
            fg="#e94560",
            bg="#1a1a2e",
            pady=10,
        )
        self.label_titulo.pack()

        # Display do horário em ASCII
        self.label_hora = tk.Label(
            root,
            text="",
            font=("Courier", 18, "bold"),
            fg="#00d4ff",
            bg="#1a1a2e",
            justify="center",
            padx=20,
            pady=10,
        )
        self.label_hora.pack()

        # Data por extenso
        self.label_data = tk.Label(
            root,
            text="",
            font=("Courier", 12),
            fg="#a8dadc",
            bg="#1a1a2e",
            pady=8,
        )
        self.label_data.pack()

        # Linha separadora decorativa
        self.label_sep = tk.Label(
            root,
            text="─" * 40,
            font=("Courier", 10),
            fg="#e94560",
            bg="#1a1a2e",
        )
        self.label_sep.pack()

        # Rodapé
        self.label_footer = tk.Label(
            root,
            text="Pressione Alt+F4 para fechar",
            font=("Courier", 9),
            fg="#555577",
            bg="#1a1a2e",
            pady=6,
        )
        self.label_footer.pack()

        self.atualizar()

    def atualizar(self):
        agora = datetime.now()

        # Horário no formato HH:MM:SS
        hora_str = agora.strftime("%H:%M:%S")
        ascii_hora = build_ascii_time(hora_str)
        self.label_hora.config(text=ascii_hora)

        # Data formatada em português
        dias_semana = [
            "Segunda-feira", "Terça-feira", "Quarta-feira",
            "Quinta-feira", "Sexta-feira", "Sábado", "Domingo",
        ]
        meses = [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro",
        ]
        dia_semana = dias_semana[agora.weekday()]
        mes = meses[agora.month - 1]
        data_str = f"{dia_semana}, {agora.day:02d} de {mes} de {agora.year}"
        self.label_data.config(text=data_str)

        # Atualiza a cada 1 segundo
        self.root.after(1000, self.atualizar)


if __name__ == "__main__":
    root = tk.Tk()
    app = RelogioApp(root)
    root.mainloop()
