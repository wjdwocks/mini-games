# Mini Games
- 어렸을 때 하던 추억게임들을 파이게임을 통해 만들어 보았습니다.
- 크게 메인메뉴 -> 게임메뉴 -> 각 게임들 -> 실행의 형태로 화면의 전환이 일어납니다.
---

## Main Menu
->메인메뉴 사진.
W, S, &uarr;, &darr; 을 통해 커서를 원하는 위치로 옮길 수 있다. (모든 화면 공통)
BackSpace, ESC 키를 통해 뒤로가기를 수행할 수 있다. (모든 화면 공통)
Enter, Spacebar 키를 통해 커서가 위치한 메뉴를 선택할 수 있다. (모든 화면 공통)
메인 메뉴에서는 게임메뉴, 옵션, credit, Exit 버튼이 있다.
--- 
### Option Menu
->옵션메뉴 사진
옵션메뉴에서는 White Mode를 만들어서 선택 시
배경 : 검정, 글씨 : 흰색 -> 배경 : 흰색, 글씨 : 검정으로 변경할 수 있다. 
--- 
### Credit Menu
-> Credit 메뉴 사진
Credit메뉴에서는 제작자와 여러 이미지나 폰트의 저작권을 적어두었습니다.
---
### Games Menu
-> Games Menu 사진
Game Menu에서는 여러 게임들을 선택할 수 있게 하여 해당 게임들의 세부사항을 선택할 수 있는 메뉴로 옮겨준다.
---
##### Space Game
![space Menu](https://github.com/wjdwocks/mini-games/assets/144427497/606e51e7-dea6-48ba-aa30-4f5b2941dbbe)
Space Game 메뉴에서는 1Person Mode, 2Person Mode, GameMenual 1p, GameMenual 2p을 선택할 수 있다.
1p모드는 혼자서 게임을 할 수 있고, 2p모드는 둘이서 게임을 할 수 있다.
GameMenual 1p, GameMenual 2p는 각 게임모드에 대한 설명이 적혀있다.

###### 1p Mode
![1p](https://github.com/wjdwocks/mini-games/assets/144427497/cb2fec61-f289-4b5c-b1c1-392fc92334ad)
1p모드에서 적은 랜덤으로 움직이고, 랜덤한 주기로 총알을 발사한다. 
플레이어는 A, &larr;, D, &rarr;를 통해서 좌우로 움직이며 SpaceBar를 통해 총알을 발사할 수 있다.
플레이어와 상대 모두 체력은 10으로 동일하고 0이되면 승리하거나 패배한다.
패배하거나 승리하면 문구가 화면에 출력되고, 3초 후 메뉴화면으로 돌아간다.

###### 2p Mode
![2p](https://github.com/wjdwocks/mini-games/assets/144427497/2bddb1b3-7bd2-4a33-8e36-43501e0e8071)
2p 모드에서는 1p가 &larr;, &rarr;를 통해 움직이고, 숫자패드의 0을 눌러 총알을 발사할 수 있다.
2p는 A, D, SpaceBar를 통해 조작할 수 있다.
한쪽이 죽어서 게임이 끝나게 되면, 이긴 플레이어가 화면에 출력되고, 3초 후 메뉴화면으로 돌아간다.

##### BrickBreaking Game(블록깨기)
![brick Menu](https://github.com/wjdwocks/mini-games/assets/144427497/e6f5e4fd-6970-408b-83a1-bb94d270dcc8)
BrickBreaking Menu에서는 Game Start버튼과 Game Menual을 볼 수 있다.

###### BrickBreaking in game
![brick ingmae](https://github.com/wjdwocks/mini-games/assets/144427497/9c432791-6283-4ebe-b93c-11d493d0343d)
BrickBreaking 게임은 마우스를 통해서 바닥의 패달을 움직일 수 있고, 공이 바닥에 닿으면 게임 오버되는 방식이다. 
게임오버되면 3초 후 메뉴로 돌아가지게 된다.

##### Escape Poo Game(똥피하기)
![po0Menu](https://github.com/wjdwocks/mini-games/assets/144427497/ccc3c9d5-f549-4322-822f-4d725c17c200)
Escape Poo Game Menu에서는 Game Start버튼과 Menual버튼이 있어서 게임 설명을 보거나, 게임을 시작할 수 있다.

###### Escape Poo in game
![c_1](https://github.com/wjdwocks/mini-games/assets/144427497/806af243-a070-4e23-954b-1fa99250ff48)
Escape Poo Game에서는 &larr;, &rarr;, A, D키를 통해 좌우로 캐릭터를 움직일 수 있다.
똥들은 화면의 가장 위 랜덤 위치에서 랜덤한 간격으로 생성되며, 일정한 속도로 바닥으로 떨어진다.
똥이 바닥에 닿으면 사라지게 되고, 캐릭터는 똥에 맞을 때마다 점점 똥이 묻게된다.
![c_2](https://github.com/wjdwocks/mini-games/assets/144427497/1e95c4cc-f7a1-4456-9d0d-78ddb1390525)
![c_3](https://github.com/wjdwocks/mini-games/assets/144427497/95d29db3-4e60-4726-b367-482e0faf4ce4)
3번 똥에 맞게되면 GAME OVER가 된다.
![gmaeover](https://github.com/wjdwocks/mini-games/assets/144427497/e802bb5b-e9e1-4852-a112-568153ff6c7d)
게임 오버가 되면, 자신의 기록(버틴 시간)이 화면에 출력되고, 3초 후 메뉴화면으로 돌아간다.
(+)&nbsp;&nbsp;캐릭터의 피격범위가 보이는 것보다 커서 좌우로 30px씩 줄였다.

##### Mouse Maze Game(마우스 피하기)
![mouseMenu](https://github.com/wjdwocks/mini-games/assets/144427497/d594c09a-2c6f-4101-bfe2-000683538545)

Mouse Maze Game Menu에서는 Game Start버튼과 Menual 버튼이 있어서 게임을 시작하거나 게임 설명서를 확인할 수 있다.

###### Mouse Maze in gamek<br/>
-> 마우스 피하기 인게임 사진
시작 화면


마우스 피하기 
