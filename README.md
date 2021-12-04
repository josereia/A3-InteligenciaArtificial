 # A3 UnoTurbo16Cilindros

 ### Humano X IA
###### Este projeto tem como objetivo uma partida de jogo de cartas Uno, entre um humano e uma Inteligência Artificial

## Requisito para conseguir executar o jogo!

###### Ter o Phyton instalado na sua maquina https://www.python.org/downloads/

## Tutorial para iniciar o jogo!

###### Em ambiente Windows: Na pasta do jogo, execute no prompt de comando o seguinte comando:

`py main.py`

###### Em ambiente Linux: Na pasta do jogo, execute no terminal o comando:

`python3 main.py`

# Regras do jogo https://copag.com.br/blog/detalhes/uno

## Conteúdo: 112 cartas de jogo, sendo: 

###### ► 19 Cartas Azuis - 0 a 9;  
###### ► 19 Cartas Verdes - 0 a 9;  
###### ► 19 Cartas Amarelas - 0 a 9;  
###### ► 19 Cartas Vermelhas - 0 a 9;  
###### ► 8 Cartas Comprar Duas Cartas - 2 de cada cor;
###### ► 8 Cartas Inverter - 2 de cada cor; 
###### ► 8 Cartas Pular - 2 de cada cor, 
###### ► 4 Cartas Curinga; 
###### ► 4 Cartas Curinga Comprar Quatro Cartas; 
###### ► 1 Carta Curinga Trocar as Mãos; 
###### ► 3 Cartas Curinga Branca para Personalizar. 

## Objetivo do Jogo:

###### Seja o primeiro jogador a se livrar de todas as suas cartas em cada rodada e ganhe pontos pelas cartas que sobram em poder dos seus adversários. Os pontos de cada rodada vão sendo acumulados e o primeiro jogador a fazer 500 pontos será o vencedor. 


## Preparação: 


###### 1. Cada jogador tira uma carta. Aquele que tirar o número mais alto fará a distribuição. 
###### 2. O jogador que estiver distribuindo as cartas embaralha e distribui 7 cartas para cada um (se as cartas Curinga Branca para Personalizar ainda não estiverem escritas, deixe-as de fora do jogo). 
###### 3. As cartas restantes devem ser colocadas viradas para baixo, formando a pilha de Compras. 
###### 4. A carta superior da pilha de Compras é virada para formar uma pilha de Descarte. 

###### Observação: Se qualquer uma das Cartas de Ação (símbolos) for virada para dar início à pilha de Descarte, consulte as FUNÇÕES DAS CARTAS DE AÇÃO para ler instruções especiais. 


## Vamos Jogar:

###### O jogador à esquerda de quem estiver distribuindo as cartas começa o jogo, e o jogo deverá seguir em sentido horário. Na sua vez, você deve combinar uma carta da sua mão com aquela no alto da pilha de Descarte, seja por número, cor ou símbolo (os símbolos representam Cartas de Ação; consulte FUNÇÕES DAS CARTAS DE AÇÃO). 


###### Exemplo: Se a carta na pilha de Descarte for um 7 Azul, o jogador deve jogar uma carta Azul de qualquer número, ou um número 7 de qualquer cor. Se o jogador não tiver uma carta que combine, deve comprar uma na pilha de Compras. Se a nova carta servir, ele pode jogá-la na mesma rodada. Caso contrário, passará a vez para o próximo jogador. O jogador não pode jogar uma carta que já estava na sua mão antes de fazer a compra. 


## Funções das Cartas de Ação:


###### Comprar Duas Cartas - Quando esta carta for jogada, o próximo jogador deve comprar 2 cartas e perde a vez. Ela apenas pode ser jogada sobre uma cor que combine ou sobre outra carta Comprar 2. A mesma regra se aplica caso ela seja virada no início do jogo. 


###### Inverter - Ao descartar esta carta, o sentido do jogo é invertido (se estiver indo para a esquerda, muda para a direita e vice-versa). Ela apenas pode ser jogada sobre uma cor que combine ou sobre outra carta Inverter. Se a carta for virada no início do jogo, aquele que distribuiu as cartas joga primeiro e o jogo continua no sentido anti-horário ao invés de horário. 


