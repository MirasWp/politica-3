candidatos = [
    'Lula', 'Bolsonaro', 'Marçal', 'Ciro', 'Simone', 'Soraya', 'Pablo gomes',
    'Anitta', 'Nikolas Ferreira', 'Batata'
]
partido = [
    'Pt', 'PSDP', 'LAL', 'CLR', 'TUR', 'STR', 'INT', 'BOOL', 'DEF', 'INP'
]
vice = [
    'Paulo henrique', 'Hanzo', 'Catin', 'Camille', 'Higor', 'Pablo', 'Rodrigo',
    'Gilmara', 'Valdir', 'Luan'
]
cargo = [
    'Presidente', 'Governador', 'Prefeito', 'Presidente', 'Governador',
    'Prefeito', 'Presidente', 'Governador', 'Presidente',
    'Presidente'
]
idade = ['37', '29', '22', '43', '45', '31', '28', '62', '43', '56', '54']

numero = int(input('Número do candidato: '))

if 1 <= numero <= 10:
    print(f'Seu candidato é: {candidatos[numero-1]}')
    print(f'Seu partido é: {partido[numero-1]}')
    print(f'Seu vice é: {vice[numero-1]}')
    print(f'Seu cargo é: {cargo[numero-1]}')
    print(f'Sua idade é: {idade[numero-1]}')
else:
    print('Número invalido, não temos esse candidato aqui')