# data - campo 0
# ip - campo 2
# status - campo 7
# pagina - campo 6
# navegador - campo 5

try: 
    fd = open ("try_on-2017-11-13.txt", "r")
    fd.readline()
    logs = []
    for log in fd:
        log = log.split()
        logs.append ((log[0], log[2], log[5], log[6], log[7]))
    fd.close()
    
    # dicionario em que:
    #   chave é o momento (data/hora/mm/ss) 
    #   valor é #acessos naquele momento
    data_acessos = {}
    for log in logs:
        momento = log[0]
        data_acessos[momento] = data_acessos.get(momento, 0) + 1
    mais_acessos_data = max(data_acessos.items(), key=lambda x: x[1])
    print ("Momento de maior acesso:")
    print (f"\t{mais_acessos_data[0][1:]} -> {mais_acessos_data[1]}")

    ip_acessos = {}
    for log in logs:
        ip = log[1]
        ip_acessos[ip] = ip_acessos.get(ip, 0) + 1
    mais_acessos_ip = max(ip_acessos.items(), key=lambda x: x[1])
    print ("IPs com mais acessos:")
    print (f"\t{mais_acessos_ip[0]} -> {mais_acessos_ip[1]}")

    
    print ("Paginas nao atendidas", 
           len(list(filter (lambda log: log[4] != "200",  logs))))

    ips = list(map (lambda log: log[1], logs))
    print (ips)
    
except FileNotFoundError as f_nfound:
    print ("Arquivo nao encontrado")