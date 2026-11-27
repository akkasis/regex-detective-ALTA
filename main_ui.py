from rich.console import Console
from rich.panel import Panel
from rich.text import Text

import passes
passes_rounds = passes.rounds

import archive
archive_rounds = archive.rounds

all_rounds = passes_rounds + archive_rounds

console = Console(markup=False, highlight=False)
clues = []

console.print(Panel("Из лаборатории пропали секретные чертежи. Найдите вора.",
                    title="REGEX-ДЕТЕКТИВ", border_style="bright_red"))

for game_round in all_rounds:
    console.print()
    console.print(Panel(game_round.task, title=game_round.title, border_style="bright_cyan"))

    while True:
        pattern = console.input(Text("Введите регулярное выражение (? - подсказка): ", style="bold bright_yellow"))

        if pattern == "?":
            console.print("Подсказка: " + game_round.hint, style="bright_blue")
            continue

        success, message = game_round.check(pattern)

        if success:
            console.print(message, style="bold bright_green")
            console.print(Panel(game_round.clue, title="Улика", border_style="bright_green"))
            clues.append(game_round.clue)
            break

        console.print(message, style="bright_red")
        console.print("Попробуйте ещё раз.")

console.print()
console.print(Panel("\n".join(clues), title="Все улики собраны", border_style="bright_red"))
console.print("Вор - завхоз Громов. Дело закрыто!", style="bold bright_red")
