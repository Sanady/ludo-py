'''
Projekt: Clovece nezlobsa
Vypracoval: Ivan Rener
'''

from random import SystemRandom
import math


'''==================================================================================================================
--->>> INICIALIZACIA PROGRAMU A MINI POMOCNE FUNKCIE
====================================================================================================================='''

''' P: Kazdy z hracov ktory zacne hrat tuto hru ma 3 sance zavrtiet kocku pokial nedostane cislo 6 a nevihodi figurku z domceku na cestu'''
''' Funkcia Ocist: Cestenie obrazovky pomocou printovania novych riadkov. 
    Funkcionalita: funguje to na princip for ciklu ktory zbehne kolko krat je to zadane v parametri.'''
def clearScreen(n):
    for i in range(0, n):
        print('\n');


'''Funkcia pauseGame: Je tu preto aby dalo casu ucastnikovy si pekne pozriet situaciu pri hrani
   Funkcionalita: Easy princip, proste zadame si na input tlacitko enter.'''

def pauseGame():
    input('Stlacte ENTER pre pokracovanie...')


'''Pred zaciatkom hrania a vobec vykreslovania hracieho posla, potrebujeme vycistit hracie pole timto sposobom.'''
clearScreen(20)

'''Vstupna hodnota hracieho pola, aka velkost toho hracieho pola ma bit, ako mini navod'''
print('Vstupna hodnota hracieho pola:')
print('NOTE: Vstupna hodnota hracieho pola musi byt cislo 5 alebo vacsie neparne cislo!\n\n\r')
'''Zadavanie hodnoty do premennej, cize vlastne velkost sachovnice:'''
sachSize = int(input('N = '))


'''Tato sada if funkcii vlastne overuje ze ci je podmienka hore uvedena v navode dodrzana, ak ano kod pokracuje ak nie, 
    cize ak je velkost tejto nasej sachovnice mensia ako 5, pritneme error ktory si sami napiseme a automaticky pridame
    velkost sachovnice kodom cize velkost sachovnice je 9.
    Druhy else if je vlastne preto tu, aby overil ze ci je velkost sachovnice neparne cislo, ak nie tak vyprintujeme 
    error a manualne kodom pridame do tej nasej sachovne + 1 cize zvecime sachovnicu o jedna a tim padom dostaneme
    neparne cislo.'''
if (sachSize < 5):
    print('WARNING: nespravne zadane N-ko, cislo N musi byt neparne cislo a vacsie ako 4,')
    print('kedze ste zadali nespravne cislo, vygeneruje sa cislo 9.')
    sachSize = 9
elif (sachSize % 2 == 0):
    print('WARNING: nespravne zadane N-ko, cislo N musi byt neparne cislo,')
    print('namiesto zadaneho cisla ', sachSize, ' pouzijeme ', sachSize + 1)
    sachSize += 1

'''NOTE: nasledovne premenne zvazime ze su vlastne ako ked by definy, cize konstaty ktore nam sluzia
        na lepsie orientovanie v kode!'''
MAX_PLAYERS = int((sachSize - 3) / 2)
AVERAGE_POS = int((sachSize - 1) / 2)
LENGTH = (AVERAGE_POS * 8)

'''Nasledovna cast kodu ukazuje na to ako sa vlastne hraci tak zvane definuju, cize hrac A bude 0-ty hrac v poradi
    a prvy hrac bude B-cko, cize ako ked by nejake amatericke kodovanie tich hracov podla pismen.'''
player = int(0) #Cize vlastne v tejto casti tohto kodu sa urcuje ze 0-ty hrac bude A a 1-vy bude B-cko
playersFigure = {0: 'A', 1: 'B'}

'''Dalsia premenne mi bude urcovat vlastne kde sa figurka bude nachadzat, ci vlastne sa nachadza v domceku ci
na ceste alebo ci este vobec ani neni na ceste. To overujem pomocou tohto kusu kodu,
    Definicie: -2: je v domecku
              -1: nie je na ceste
              0 do n-1: figurka je na ceste'''
playersFigureTravel = [[int(-1) for i in range(MAX_PLAYERS)],
                       [int(-1) for j in range(MAX_PLAYERS)]]

'''Tato premenne tak zvana kocka je vlastne kocka ktora sa bude pouzivat na generovanie hodnoty, cize simulovanie
hadzanie kocky'''
kocka = int(0)  # Hodnoty kocky (hodnoty od 1 - 6)

