#imports here
import argparse

def morse():
    pass

def cesar():
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Narzędzie do szyfrowania/odszyfrowania plików: Cezar lub Morse'
    )

    # tryb: encrypt vs decrypt
    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument('-e', '--encrypt', action='store_true',
                            help='uruchom tryb szyfrowania')
    mode_group.add_argument('-d', '--decrypt', action='store_true',
                            help='uruchom tryb odszyfrowywania')

    # algorytm: Cezar vs Morse
    cipher_group = parser.add_mutually_exclusive_group(required=True)
    cipher_group.add_argument('-c', '--caesar', action='store_true',
                              help='użyj szyfru Cezara')
    cipher_group.add_argument('-m', '--morse', action='store_true',
                              help='użyj kodu Morse’a')

    # opcja przesunięcia dla Cezara
    parser.add_argument('-n', type=int, default=3,
                        help='(Cezar) wartość przesunięcia liter (domyślnie 3)')

    # pliki wejściowy i wyjściowy
    parser.add_argument('input_file', help='ścieżka do pliku wejściowego')
    parser.add_argument('output_file', help='ścieżka do pliku wyjściowego')

    args = parser.parse_args()
    print(args)