###### Pular - Quando você joga esta carta, o próximo jogador é 'pulado' (perde a vez). Ela apenas pode ser jogada sobre uma cor que combine ou sobre outra carta Pular. Se uma carta Pular for virada no início do jogo, o jogador à esquerda daquele que distribuiu é pulado. Neste caso, o jogador à esquerda dele começará.


###### Curinga - Ao jogar esta carta, você escolhe a cor que continuará o jogo (pode ser qualquer cor, inclusive a que estava sendo jogada antes do Curinga). Você pode jogar um Curinga na sua vez, mesmo que tenha outra carta que combine na mão. Se o Curinga for virado no começo da partida, a pessoa à esquerda daquele que distribuiu as cartas escolhe com qual cor o jogo deve começar. 


###### Curinga Comprar Quatro Cartas - Ao jogar esta carta, você pode escolher a cor a ser jogada, além de fazer com que o próximo jogador tenha que comprar 4 cartas da pilha de Compras, perdendo também a vez. Mas há um detalhe! Esta carta só pode ser jogada quando você não tiver outra carta que combine com a cor da pilha de descarte (porém, ela pode ser descartada se você tiver uma carta com o número que combine ou outra Carta de Ação). Se ela for virada no começo do jogo, coloque-a no meio do monte e pegue outra carta. 


###### Observação: Caso suspeite que uma carta Curinga Comprar 4 tenha sido jogada contra você de forma desonesta (por exemplo, quando o jogador possuir uma carta de cor correspondente), você pode desafiá-lo. O jogador desafiado deve mostrar as cartas que tem para a pessoa que o desafiou. Se ele trapaceou, é ele quem deverá comprar as 4 cartas. Entretanto, se o jogador desafiado não trapaceou, você deve comprar as 4 cartas e mais 2 cartas.


###### Curinga Trocar as Mãos - Esta carta é um exemplo de algo que você pode fazer para personalizar suas próprias cartas brancas. Ao jogar esta carta, você pode escolher a cor a ser jogada a seguir além de trocar as suas cartas com as cartas de outro jogador. Se ela for virada no começo do jogo, coloque-a no meio do monte e pegue outra carta. 


###### Curinga Branca para Personalizar - Esta carta vale como um Curinga além de permitir que os jogadores escrevam à lápis qualquer regra que desejarem. Se ela for virada no começo do jogo, coloque-a no meio do monte e pegue outra carta. 


###### Finalizando: Ao jogar sua penúltima carta, você deve gritar "UNO" para indicar que você só tem uma carta na mão. Se não gritar "UNO' e alguém perceber antes do próximo jogador começar a jogar, você terá que comprar duas cartas. Quando um jogador tiver acabado com suas cartas, a rodada termina. Os pontos são então somados (ver PONTUAÇÃO) e o jogo começa novamente. Caso a última carta jogada em uma rodada seja Comprar Duas Cartas ou Curinga Comprar 4 Cartas, o próximo jogador deve comprar 2 ou 4 cartas, de acordo com a ação comandada. Elas serão contadas na soma de pontos. A carta Curinga Trocar as Mãos não pode ser jogada como a última carta. Caso nenhum jogador tenha terminado suas cartas quando a pilha de Compras acabar, a pilha de Descarte deverá ser embaralhada novamente para que o jogo continue. 

 

## Pontuação:


###### ► Todas as cartas numeradas (0 a 9): Valor Nominal; 
###### ► Comprar Duas Cartas: 20 Pontos; 
###### ► Inverter: 20 Pontos; 
###### ► Pular: 20 Pontos; 
###### ► Curinga: 50 Pontos; 
###### ► Curinga Comprar Quatro Cartas: 50 Pontos; 
###### ► Curinga Trocar as Mãos: 50 Pontos; 
###### ► Curinga Branca para Personalizar: 50 Pontos. 

###### Se após a contagem for constatado que nenhum jogador alcançou 500 pontos, será necessário embaralhar novamente e iniciar uma nova rodada. 


## Vencendo o jogo:

###### O ganhador é o primeiro a marcar 500 pontos. 


## Contagem de pontos alternativa:

###### Outra forma de contabilizar a pontuação é marcar os pontos das cartas que sobram com cada jogador no final de cada rodada. Quando um jogador alcançar 500 pontos, aquele com a menor pontuação será o vencedor. 




