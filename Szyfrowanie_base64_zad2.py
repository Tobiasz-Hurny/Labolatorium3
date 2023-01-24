import base64

tekst1 = input('Prosze wprowadzić tekst do zaszyfrowania base64\n') #użytkownik wpisuje string, który chce zaszyfrować
message_bytes = tekst1.encode('ascii') #w tym miejscu zamienia tekst na bajty
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

print(base64_message)

tekst2 = input('Prosze wprowadzić tekst do rozszyfrowania base64\n') #użytkownik wpisuje string, który chce zaszyfrować
message_bytes = tekst2.encode('ascii') #w tym miejscu zamienia tekst na bajty
base64_bytes = base64.b64decode(message_bytes)
base64_message = base64_bytes.decode('ascii')

print(base64_message)