'''Premmenna hraciePole je vlastne zastupny symbol.
    Pomocou tejto premennej sa mozeme odkazovat na funkcie.'''
hraciepole = None


'''==================================================================================================================
--->>> POMOCNE FUNKCIE
====================================================================================================================='''

''' Funkcia gensachovnicu: funkcia ktoru som naprogramoval je pre generovanie hracieho pola pre uzivatela alebo klienta.
    Pomocou tejto funkcie hrac bude vygenerovane pole ale nie vypisane. 
    Funkcionalita: Pomocou parametra N, vykreslujem maticu N x N, cize hracie pole N x N'''
def gensachovnicu(k):
    '''Inicializacia premennej hraciPoligon.
    Cize na zaciatku kodu mame prazdnu maticu do ktorej si vlastne naplnime hracie pole.'''
    hraciPoligon = [[' ' for x in range(sachSize)]
                        for y in range(sachSize)]
    ''''''
    for i in range(k):
        ''''''
        for j in range(k):
            '''Pridavanie prazdnych miest na miesta kde niesu hviezdicky cize
            kde uzivatel nema pristup.'''
            hraciPoligon[i][j] = ' '

            '''Konrolovanie vo vsetkych 4-oh smeroch
            hore/dole/lavo/pravo
            a pridavanie v tych miestach namiesto prazdneho miesto pridavame * a pomocou toho vlastne zaciname
            vykreslovat cestu.'''
            '''Pomocout tohto ifu vieme vlastne kde mame davat *'''
            if (k - 1) / 2 == i + 1 or (k - 1) / 2 == j + 1 or (k + 1) / 2 == i or (k + 1) / 2 == j:
                ''''''
                hraciPoligon[i][j] = '*'

    '''V kode ktory nasleduje robime jednoduchu vec a to ze vlastne naplname
    prazdne miesta cize medzeri so hviezdickami, cize spajame hraci poligon (cestu).'''
    hraciPoligon[0][AVERAGE_POS] = '*'
    '''Cize na hornej casti matice, vlastne na prvom riadku na strede matice si zapisujeme *
    '''
    hraciPoligon[AVERAGE_POS][0] = '*'
    '''Na prvom stplci v strede si zapisujeme *
    '''
    hraciPoligon[k - 1][AVERAGE_POS] = '*'
    '''Na poslednom riadku a v strete si zapisujeme *
    '''
    hraciPoligon[AVERAGE_POS][k - 1] = '*'
    '''Na poslednom stlpci a v strede si davame *'''

    '''Pomocou tohto for cyklu si vlastne definujeme domceky.
        For cyklom prejdem od 1 a az po maximalni pocet panacikov posunutich o 1'''
    for i in range(1, MAX_PLAYERS + 1):
        '''Domcek ktory sa nachadza hore
        '''
        hraciPoligon[i][AVERAGE_POS] = 'D'
        '''Domcek ktory sa nachadza dolu:
        '''
        hraciPoligon[k - (i + 1)][AVERAGE_POS] = 'D'
        '''Domcek ktory sa nachadza v lavo:
        '''
        hraciPoligon[AVERAGE_POS][i] = 'D'
        '''Domcek ktory sa nachadza v pravo:
        '''
        hraciPoligon[AVERAGE_POS][k - (i + 1)] = 'D'
    '''Naplnenie streda s hodnotou X
    '''
    hraciPoligon[AVERAGE_POS][AVERAGE_POS] = 'X'
    '''A na koniec vratime hracie pole
    '''
    return hraciPoligon
'''=====================================================================================================================
====================================================================================================================='''

'''Funkcia showPlayerOnPlayableField: funkcia ma za ulohu ukazat na poli kde sa hrac nachadza, vlastne na akej pozicii
    Logiku ktoru som pouzil si mislim ze je mozne aj nejako inak spravit ale momentalne sa mi toto riesenie
    tohto problemu zdalo najlepsie:'''
