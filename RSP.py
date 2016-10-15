"""
TEST
	.. image:: /Users/godonghyeon/Downloads/customLogo.gif
		:height: 100
		:width: 221
		:alt: 가위바위보
	이 프로램은 컴퓨터와 가위,바위,보를 하는 프로그램입니다.
	이 프로그램은 Python3 으로 작성 되었습니다.
		작성자 : 고동현
		작성일 : 2016 Oct 12
		사용언어 : Python3

"""
import random 

kind = ["가위","바위","보"]
board = [0 ,0 ,0] #승,무,패 를 기록하는 보드
print("=======================================")
for i in range(10): #10번 반복
	computer = random.randrange(3)
	player = int(input("가위,바위,보(0,1,2) : "))
	print("선택한 것은",kind[player],"입니다.")
	print("컴퓨터가 낸 것은",kind[computer],"입니다.")
	if(computer==player):
		print("\n비김")
		board[1]+=1
	elif(computer == player+1 or computer == player-2):
		print("\n컴퓨터 승리")
		board[2]+=1
	else:
		print("\n플레이어 승리")
		board[0]+=1
	print("=======================================")

#보드 출력
print("\n\tBoard")
print("플레이어 승리 횟수 : ",board[0])
print("플레이어 패배 횟수 : ",board[2])
print("무승부 : ",board[1])
print("=======================================")

"""
	==================
	동현이가 만든 가위바위보
	==================

	변수 설명
	-------
	
	import random
	-------------
	아래 computer 변수를 위해 random 라이브러리를 import한다.

	kind
	----
	"가위","바위","보" 를 순서대로 kind 라는 이름의 배열에 넣어준다.
	넣은 이유는 플레이어가 낸 손가락 모양과,컴퓨터가 낸 손가락 프린트 해주기 위해서이다. 

	board
	-----
	초기값
	+-----------+-----------+-----------+
	|    WIN    |    DRAW   |    LOSE   |
	+===========+===========+===========+
	| board[0]=0| board[1]=0| board[2]=0|
	+-----------+-----------+-----------+

	computer
	--------
	random 함수를 이용해서 0~2 사이의 수를 생성한다.

	player
	------
	player가 내고싶은 모양을 입력받는다.


"""
