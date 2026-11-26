from passes import round1, round2

success, message = round1.check(r"[A-Z]{2}-[0-9]{3}")
assert success
success, message = round1.check(r"[A-Z][A-Z]-\d\d\d")
assert success

success, message = round1.check(r"[A-Z]+-[0-9]{3}")
assert not success
assert "A-105" in message

success, message = round1.check("[A-Z")
assert not success
assert "скомпилировать" in message

success, message = round2.check(r"(GUEST|STAFF):\d{1,3}")
assert success
success, message = round2.check(r"(STAFF|GUEST):[0-9][0-9]?[0-9]?")
assert success

success, message = round2.check(r"GUEST|STAFF:\d{1,3}")
assert not success

success, message = round2.check("(GUEST|STAFF")
assert not success
assert "скомпилировать" in message

print("Все проверки главы «Бюро пропусков» пройдены")