def showPlayerOnPlayableField(player=0, pos=0):
    '''Hrac 0 cize hrac A, ktory vlastne zacina z 0, cize zacina z inej pozicii
    ako hrac B cize hrac 1, vlastne zacina z druhej strany hracieho pola.'''
    if (player == 1):
        pos = (player + (LENGTH / 2))
        pos = pos % LENGTH

    a = 0
    b = AVERAGE_POS - 1

    '''Na toto som myslel ked som hore napisal ze je lepsi pristup ako tento problem z vizualizaciou hraca na
    hracom poli resit.'''
    if (pos >= 0 and pos < 2):
        ''''''
        a = 0
        ''''''
        b = AVERAGE_POS - 1 + (pos)
        ''''''
    elif (pos < (2 + AVERAGE_POS)):
        ''''''
        a = (pos - 2)
        ''''''
        b = AVERAGE_POS + 1
        ''''''
    elif (pos < (2 + AVERAGE_POS + AVERAGE_POS) - 1):
        ''''''
        a = AVERAGE_POS - 1
        ''''''
        b = AVERAGE_POS + 1 + (pos - (2 + AVERAGE_POS) + 1)
        ''''''
    elif (pos < (3 + AVERAGE_POS + AVERAGE_POS)):
        ''''''
        a = AVERAGE_POS - 1 + (pos - (2 + AVERAGE_POS + AVERAGE_POS - 2))
        ''''''
        b = sachSize - 1
        ''''''
    elif (pos < (2 + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS)):
        ''''''
        x = (2 + AVERAGE_POS + AVERAGE_POS)
        ''''''
        a = AVERAGE_POS + 1
        ''''''
        b = sachSize - 1 - (pos - x)
        ''''''
    elif (pos < (2 + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS) - 1):
        ''''''
        x = (2 + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS) - 1
        ''''''
        a = AVERAGE_POS + 1 + (pos - x)
        ''''''
        b = AVERAGE_POS + 1
        ''''''
    elif (pos < (3 + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS)):
        ''''''
        x = (AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS)
        ''''''
        a = sachSize - 1
        ''''''
        b = AVERAGE_POS + 1 - (pos - x)
        ''''''
    elif (pos < (2 + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS)):
        ''''''
        x = (2 + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS)
        ''''''
        a = sachSize - 1 - (pos - x)
        ''''''
        b = AVERAGE_POS - 1
        ''''''
    elif (pos < (1 + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS)):
        ''''''
        x = (2 + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS) - 1
        ''''''
        a = AVERAGE_POS + 1
        ''''''
        b = AVERAGE_POS - 1 - (pos - x)
        ''''''
    elif (pos < (3 + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS)):
        ''''''
        x = (AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS)
        ''''''
        a = AVERAGE_POS + 1 - (pos - x)
        ''''''
        b = 0
        ''''''
    elif (pos < (2 + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS)):
        ''''''
        x = (2 + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS)
        ''''''
        a = AVERAGE_POS - 1
        ''''''
        b = 0 + (pos - x)
        ''''''
    elif (pos < (AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS)):
        ''''''
        x = (2 + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS + AVERAGE_POS) - 1
        ''''''
        a = AVERAGE_POS - 1 - (pos - x)
        ''''''
        b = AVERAGE_POS - 1
        ''''''
    elif (pos >= LENGTH):
        ''''''
        print('Hrac je v domceku.')
        ''''''
        return
    ''''''
    hraciepole[int(a)][int(b)] = playersFigure[player]
    return


