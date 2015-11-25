#from absorbFireballs import *
from ladderPlacement import *
#from placePrincess import *
#from buttonOnScreen import *
#from moveFireballs import *
from PlayerIsHero import *
from Walls import *
#from CoinsInGame import *
#from Person import *
#from printingCoins import *
from placeKong import *
#from printMessage import *

listOfWalls=pygame.sprite.Group()
listOfWallsAndHero=pygame.sprite.Group()
listOfLadders=pygame.sprite.Group()

ceiling=Walls(140,40,1200,25)
wall1=Walls(115,40,25,860)
floor=Walls(115,900,1250,25)
wall2=Walls(1340,40,25,860)

leftFloor11=Walls(140,180,165,25)
leftFloor12=Walls(330,180,275,25)
leftFloor13=Walls(630,180,100,25)
rightFloor11=Walls(560,300,345,25)
rightFloor12=Walls(930,300,430,25)
leftFloor21=Walls(140,420,440,25)
leftFloor22=Walls(605,420,150,25)
rightFloor21=Walls(400,540,370,25)
rightFloor22=Walls(795,540,370,25)
leftFloor31=Walls(140,660,370,25)
leftFloor32=Walls(535,660,450,25)
rightFloor31=Walls(405,780,405,25)
rightFloor32=Walls(835,780,510,25)

listOfWalls.add(ceiling,wall1,floor,wall2,leftFloor11,leftFloor12,leftFloor13,rightFloor11,leftFloor21,rightFloor12,leftFloor22,rightFloor21,rightFloor22,leftFloor31,leftFloor32,rightFloor31,rightFloor32)

ladder1=ladderPlacement(805,780)
ladder2=ladderPlacement(505,660)
ladder3=ladderPlacement(765,540)
ladder4=ladderPlacement(575,420)
ladder5=ladderPlacement(900,420)
ladder6=ladderPlacement(900,300)
ladder7=ladderPlacement(600,180)
ladder8=ladderPlacement(300,300)
ladder9=ladderPlacement(300,180)

listOfLadders.add(ladder1,ladder2,ladder3,ladder4,ladder5,ladder6,ladder7,ladder8,ladder9)

player=PlayerIsHero(145,870,'rsz_hero2_1.png')
kong=placeKong(180,120)


def test_playerMovement():
    player.changePosition(5,0)
    player.printPlayer(listOfWalls)
    assert player.getXCoordinate()==150

def test_heroJump():
    player.heroJump(listOfWalls,listOfLadders)
    player.printPlayer(listOfWalls)
    assert player.getYCoordinate()==860

def test_kongMovementLeftRight():
    kong.moveKongRight(3)
    assert kong.getXCoordinate()==6

def test_kongMovmentMain():
    kong.moveKong(203)
    assert kong.getXCoordinate()==206

def test_wallPosition():
    assert wall1.getXCoordinateOfWall()==115
    assert wall1.getYCoordinateOfWall()==40

def test_ladder():
    assert ladder1.getXCoordinate()==805
    assert ladder1.getYCoordinate()==780

def test_kongRange():
    startKong=190
    for _ in range(1000):
        if startKong<160:
            startKong=160
            kong.changeFlag(0)
        kong.moveKong(startKong)
        if startKong<689 and kong.getFlag()==0:	
            startKong+=3
            if startKong==689:
	        kong.changeFlag(1)
        if startKong>200 and kong.getFlag()==1:
            startKong-=3
            if startKong==190:
                kong.changeFlag(0)
        assert startKong>=160 and startKong<=691
