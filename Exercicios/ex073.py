times = ('Palmeiras','Santos','São Paulo','Atlético-MG','Botafogo',
'Athletico-PR','Flamengo','Bahia','Internacional','Goiás',
'Cruzeiro','Corinthians','Chapecoense','Ceará','Fluminense',
'Fortaleza','CSA','Grêmio','Avaí','Vasco')
print('='*80 + f'\n{"Tabela do Brasileiro 2019":^80}\n' + '=' *80)
print(f'Os 5 primeiros colocados são {times[:5]}\n'
      f'Os 4 ultimos colocados são {times[16:]}\n'
      f'Os times em ordem alfabetica {sorted(times)}\n'
      f'A chapecoense está na {times.index("Chapecoense")+1}ª colocação')