'''=====================================================================================================================
====================================================================================================================='''
'''Funkcia tlacsachovnice: v tomto kode hore sme si najprv spravili funkciu ktora nam hracie pole alebo sachovnicu 
vygenerovalo, ale po generenovai sme si ju nikde nevypisali, preto je tu tato funkcia, ktora to spravi za nas, 
cize vykresli hracie pole na obrazovku uzivatela.'''
def tlacsachovnice(hraciPoligon):
    '''Pred akym kolvek novym vykreslovanim, najprv si vymazeme vsetko z obrazovky pomocou ClearScreen funkcie
    ktoru sme si napisali na zaciatku kodu.
    '''
    clearScreen(15)
    '''V tomto for cikly si vymazavame figurky s hracieho pola.'''
    for i in range(sachSize):
        for x in range(sachSize):
            '''Pomocou tichto forou prejdeme celou maticou:
            '''
            if (((i >= 1 and i <= 4) or (i <= (sachSize - 2) and i >= (sachSize - 5))) and (x == AVERAGE_POS)):
                continue
            '''V tomto if si vlastne nahradzame hraca z hviezdickov, cize ak sa hrac posunie o niekolko poli vopred
            namiesto Aciek a Bciek tam dame hviezdu.'''
            if (hraciPoligon[i][x] == 'A' or hraciPoligon[i][x] == 'B'):
                '''Ak hrac na poligne je rovny A alebo B potom na xtej pozicii vypis *
                '''
                hraciPoligon[i][x] = '*'
    '''V dalsom for cykle ktory sa nachadza popot nas komentar vlastne pridavame vsetky figurky na cestu do matice
    ktoru mame vygenerovanu.'''
    for player in range(2):
        for figure in range(MAX_PLAYERS):
            '''Prejdeme cez celi pocet hracov:
            '''
            if (playersFigureTravel[player][figure] >= 0) and (playersFigureTravel[player][figure] < LENGTH):
                '''A pomocou podmienky zistime ze ci hrac uz ma nejaku figurku na hracom poli:
                '''
                showPlayerOnPlayableField(player, playersFigureTravel[player][figure])
    '''Kod ktory je popot tento komentar robi to ze vypise najvysie poradove cislo:
    '''
    print('', end=' ')
    '''Pomocou for cyklu prejdem celou velkostou sachovnice:
    '''
    for i in range(sachSize):
        '''Limitujeme ich od 0-9
        '''
        print(i % 10, end=' ')
    print('')
    '''prikazovanie celej matice v dalsom fore:
    '''
    for i in range(sachSize):
        '''Zase prejdeme celou velkostou celej matice
        '''
        print(i % 10, end=' ')
        '''Limitujeme ich od 0-9
        '''
        for x in range(sachSize):
            '''Prejdeme zase celou velkostou matice
            '''
            print(str(hraciPoligon[i][x]), end='')
            '''A vypiseme hraciu plochu alebo hraci poligon
            '''
            print(' ', end='')
            '''Medzeri vypiseme tam kde hrac neprechadza cize na miesta 
            na ktore hrac vobec nema pristup:'''
        print('')  # Po defaulte, python dava \n na konci print

    print('')
    print('')


'''=====================================================================================================================
====================================================================================================================='''
'''Funkcia findPlayerOnPlayableField: je tu na to vlastne aby sme aby nasli poziciu na ktorej sa hrac nachadza
cize hladanie hraca na hracej ploche. (1 - 4 | 1 = prvy, 2 = druhy, ............)'''
def findPlayerOnPlayableField(player, figure):
    '''na zaciatku funkcie si inicializujeme premennu:
     '''
    count = 1
    for i in range(MAX_PLAYERS):
        '''Prejdeme celou velkostou hracou cize, maximalnim poctom hracou:
        '''
        if (-1 < playersFigureTravel[player][i] < LENGTH):
            '''Skontrolujeme ze ci je hrac v poli a nie mimo pola:
            '''
            if (count == figure):
                '''Ak ano tak sme nasli hraca
                '''
                return i
            else:
                '''Ak nie tak pokracujeme hladat dalej
                '''
                count += 1
    '''Ak sme hraca nenasli tak potom vratime -1
    '''
    return -1
'''=====================================================================================================================
====================================================================================================================='''
'''Funkcia playerFigureOnPlayableField: funkcia vrati vlastne figurku ktora sa nachadza na hracej ploche,
cize na hracom fielde.'''
def playerFigureOnPlayableField(player=0):
    pocitat = int(0)
    for i in range(MAX_PLAYERS):
        '''Prechadzem celou velkostou MAX_PLAYERS co je vlastne maximalni pocet hracov
        '''
        if (-1 < playersFigureTravel[player][i] < LENGTH):
            '''Rovnaky princip ako aj hore uvedeny vo funkcii nad kontrolujeme ci je hrac v hracom poli
            '''
            pocitat += 1
    '''a vratime vlastne count
    '''
    return pocitat
'''=====================================================================================================================
====================================================================================================================='''
'''Funkcia playerFigureInHouse: funkcia preveri ci sa figurka nenachadza v domceku uzivatela
'''
def playerFigureInHouse(player=0):
    count = int(0)
    ''''''
    for i in range(MAX_PLAYERS):
        '''Prechadzem celou velkostou MAX_PLAYERS co je vlastne maximalni pocet hracov
        '''
        if (playersFigureTravel[player][i] >= LENGTH):
            count += 1
            '''pomocou if podmienky ci je hracova pozicia vacsia ako dlzka, ak ano potom je v domceku:
            '''
    return count
