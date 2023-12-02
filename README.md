# Mini Games
- 어렸을 때 하던 추억게임들을 파이게임을 통해 만들어 보았습니다.
- 크게 메인메뉴 -> 게임메뉴 -> 각 게임들 -> 실행의 형태로 화면의 전환이 일어납니다.
  
---
## Main Menu
![_1 Main](https://github.com/wjdwocks/mini-games/assets/144427497/90f9a4f7-18f1-4722-b71b-888ee314919b)<br/>
- W, S, &uarr;, &darr; 을 통해 커서를 원하는 위치로 옮길 수 있다. (모든 화면 공통)
- BackSpace, ESC 키를 통해 뒤로가기를 수행할 수 있다. (모든 화면 공통)
- Enter, Spacebar 키를 통해 커서가 위치한 메뉴를 선택할 수 있다. (모든 화면 공통)
- 메인 메뉴에서는 게임메뉴, 옵션, credit, Exit 버튼이 있다.

--- 
### Option Menu
![New Issue · wjdwocks_mini-games - Chrome 2023-11-26 오후 4_09_37](https://github.com/wjdwocks/mini-games/assets/144427497/3903e5c5-e539-4397-a7ee-0e1ab0289501)
<br/>
- 옵션메뉴에서는 White Mode를 만들어서 선택 시
- 배경 : 검정, 글씨 : 흰색 -> 배경 : 흰색, 글씨 : 검정으로 변경할 수 있다.
![pygame window 2023-11-26 오후 10_13_38](https://github.com/wjdwocks/mini-games/assets/144427497/661bc39a-71d2-4e36-8d4e-b7d6b12821f4)

--- 
### Credit Menu
![credits (2)](https://github.com/wjdwocks/mini-games/assets/144427497/df8b28ca-453a-46b5-93cc-2c2d35398a09)<br/>
- Credit메뉴에서는 제작자(나)와 여러 이미지나 폰트의 저작권을 적어두었습니다.

---
### Games Menu
![_2 GameMenu](https://github.com/wjdwocks/mini-games/assets/144427497/0afb1b0e-d575-453b-bf5b-6d68277c2fd2)<br/>
Game Menu에서는 여러 게임들을 선택할 수 있게 하여 해당 게임들의 세부사항을 선택할 수 있는 메뉴로 옮겨준다.<br/>

---
##### Space Game
![_3space_menu](https://github.com/wjdwocks/mini-games/assets/144427497/021d0497-8dd5-40eb-baf5-e1e6aecad969)<br/>
Space Game 메뉴에서는 1Person Mode, 2Person Mode, GameMenual 1p, GameMenual 2p을 선택할 수 있다.<br/>
1p모드는 혼자서 게임을 할 수 있고, 2p모드는 둘이서 게임을 할 수 있다.<br/>
GameMenual 1p, GameMenual 2p는 각 게임모드에 대한 설명이 적혀있다.<br/>

###### 1p Mode
![1p](https://github.com/wjdwocks/mini-games/assets/144427497/c9260bba-6563-463b-b240-191627523de9) <br/>
1p모드에서 적은 랜덤으로 움직이고, 랜덤한 주기로 총알을 발사한다. <br/>
플레이어는 A, &larr;, D, &rarr;를 통해서 좌우로 움직이며 SpaceBar를 통해 총알을 발사할 수 있다.<br/>
플레이어와 상대 모두 체력은 10으로 동일하고 0이되면 승리하거나 패배한다.<br/>
패배하거나 승리하면 문구가 화면에 출력되고, 3초 후 메뉴화면으로 돌아간다.<br/>

###### 2p Mode
![2p](https://github.com/wjdwocks/mini-games/assets/144427497/31af62c7-d1f1-4b76-b8ff-e84fd41218a3) <br/>
2p 모드에서는 1p가 &larr;, &rarr;를 통해 움직이고, 숫자패드의 0을 눌러 총알을 발사할 수 있다.<br/>
2p는 A, D, SpaceBar를 통해 조작할 수 있다.<br/>
한쪽이 죽어서 게임이 끝나게 되면, 이긴 플레이어가 화면에 출력되고, 3초 후 메뉴화면으로 돌아간다.<br/>

---
##### BrickBreaking Game(블록깨기)
![brick Menu](https://github.com/wjdwocks/mini-games/assets/144427497/25d8a2be-e9a2-435a-851d-ab796d15ef59)<br/>
BrickBreaking Menu에서는 Game Start버튼과 Game Menual을 볼 수 있다.

###### BrickBreaking in game
![brick](https://github.com/wjdwocks/mini-games/assets/144427497/dde7c415-65fa-42f4-81f2-bb0f5658cb2a) <br/>
BrickBreaking 게임은 마우스를 통해서 바닥의 패달을 움직일 수 있고, 공이 바닥에 닿으면 게임 오버되는 방식이다. <br/>
게임오버되면 3초 후 메뉴로 돌아가지게 된다.

---
##### Escape Poo Game(똥피하기)
![po0Menu](https://github.com/wjdwocks/mini-games/assets/144427497/ccc3c9d5-f549-4322-822f-4d725c17c200)<br/>
Escape Poo Game Menu에서는 Game Start버튼과 Menual버튼이 있어서 게임 설명을 보거나, 게임을 시작할 수 있다.

###### Escape Poo in game
![c_1](https://github.com/wjdwocks/mini-games/assets/144427497/02a4f90c-9028-4374-a001-7f91116e410a)<br/>
Escape Poo Game에서는 &larr;, &rarr;, A, D키를 통해 좌우로 캐릭터를 움직일 수 있다.<br/>
똥들은 화면의 가장 위 랜덤 위치에서 랜덤한 간격으로 생성되며, 일정한 속도로 바닥으로 떨어진다.<br/>
똥이 바닥에 닿으면 사라지게 되고, 캐릭터는 똥에 맞을 때마다 점점 똥이 묻게된다.<br/>

![c_2](https://github.com/wjdwocks/mini-games/assets/144427497/92143c28-ee29-451d-ae2f-96d339d99e73)
![c_3](https://github.com/wjdwocks/mini-games/assets/144427497/65b71bc8-e75f-4ac0-a3a1-b9151afa7e8f)
3번 똥에 맞게되면 GAME OVER가 된다.<br/>
게임 오버가 되면, 자신의 기록(버틴 시간)이 화면에 출력되고, 3초 후 메뉴화면으로 돌아간다.<br/>

![gameover](https://github.com/wjdwocks/mini-games/assets/144427497/9c064bb8-d7ed-4b79-a0d8-57fa4e1677a8)
(+) &nbsp;&nbsp;캐릭터의 피격범위가 보이는 것보다 커서 좌우로 30px씩 줄였다.<br/>
(+) &nbsp;&nbsp; 하늘에서 휴지가 떨어지게 해서 휴지와 닿는다면 캐릭터의 체력이 하나 회복되도록함.<br/>

![후지](https://github.com/wjdwocks/mini-games/assets/144427497/6c6d100a-f0c0-4f57-ac6c-b742f74e5569)
---
##### Mouse Maze Game(마우스 피하기)
![mouseMenu](https://github.com/wjdwocks/mini-games/assets/144427497/d594c09a-2c6f-4101-bfe2-000683538545)<br/>
Mouse Maze Game Menu에서는 Game Start버튼과 Menual 버튼이 있어서 게임을 시작하거나 게임 설명서를 확인할 수 있다.

###### Mouse Maze in game
![mouse_in](https://github.com/wjdwocks/mini-games/assets/144427497/c52d3ad7-544e-4ff5-ab12-4d7aa903480c)<br/>
마우스 피하기 게임은 마우스만으로 하는 게임인데 마우스 커서가 가리키는 곳의 1px의 정사각형이 화면 안의 블록 속에만 있도록 유지하면서 시작 지점부터 마지막 지점까지 이동해야 하는 게임이다.

게임을 시작하면 마우스를 일정 위치의 블록에 가져가서 클릭을 해야 게임이 시작된다.&nbsp;&nbsp;(사기 방지)
-> 마우스 피하기 시작화면 사진

색이 있는 화면을 넘어가게 되면 GAME OVER문구가 뜨고, 3초 뒤 메뉴화면으로 돌아가게 된다.
만약 시작 지점 -> 종료 지점까지 이동하게 되면, YOU WIN문구가 뜨고, 3초 뒤 메뉴화면으로 돌아간다.

