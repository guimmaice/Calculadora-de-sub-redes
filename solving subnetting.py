def verif_class_ip(ip_values):
    if 0<=ip_values[0]<127 :
        return "IP de classe A"
    elif 128<=ip_values[0]<192: 
        return "IP de classe B" 
    elif 192<=ip_values[0]<224:
        return "IP de classe C"
    elif 224<=ip_values[0]<240:
        return "IP de classe D"
    elif 240<=ip_values[0]<256:
        return "IP de classe E"
    else:     
        return "IP de classe inexistente"     

def verif_mask(mask_value):
    if 0<=mask_value<=32:
        return True
    else:
        return False
 
def verif_ip_address(ip_values, mask_value_b):
    if len(ip_values)!=4 or mask_value_b==False:
        return "Endereço de IP inválido"
    else:
        for ip in ip_values:
            if ip<0 or ip>255 :
                return "Endereço de IP inválido"
            else:
                continue
        return "Endereço de IP válido"    

def calculator(mask_value):
    bits_0=2**(32-mask_value)
    hosts=bits_0-2
    #subnets=None

    if bits_0>256:
        for i in range(1,5,1):
            bits_0//=256
            if 0<=bits_0<=256:
                break

        num_sub_net=256//bits_0

        if mask_value==32:
            hosts=0
            return hosts, num_sub_net, bits_0
        else:
            return hosts, num_sub_net, bits_0
    else:
        num_sub_net=256//bits_0

        if mask_value==32:
            hosts=0
            return hosts, num_sub_net, bits_0
        else:
            return hosts, num_sub_net ,bits_0 

def subnetting(mask_value, ip_values, num_sub_net, sub_nets):
    sub_net_list=[]
    if 0<=mask_value<9:
        for i in range(0,num_sub_net,1):
            num=i*sub_nets
            rede=[num, 0, 0, 0]
            primeiro_host=[num, 0, 0, 1]
            ultimo_host=[num, 255, 255, 254]
            broadcast=[num, 255, 255, 255]
            sub_net_list.append({
                "rede":rede,
                "primeiro_host":primeiro_host,
                "ultimo_host":ultimo_host,
                "broadcast":broadcast })

        return sub_net_list
    
    elif 9<=mask_value<17:
        for i in range(0,num_sub_net,1):
            num=i*sub_nets
            rede=[ip_values[0], num, 0, 0]
            primeiro_host=[ip_values[0], num, 0, 1]
            ultimo_host=[ip_values[0], num+sub_nets-1, 255, 254]
            broadcast=[ip_values[0], num+sub_nets-1, 255, 255]
            sub_net_list.append({
                "rede":rede,
                "primeiro_host":primeiro_host,
                "ultimo_host":ultimo_host,
                "broadcast":broadcast })
        return sub_net_list
    
    elif 17<=mask_value<25:
        for i in range(0,num_sub_net,1):
            num=i*sub_nets
            rede=[ip_values[0], ip_values[1], num, 0]
            primeiro_host=[ip_values[0], ip_values[1], num, 1]
            ultimo_host=[ip_values[0], ip_values[1], num+sub_nets-1, 254]
            broadcast=[ip_values[0], ip_values[1], num+sub_nets-1, 255]
            sub_net_list.append({
                "rede":rede,
                "primeiro_host":primeiro_host,
                "ultimo_host":ultimo_host,
                "broadcast":broadcast })
        return sub_net_list
    
    elif 25<=mask_value<33:
        for i in range(0,num_sub_net,1):
            num=i*sub_nets
            rede=[ip_values[0], ip_values[1], ip_values[2], num]
            primeiro_host=[ip_values[0], ip_values[1], ip_values[2], num+1]
            ultimo_host=[ip_values[0], ip_values[1], ip_values[2], num+sub_nets-2]
            broadcast=[ip_values[0], ip_values[1], ip_values[2], num+sub_nets-1]
            sub_net_list.append({
                "rede":rede,
                "primeiro_host":primeiro_host,
                "ultimo_host":ultimo_host,
                "broadcast":broadcast })        

        return sub_net_list

def ip_insert():
    while True:
        ip_values=[]
        try:
            ip_value=input("insira o IP: ")
            ips=ip_value.strip().split(".")
            for ip in ips:
                num=int(ip)
                ip_values.append(num) 
        except ValueError as erro:
                print(f"Erro detectado: {erro}")
                     
        else:        
            return ip_values      
           
def mask_insert():
    while True:    
        try:
            mask_value=int(input("insira a máscara: "))  
        except ValueError as erro:
            print(f"Erro detectado: {erro}")
            print("A máscara de um IP é um valor inteiro entre 0 e 32")
            break
        else:    
            return verif_mask(mask_value), mask_value

def main():
    octetos=ip_insert()
    mask_value_b, valor_mascara=mask_insert()
    verif=verif_ip_address(octetos, mask_value_b)
    print(f" {verif} : {octetos}/{valor_mascara} ")
    if verif.upper().strip()=="ENDEREÇO DE IP VÁLIDO" :
        class_ip=verif_class_ip(octetos)
        print(class_ip)
        hosts, numero_sub_redes, sub_nets =calculator(valor_mascara)
        print(f"Número de hosts: {hosts} ")
        print(f"Número de sub-redes: {numero_sub_redes} ")
        lista_de_enderecos=subnetting(valor_mascara, octetos, numero_sub_redes, sub_nets)
        for rede in lista_de_enderecos:
            print(rede)
    else:
        main()

main()