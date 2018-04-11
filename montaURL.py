import datetime

a = datetime.date.today().year
m = datetime.date.today().month
d = datetime.date.today().day - 1

if m == 1:
    mes = 'JAN'
    mesPasta = 'Janeiro'
elif m == 2:
    mes = 'FEV'
    mesPasta = 'Fevereiro'
elif m == 3:
    mes = 'MAR'
    mesPasta = 'Mar%C3%A7o'
elif m == 4:
    mes = 'ABR'
    mesPasta = 'Abril'
elif m == 5:
    mes = 'MAI'
    mesPasta = 'Maio'
elif m == 6:
    mes = 'JUN'
    mesPasta = 'Junho'
elif m == 7:
    mes = 'JUL'
    mesPasta = 'Julho'
elif m == 8:
    mes = 'AGO'
    mesPasta = 'Agosto'
elif m == 9:
    mes = 'SET'
    mesPasta = 'Setembro'
elif m == 10:
    mes = 'OUT'
    mesPasta = 'Outubro'
elif m == 11:
    mes = 'NOV'
    mesPasta = 'Novembro'
elif m == 12:
    mes = 'DEC'
    mesPasta = 'Dezembro'

if m < 10:
    if d < 10:
        enderecoXLSX = 'https://cdre.ons.org.br/CDRE%20%20Processo%20Relatrio%20Dirio%20da%20Situao%20HidrulicoH/'+'RDH_'+ str(a) + '/0'+ str(m) + '_'+ mesPasta+ '/RDH0'+ str(d) + mes+ '.xlsx'
    else:
        enderecoXLSX = 'https://cdre.ons.org.br/CDRE%20%20Processo%20Relatrio%20Dirio%20da%20Situao%20HidrulicoH/'+'RDH_'+ str(a) + '/0'+ str(m) + '_'+ mesPasta+ '/RDH'+ str(d)+ mes+ '.xlsx'
else:
    if d < 10:
        enderecoXLSX = 'https://cdre.ons.org.br/CDRE%20%20Processo%20Relatrio%20Dirio%20da%20Situao%20HidrulicoH/'+'RDH_'+ str(a) + '/'+ str(m) + '_'+ mesPasta+ '/RDH0'+ str(d)+ mes+ '.xlsx'
    else:
        enderecoXLSX = 'https://cdre.ons.org.br/CDRE%20%20Processo%20Relatrio%20Dirio%20da%20Situao%20HidrulicoH/'+'RDH_'+ str(a) + '/'+ str(m) + '_'+ mesPasta+ '/RDH'+ str(d)+ mes+ '.xlsx'

print(enderecoXLSX)