'''=====================================================================================================================
====================================================================================================================='''
'''Funkcia: checkField - preveri ci na danom poli jestvuje figurka alebo je to pole prazne, ak je prazne funkcia vrati
-1 a ak nie tak vrati ID hraca.
    Figurky v poli:
 		-1 - prazdno
		0 - hrac A
		1 - hrac B
'''
def checkField(field):
    for i in range(MAX_PLAYERS):
        '''Prejdeme cez celi pocet hracov:
        '''
        if (playersFigureTravel[0][i] != -1 and playersFigureTravel[0][i] == field):
            '''A skontrolujeme ze ci ktory z hracov sa vlastne nachadza na danej pozicii
            A vratime hodnotu s hracovim ID a poziciou'''
            return 0, i
            ''''''
        elif (playersFigureTravel[1][i] != -1 and int((playersFigureTravel[1][i] + (LENGTH / 2)) % LENGTH) == field):
            '''A skontrolujeme ze ci ktory z hracov sa vlastne nachadza na danej pozicii
            A vratime hodnotu s hracovim ID a poziciou'''
            return 1, i
    '''Ak nenajdeme nic tak vratime -1ky'''
    return -1, -1
'''=====================================================================================================================
====================================================================================================================='''
'''Funkcia takePlayerOutOfHideout - sluzi vlastne na to aby vybrala hraca na hracie pole z domoceku vlastne zo toho ako
by nejakej skrisi na hracie pole.'''
def takePlayerOutOfHideout(player):
    protihrac = (player + 1) % 2
    for i in range(MAX_PLAYERS):
        '''Ak je dana figurka ktoru momentalne checkujeme nie je v domceku a ani na hracom poli
        tak ju vyhodime z danej skrisi na hracie pole'''
        if (playersFigureTravel[player][i] == -1):
            ''''''
            checkOfSet = 0
            ''''''
            if (player == 1):
                ''''''
                checkOfSet = LENGTH / 2
                ''''''
            pole = checkField(checkOfSet)
            ''''''
            if (pole[0] == protihrac):
                '''Ak sa nahodou stane ze hrac jedan je na rovnakej pozicii ako hrac dva
                tak program funguje tak ze zozerie hrada jedna ktory bol na tej pozicii'''
                playersFigureTravel[protihrac][pole[1]] = 0

            if (pole[0] == player):
                '''Ak na poli sa nachadza nas hrac cize nasa figurka tak potom 
                vratime -1'''
                return -1

            '''Touto castou kodu vraciame nasu figurku na zaciatok pola.'''
            playersFigureTravel[player][i] = 0
            return i
    return -1
'''=====================================================================================================================
====================================================================================================================='''
'''Funkcia movePlayersFigure - sluzi na to vlastne aby posuvalo hracovu figurku na poziciu position ktora je v 
parametry funkcie. 
        Returny: 
         	0 ak hrac nemoze posunut tu figurku(hon uz ma figurku na tej pozicii)
            1 ak posunul figurku
            2 - Ak posunul jeho figurku a ziedol/znicil protihracovu figurku
            -1 do -3 v pripade ak hrac moze posunut svoju figurku do domceka
            '''
def movePlayersFigure(player, figure, position):
    '''Al nova pozicia je vacsia ako dlzka fieldu to znamena ze figurka vchadza do domeceku alebo ze je figurka zablo-
    kovana'''
    if (playersFigureTravel[player][figure] + position >= LENGTH):
        '''house je vlastne premenna v ktorej sa pocita kolko pozicii vchadza vlastne:
        '''
        house = ((LENGTH - 1) - (playersFigureTravel[player][figure] + position))
        '''Cize miesta v domceku su iba MAX_PLAYERS cize su ohranicene, treba davat pozor na to, ak sa stane 
        ze vsetky miesta v domceku su plne tan vrati 0'''
        if (house < MAX_PLAYERS):
            ''''''
            return 0
        '''Ak je mieto v domceku tak vlozi figurku do domceku:'''
        sucess = setFigureToHouse(player, figure, house)
        '''Funkcia vrati sucess'''
        return sucess

    checkofset = 0
    ''''''
    if (player == 1):
        checkofset = LENGTH / 2

    field = checkField((playersFigureTravel[player][figure] + position + checkofset) % LENGTH)
    '''V tomto dolu uvedenom ife checknem vlastne ci mam svoju figurku na tej pozicii ak mam tak returnem 0'''
    if (field[0] == player):
        print('WARNING: Blokuje vas vasa vlastna figurka! Skuste znova!')
        return 0
    '''V nasledovnej casti kodu vlastne checkujem ci protihrac m,a figurku na tej istej pozicii ako aj ja, ak ano
    tak ho zozeriem a vlastne na tej pozicii sa nahradi figurka s mojou znackou aj IDckom'''
    player2 = (player + 1) % 2
    if (field[0] == player2):
        '''A ak sa stane ze protihrac nema figurku na tej istej pozicii tak sa figurka zotire
        '''
        playersFigureTravel[player2][field[1]] = -1
        '''A to nahradi z nasou figurkou
        '''
        playersFigureTravel[player][figure] += position
        return 2
    '''Posun ktory sme vykonali v tomto kode bol uspesny tak vratime sucess cize 1
    '''
    playersFigureTravel[player][figure] += position
    return 1
