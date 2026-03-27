🌐 Calculadora de Sub-redes IPv4

Este projeto é uma ferramenta desenvolvida em Python para automatizar o cálculo de sub-redes, facilitando a resolução de exercícios de Redes de Computadores II. O script valida endereços IP, identifica classes e gera listas detalhadas de sub-redes.



🚀 Funcionalidades

1.Validação de Endereço IP: Garante que o IP inserido tem 4 octetos e valores entre 0 e 255.

2.Tratamento de Exceções: Uso de blocos try/except para evitar falhas com entradas inválidas.

3.Identificação de Classe: Identifica automaticamente se o IP pertence às classes A, B, C, D ou E.

4.Cálculo de Sub-redes: Gera o endereço de Rede e o endereço de Broadcast para cada sub-rede com base na máscara CIDR.

5.Modularidade: Código organizado em funções específicas para facilitar a manutenção e leitura.


🛠️ Tecnologias Utilizadas

1.Python 3
2.Git & GitHub (Controlo de Versão)



📋 Como utilizar

1.Execute o ficheiro solving_subnetting.py.

2 Insira o endereço IP quando solicitado (ex: 192.168.1.0).

3.Insira o valor da máscara CIDR (ex: 24).



O programa exibirá o número de hosts, o número de sub-redes e a lista completa de endereços.
