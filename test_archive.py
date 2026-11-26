from archive import round1, round2

success, message = round1.check(r"№\d{4}")
assert success
success, message = round1.check(r"№[0-9][0-9][0-9][0-9]")
assert success

success, message = round1.check(r"\d{4}")
assert not success
assert "2026" in message

success, message = round1.check("(№\\d{4}")
assert not success
assert "скомпилировать" in message

success, message = round2.check(r"агент_\d{2}")
assert success
success, message = round2.check(r"агент_[0-9][0-9]")
assert success

success, message = round2.check(r"агент_\d+")
assert not success
assert "агент_3" in message

success, message = round2.check("агент_[0-9")
assert not success
assert "скомпилировать" in message

print("Все проверки главы «Архив переписки» пройдены")