'''=====================================================================================================================
====================================================================================================================='''
'''Funkcia setFigureToHouse - ako sam nazov hovori, tak vkladame figurku do domcoku a tim padom je uz na bespecnom miest
 funkcia vrati negativne cislo za kazdi domcek, takze ho iba zmenime na pozitivne, cize ratame to ako math.abs(figure)'''
def setFigureToHouse(player, figure, position):
    if (position < 0):
        position = int(position * (-1))
    if (player == 0):
        '''Pomocou nasledovneho ifu vlastne preverim ci je domcek plny ak ano tak vratime 0
        '''
        if (hraciepole[position][AVERAGE_POS] != 'D'):
            ''''''
            return 0
        ''''''
        hraciepole[position][AVERAGE_POS] = playersFigure[player]
        ''''''
    else:
        ''''''
        if (hraciepole[int((sachSize - 1) - position)][AVERAGE_POS] != 'D'):
            ''''''
            return 0
        ''''''
        hraciepole[int((sachSize - 1) - position)][AVERAGE_POS] = playersFigure[player]
    '''Tento nasledovny kus kodu nam hovori o tom ze treba polozit figurku do domu
    a nie kdekolvek inam na hraciu plochu'''
    playersFigureTravel[player][figure] = -2

    figureInHouse = 0
    '''Timto kusom kodu vlastne checknem ze kolko figuriek hrac ma v domceku a 
    este chceknem ci vyhral!'''
    for i in range(MAX_PLAYERS):
        '''Prejdeme celou velkostou MAX_PLAYERS
        '''
        if (playersFigureTravel[player][figure] == -2):
            '''Skontrolujeme poziciu figurky ci je v house
            '''
            figureInHouse
    if (figureInHouse == MAX_PLAYERS):
        '''Ak je pocet figurok v domocoku rovny max_players
        tak potom mame vyhercu'''
        print('Hrac', playersFigure[player], 'zvytazil!')
        '''Zamrzneme hru a vypiseme vyhercu
        '''
        pauseGame()
        quit()

    tlacsachovnice(hraciepole)
    return 1
'''=====================================================================================================================
====================================================================================================================='''
'''Inicializujeme maticu na hranie hry
'''
hraciepole = gensachovnicu(sachSize)
'''=====================================================================================================================
====================================================================================================================='''
'''Touto funkciou ktoru mame nasledovne, sa uistujeme ci je hodnota ktora je zadana fakticky cislo, ak nie
tak odmietneme vstup a pockame na novy vstup.'''
def inputNum():
    num = int(-1)
    '''Loop pokial vnesene cislo nie je zmenene na spravnu hodnotu'''
    while (num == -1):
        char = input()
        '''Checknem ci je character cislo na vstupe'''
        if (char.isdigit() == True):
            num = int(char)
    return num
'''=====================================================================================================================
====================================================================================================================='''
'''Pomocou tejto funkcii generujem vlastne random cisla od 1 az po 6:'''
def rollTheDice():
    dice = SystemRandom().randint(1, 6)
    return dice
