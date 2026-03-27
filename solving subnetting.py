def verif_class_ip(ip_values):
    if ip_values[0]>0 and ip_values[0]<128 :
        return "IP de classe A"
    elif ip_values[0]>=128 and ip_values[0]<192: 
        return "IP de classe B" 
    elif ip_values[0]>=192 and ip_values[0]<224:
        return "IP de classe C"
    elif ip_values[0]>=224 and ip_values[0]<240:
        return "IP de classe D"
    elif ip_values[0]>=240 and ip_values[0]<256:
        return "IP de classe E"
    else:     
        return "IP de classe inexistente"     

def verif_mask(mask_value):
    if mask_value<33 and mask_value>=0:
        return True
    else:
        return False
 
def verif_ip_address(ip_values, mask_value_b):
    for ip in ip_values:
        if ip>255 or len(ip_values)!=4 or mask_value_b==False:
            return "Endereço de IP inválido"
        else:
            return "Endereço de IP válido"

def calculator(mask_value):
    bits_0=2**(32-mask_value)
    hosts=bits_0-2
    subnets=0
    
    if bits_0>256:
        for i in range(33):
            subnets=bits_0//256
            if subnets<256:
                break

        num_sub_net=256//subnets

        if mask_value==32:
            hosts=0
            return hosts, num_sub_net, subnets
        else:
            return hosts, num_sub_net, subnets
    else:
        num_sub_net=256//bits_0

        if mask_value==32:
            hosts=0
            return hosts, num_sub_net, bits_0
        else:
            return hosts, num_sub_net ,bits_0 

def subnetting(mask_value, ip_values, num_sub_net, sub_nets):
    sub_net_list=[]
    if mask_value>=0 and mask_value<9:
        for i in range(0,num_sub_net):
            num=i*sub_nets
            rede=[num, 0, 0, 0]
            broadcast=[num, 255, 255, 255]
            sub_net_list.append({
                "rede":rede,
                "broadcast":broadcast })

        return sub_net_list
    
    elif mask_value>=9 and mask_value<17:
        for i in range(0,num_sub_net,1):
            num=i*sub_nets
            rede=[ip_values[0], num, 0, 0]
            broadcast=[ip_values[0], num+sub_nets-1, 255, 255]
            sub_net_list.append({
                "rede":rede,
                "broadcast":broadcast })
        return sub_net_list
    
    elif mask_value>=17 and mask_value<25:
        for i in range(0,num_sub_net,1):
            num=i*sub_nets
            rede=[ip_values[0], ip_values[1], num, 0]
            broadcast=[ip_values[0], ip_values[1], num+sub_nets-1, 255]
            sub_net_list.append({
                "rede":rede,
                "broadcast":broadcast })
        return sub_net_list
    
    elif mask_value>=25 and mask_value<33:
        for i in range(0,num_sub_net,1):
            num=i*sub_nets
            rede=[ip_values[0], ip_values[1], ip_values[2], num]
            broadcast=[ip_values[0], ip_values[1], ip_values[2], num+sub_nets-1]
            sub_net_list.append({
                "rede":rede,
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
                #break       
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
    ip_values=ip_insert()
    mask_value_b, mask_value=mask_insert()
    verif=verif_ip_address(ip_values, mask_value_b)
    print(f" {verif} : {ip_values}/{mask_value} ")
    if verif.upper().strip()=="ENDEREÇO DE IP VÁLIDO" :
        class_ip=verif_class_ip(ip_values)
        print(class_ip)
        hosts, num_sub_net, sub_nets =calculator(mask_value)
        print(f"Número de hosts: {hosts} ")
        print(f"Número de sub-redes: {num_sub_net} ")
        sub_net_list=subnetting(mask_value, ip_values, num_sub_net, sub_nets)
        for net in sub_net_list:
            print(net)
    else:
        main()

main()