import re

from game_round import Round


class PassRound(Round):
    def __init__(self, title, task, hint, clue, valid_codes, fake_codes):
        super().__init__(title, task, hint, clue)
        self.valid_codes = valid_codes
        self.fake_codes = fake_codes

    def check(self, pattern):
        try:
            regex = re.compile(pattern)
        except re.error as error:
            return False, "Шаблон не удалось скомпилировать: " + str(error)

        for code in self.valid_codes:
            if not regex.fullmatch(code):
                return False, "Ваш шаблон отклонил действительный пропуск " + code

        for code in self.fake_codes:
            if regex.fullmatch(code):
                return False, "Ваш шаблон принял поддельный пропуск " + code

        return True, "Верно! Шаблон отличает настоящие пропуска от поддельных."


round1 = PassRound(
    "Дело № 1. Поддельный пропуск",
    "Код состоит из двух заглавных латинских букв,\n"
    "дефиса и трёх цифр от 0 до 9.\n\n"
    "Действительные коды: AB-042, ZX-105\n"
    "Поддельные коды:     ab-042, A-105, AB-42, AB-1234",
    "Сколько раз повторить символ, пишут в фигурных скобках: [A-Z]{2}",
    "Ночью кто-то прошёл в лабораторию по пропуску QW-713, выданному без подписи.",
    ["AB-042", "ZX-105", "QW-713", "MN-000"],
    ["ab-042", "A-105", "AB-42", "AB-1234", "ABC-123", "AB042", "Ab-999", "AB-12a"],
)

round2 = PassRound(
    "Дело № 2. Пропуск сотрудника",
    "Код состоит из слова GUEST или STAFF (заглавными буквами),\n"
    "двоеточия и от 1 до 3 цифр.\n\n"
    "Действительные коды: GUEST:7, STAFF:123\n"
    "Поддельные коды:     guest:7, STAFF:, STAF:12, STAFF:1234",
    "Выбор из двух слов пишут через | и берут в скобки: (A|B)",
    "Пропуск QW-713 оформил сотрудник с кодом STAFF:42.",
    ["GUEST:7", "STAFF:123", "STAFF:42", "GUEST:99"],
    ["guest:7", "STAFF:", "STAF:12", "STAFF:1234", "VIP:12", "STAFF-12", "GUESTSTAFF:1", "STAFF:12a"],
)

rounds = [round1, round2]
