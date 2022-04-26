''' ipv4 e formado por 4 numeros separados por '.' que vao de 0-255
a    porem esses numeros sao 4 numeros com 8 bits---> 120.30.9.20,exemplos: 120=00010001, 30=00000101...
a             valores= 128 64 32 16 8 4 2 1       ip_ficticio= 10.20.12.45/26 
 separa o numero,pega numero mais proximo ou igual em valores-> 10- o 10 comeca no 8-> 128 64 32 16 8 4 2 1 
 oito somado com numero a direita se passar o valor bota 0                           resto e td 0   1 0 1 0
                                                                20                                1 0 1 0 0
                                                                12                                0 1 1 0 0
                                                                45                              1 0 1 1 0 1
entao fica 
10=00001010
20=00010100
12=00001100
45=00101101
O /26 apos o ip quer dizer 26 bits 1 abaixo da rede restante e 0
00001010 00010100 00001100 00101101
11111111 11111111 11111111 11000000 <--1*/26 o resto 0,mascara de sub-rede
para saber quantos hosts posso ter na rede (2**(quantidade de 0 na mascara sub-rede)-2)
calcular o octeto ta mascara so fazer igual no ip so que inverso no caso com todos '1' o numero e 255
11111111 11111111 11111111 11000000   sao 32 numeros
   255      255      255       192
00001010 00010100 00001100 00000000 ip da rede
    10       20       12      0   /26
00001010 00010100 00001100 00111111 broadcast inves de completar os ultimos 6 com 0 faz com 1 
   10        20       12       63  /26


 1-  receber um ip ok
 2- ver a mascara de sub-red ok
 3- ver o ip da rede ok
 4- ver o broadcast ok

 preciso agr fazer uma replace(ou outra forma para mudar valores em listas) no mult trocar os valores que estao em saves por 1 e os que nao estao por 0
                                                                                                                                    '''


class Ipv4():
    def cal_ipv4(ip, **kwargs):
        mult = [128, 64, 32, 16, 8, 4, 2, 1]
        ip_sep = ip.split('.')
        ip_int = [int(i) for i in ip_sep]
        saves = []
        valores_binarios = []
        ip_da_rede = ip.split('.')
        ip_da_rede.pop(3)

        ip_da_rede = ','.join(ip_da_rede)
        ip_da_rede = ip_da_rede.replace(',', '.')
        if 'cidr' in kwargs:
            cidr = kwargs
            mascara = list(cidr['cidr']*'1')
            resto = 32-len(mascara)
            qtd_ips_rede = 2**resto-2
            mascara += resto*'0'
            mascara = [int(i) for i in mascara]
            n = 8
            mascara_sep = [mascara[i:i + n] for i in range(0, len(mascara), n)]
            z = True
            indice_mascara = 0
            marcador_mascara = 0
            soma_mascara_subrede = []
            while z:
                if sum(mascara_sep[indice_mascara]) == 8:
                    mascara_sep[indice_mascara] = 255
                    indice_mascara += 1
                    continue
                else:

                    scan = mascara_sep[indice_mascara][marcador_mascara]
                    if scan == 1:
                        soma_mascara_subrede.append(mult[marcador_mascara])
                        marcador_mascara += 1
                        continue

                    else:
                        soma_mascara_subrede = sum(soma_mascara_subrede)
                        mascara_sep[indice_mascara] = soma_mascara_subrede
                        if len(mascara_sep) < 4:
                            indice_mascara += 1
                        else:
                            mascara_sub_rede = mascara_sep
                            mascara_sub_rede = str(mascara_sub_rede)
                            mascara_sub_rede = str(
                                mascara_sub_rede).strip('[]')
                            mascara_sub_rede = mascara_sub_rede.replace(
                                ',', '.')
                            z = False
        broadcast_ip = []
        broadcast_ip += (8-resto)*'0'
        broadcast_ip += resto*'1'
        broadcast_ip = [int(i) for i in broadcast_ip]
        broadcast_soma = []
        contador_broadcast = 0
        y = True
        while y:
            try:
                if broadcast_ip[contador_broadcast] == 1:
                    broadcast_soma.append(mult[contador_broadcast])
                    contador_broadcast += 1
                    continue
                elif broadcast_ip[contador_broadcast] == 0:
                    contador_broadcast += 1
                    continue
            except:
                broadcast_soma = sum(broadcast_soma)
                broadcast_soma = str(broadcast_soma)
                broadcast_ip = ip_da_rede+'.'+broadcast_soma
                y = False

        return print(f'''
                    IP:{ip}
                    Mascara: {mascara_sub_rede}
                    Rede: {ip_da_rede}
                    Broadcast: {broadcast_ip}
                    Prefixo: {cidr['cidr']}
                    Numero de IPs da rede: {qtd_ips_rede}''')


Ipv4.cal_ipv4('192.168.0.1', cidr=24)
