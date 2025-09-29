from pico2d import *
import random




class Grass:
    def __init__(self):#생성자함수
        #grass 객체의 속성을 정의하고 초기화
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x =  random.randint(100, 700)
        self.frame = random.randint(0,7)
    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,90)

    def update(self):
        self.x+=5
        self.frame = (self.frame+1)%8
        pass

class Ball:
    def __init__(self):
        balltype = random.randint(1,2)
        if balltype ==1:
            self.image = load_image('ball21x21.png')
        elif balltype == 2:
            self.image = load_image('ball41x41.png')
        self.x = random.randint(100,700)
        self.y = 599
        self.speed = random.randint(4,15)
    def update(self):
        if(self.y>60):
            self.y -= self.speed
        if(self.y<=60):
            self.y=60
    def draw(self):
        self.image.draw(self.x,self.y)


# Game object class here
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()
# game loop

#초기화



def reset_world():
    global running
    global world    #모든 객체들을 가진 리스트

    world = []      #빈 월드리스트 생성
    running = True

    grass = Grass()    #땅을 만들고 월드리스트에 추가
    world.append(grass)

    team = [Boy() for _ in range(11)] #팀을 만들고 팀을 월드에 추가
    world+=team

    ball = [Ball() for _ in range(20)]
    world+=ball



reset_world()


def update_world():
    #월드에 있는 객체들을 업데이트
    for game_object in world:
        game_object.update()
    pass

def render_world():
    #월드에 객체들을 그린다.
    clear_canvas()
    for game_object in world:
        game_object.draw()
    update_canvas()



while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)


# finalization code
close_canvas()