'''=====================================================================================================================
====================================================================================================================='''
'''A tato koncova cast kodu je vlastne ako ked by hlavna cast v ktorej kombinujeme komponenty ktore sme 
naprogramovali pred tim:'''
while 1 == 1:
    figureOnField = int(playerFigureOnPlayableField(player))
    figureInHouse = int(playerFigureInHouse(player))
    '''Player ktory name figurky na hracej ploche ma tri pokusy dostat sestorku aby vysiel na hraciu plochu'''
    countOfPlayers = 3
    '''Ale zase ak hrac ktory ma figurky na hracej ploche moze kocku hadzat iba raz a nie tri krat ako to bolo
    hore'''
    if (figureOnField > 0):
        countOfPlayers = 1
    '''While hrac ma este pokusov na hadzanie kociek:'''
    while countOfPlayers > 0:
        '''figureOnField a figureInHouse sa mozu menit na prave tomto mieste a aby neboli aktualizovane v hlavnom
        loope'''
        figureOnField = int(playerFigureOnPlayableField(player))
        figureInHouse = int(playerFigureInHouse(player))
        tlacsachovnice(hraciepole)
        print('NOTE: Hrac\'i ', playersFigure[player], ' je na rade.')
        print('NOTE: Stlac 1 aby si zavrtel kocku')
        inputOfNum = inputNum() # Hrac musi inputnut 1 aby kod pokracoval dalej
        if (inputOfNum == 1):
            '''Ked hrac hodi kocku tak kod by mal vypisat hodnut na obrazovku
            '''
            dice = int(rollTheDice())
            print('NOTE: Dostal si ', dice, '!')
            '''Tento If vlastne kontroluje ze ci hrac dostal 6 alebo nie, ak 
            hrac dostal 6 tak ma pravo hrat znova:'''
            if (dice == 6):
                if (figureOnField == 0):
                    countOfPlayers = 1
                else:
                    countOfPlayers += 1
                '''Ak nie su ziadne figurky na hracom poli, tak polozime prveho ktoreho najdeme na to
                hracie pole:'''
                if (figureOnField == 0):
                    '''figurka cize vyberame hraciu figurku z skrise 
                    na hracie pole.'''
                    figure = takePlayerOutOfHideout(player)
                    '''A vyprintneme zase aktualizovanu hraciu plochu na 
                    klientovu obrazovku'''
                    tlacsachovnice(hraciepole)
                    print('NOTE: Kocka ukazuje 6 tak si vlozil figurku (', figure, ') na hraciu plochu')
                    pauseGame()
                    '''Hra sa pauzuje a potom pokracuje:'''
                    continue
                # Iba jedna figurka na ceste, a nieto viac novych ktore sa daju pridat
                elif (figureOnField == 1 and (figureInHouse == 3)):
                    '''Do premennej figurka vlozime udaje ze kde sa presne figurka
                    nachadza na hracom poli:'''
                    figure = findPlayerOnPlayableField(player, 1)
                    '''Ked vlastne najdeme tu danu figurku tak ju posunieme:'''
                    movePlayersFigure(player, figure, dice)
                    '''A zobrazime nove hracie pole uzivatelovi
                    '''
                    tlacsachovnice(hraciepole)
                    print('NOTE: Dostal si 6 a posunul si svoju figurku')
                else:
                    '''Ked hrac dostane znovu sestku a stane sa ze uz jednu figurku ma vlozenu na hracom poli
                    tak sa dostava moznost aby hrac si vlozil este jednu figurku navise co je mozne pomocout tohto else:
                    '''
                    if (figureOnField == 1):
                        print('NOTE: Stlac 1 aby si posunul tvoju figurku')
                    else:
                        '''Pomocou tohto printu si uzivatel moze zvolit ze ktorou figurkou chce spravovat:
                        '''
                        print('NOTE: Stlac 1 -', figureOnField, 'aby si posunul figurku')

                    checkOfSet = 0
                    if (player != 0):
                        checkOfSet = LENGTH / 2
                    pole = checkField(checkOfSet)
                    '''Ak hrac nema ziadnu figurku na hracom poli, a ma 6 tak ma moznost vlozit figurku
                    na hracie pole:'''
                    if (pole[0] != player):
                        print('NOTE: Stlac 0 aby si vylozil novu figurku na hraciu plochu')
                    '''Input do ktoreho mame vlozit cislo povoluje nam iba 0, 
                    ked mozeme vybrat novu figurku, alebo vratime index figurky cize na rede bude pocitact:'''
                    inputOfNum = -1
                    while (inputOfNum == -1):
                        inputOfNum = inputNum()
                        '''Po vlozeni cisla na rade je hrac 2 cize pocitact:'''
                        if (inputOfNum == 0 and pole[0] == player):
                            ''''''
                            inputOfNum = -1
                            ''''''
                            continue
                        ''''''
                        if (inputOfNum != 0 and inputOfNum > figureOnField):
                            ''''''
                            inputOfNum = -1
                        ''''''
                    if (inputOfNum == 0):
                        '''Ak input je rovny 0 tak hrac si vybera novu figurku z kritia na hraciu
                        plochu a zacina hrat s nou:'''
                        figure = takePlayerOutOfHideout(player)
                        '''Po vybere na figurky tak sa hracia plocha aktualizuje:
                        '''
                        tlacsachovnice(hraciepole)
                        '''Print nam to ukaze na obrazovku:
                        '''
                        print('NOTE: Vylozili ste novu figurku (', figure, ') na cestu')
                        pauseGame()
                        continue
                    else:
                        '''V tomto pripade figure vlastne mame informacie o tom kde vlastne
                        figurka sa nachadza a na akej je pozicii:'''
                        figure = findPlayerOnPlayableField(player, inputOfNum)
                        '''a do premennej sucess vlastne zapiseme pohib figurky na hracom poli
                        cize novu poziciu na hracom poli:'''
                        sucess = movePlayersFigure(player, figure, dice)
                        '''Po posune figurky aktualizujeme hraciu plochu tak ze vypisime zo 
                        zmenamy ktore sme robili:'''
                        tlacsachovnice(hraciepole)
                        '''ak sucess nebol uspesny tak cez print vypiseme danu chybu:
                        '''
                        if (sucess == 0):
                            print('NOTE: nemozete posunut tu figurku')
                print('NOTE: Dostal si 6, hraj znovu!')
            elif (figureOnField > 0):
                '''^^^^ - Ak hrac nedostane 6, ale zase hrac ma figurky uz na hracej ploche:'''
                '''Ak jestvuje iba jedna figurka na hracej ploche, cize je to jedina figurka ktorou mozeme hrat kolo:'''
                if (figureOnField == 1):
                    '''Cize ako aj predtim, najdeme si figurku na hracej ploche a zapiseme to do premennej figure
                    '''
                    figure = findPlayerOnPlayableField(player, 1)
                    '''Potom ako aj predtim do sucess premennej zapiseme pohyb figurky
                    '''
                    sucess = movePlayersFigure(player, figure, dice)
                    '''A z aktualizujeme hraciu plochu po hrani hraca:
                    '''
                    tlacsachovnice(hraciepole)
                    '''Vyprintujeme alebo vypiseme vlastne hodnotu ktoru sme dostali z kocky:'''
                    print('Dostal si ', dice, '!')

                else:
                    '''V tomto else vlastne mame to ze ked hrac ma viac ako jednu figurku na hracej ploche, a podla toho vlastne
                    vieme spravovat viacerimy figurkami, ale jednu figurku mozeme pouzivat len raz, nemozeme spravovat
                    obidvomi v rovnakom case:'''
                    print('Stlac 1-', figureOnField, 'aby si posunul figurku (V smere hodinových ručičiek od počiatočnej pozicie)')
                    '''V dalsom kuse kodu vlastne spravujeme inputom, cize inputOfNum, ale to su vlastne indexy figuriek:
                    '''
                    inputOfNum = -1
                    while (inputOfNum == -1):
                        '''While zbehne pokial podmienka nie je -1:
                        '''
                        inputOfNum = inputNum()
                        '''Vlozime cislo a podla toho spravujeme figurkami:
                        '''
                        if (inputOfNum == 0 or inputOfNum > figureOnField):
                            '''pokial input je vacsi ako vsetky figurky vo hracom poli a je rovnaky ako 0 tak input nam
                            automaticky bude 0:'''
                            inputOfNum = -1
                    '''A zase zapisujeme vlastne do premennej figure kde sa vlastne hrac nachadza:
                    '''
                    figure = findPlayerOnPlayableField(player, inputOfNum)
                    '''Posunieme hraca o tolko kolko dostal na kocky:
                    '''
                    sucess = movePlayersFigure(player, figure, dice)
                    '''A z aktualizujeme hraciu plochu tak ze vypisime zase hraciu plochu:
                    '''
                    tlacsachovnice(hraciepole)
            '''Cize zmensime hracove pokusy o 1:
            '''
            countOfPlayers -= 1
            pauseGame()
    '''A z aktualizujeme hraciu plochu tak ze vypisime zase hraciu plochu:
    '''
    tlacsachovnice(hraciepole)
    '''Vypiseme vlastne a zadame ze je druhy hrac na rade aby hral:
    '''
    player = (player + 1) % 2
    '''To aj vypiseme pomocou print funckie:
    '''
    print('Nasledovny hrac\'i na rade')
    pauseGame()
