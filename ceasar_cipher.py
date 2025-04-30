def caesar_encrypt(text, shift):
    result = []
    for ch in text:
        if 'A' <= ch <= 'Z':
            offset = ord('A')
            result.append(chr((ord(ch) - offset + shift) % 26 + offset))
        elif 'a' <= ch <= 'z':
            offset = ord('a')
            result.append(chr((ord(ch) - offset + shift) % 26 + offset))
        else:
            result.append(ch)
    return ''.join(result)


def caesar_decrypt(text: str, shift: int) -> str:
    return caesar_encrypt(text, -shift)

