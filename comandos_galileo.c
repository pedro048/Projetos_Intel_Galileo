//encontrar o ip na rede local(muda em cada rede)

curl ifconfig.me // ip público

ifconfig //ip local da máquina (2º linha inet)

hostname - I // ip local 

arp -a  // retorna todos os IPs e MACs conectado na rede



// conexão ssh é usada para acesso remoto a outro computador

ssh root@ip //root é o nome da máquina e depois do @ é o ip dela 

dpkg -l ssh // verifica se os micros tem o ssh

# apt-get install ssh  // instala o ssh nos micros



//enviando pacotes com scp 

// o caminho do arquivo precisa ser especificado, exemplo:  /var/lib/arquivos 

scp /var/lib/arquivos root@192.168.100.1:/home/damasceno 

/* 
 envia uma cópia da pasta arquivos para o computador com login root e ip: 192.168.100.1 salvando em uma pasta chama Damaceno


 para olhar o manual do comando: man scp 


 criar uma chave para comunicação entre os computadores:  ssh-keygen -t rsa

 depois de criada é só copiar para o computador conectado de forma remota

*/

/* passo a passo para carregar um programa na Galileo
   criar uma pasta em home/root
*/
// cria uma pasta na Galileo. mkdir serve para criar diretórios
root@galileo:~# mkdir ~/pedro 
// abri a pasta criada
root@galileo:~# cd ~/pedro 
// transferindo arquivo para o Galileu via scp
$ scp hello.c root@192.168.0.1:/home/root/pedro

/* 
quando o arquivo com o código estiver no Galileo, está tudo pronto 
para compilar. No caso de códiigo em C he necessario usar o GCC.
*/

root@galileo/ pedro:~# gcc hello.c -o hello
root@galileo/ pedro:~# ./hello



Minha rede:
// exemplo de possiveis IPs
ip: 191.253.169.196 (rede pública)

ip: 192.168.0.102 (pc na rede local)



Possivel rede local: 192.168.0.1__

Galileo com MAC: 98:4F:EE:01:11:AA, ip: 192.168.0.107



Comandos importantes para conexão:



nmap -sP 192.168.0.1/24 (mostra o ip das máquinas conectadas a rede local)

arp -a (aparece os ips com os respectivos MACs)



ssh root@192.168.0.107
