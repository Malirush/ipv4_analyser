                         
                                                                                                                                              

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
