import pgzrun, random
WIDTH, HEIGHT, TITLE=400,400,"gradient"

def draw():
    w=WIDTH-40
    h=HEIGHT/4
    r=random.randint(0,255)
    g=0
    b=255
    for i in range(30):
        rect=Rect(20,20,w,h)
        rect.center=WIDTH/2, HEIGHT/2
        screen.draw.rect(rect,(r,g,b))
        w=w-10
        h=h+10
        if g <245:
            g=g+10
        else:
            g=0
        if b > 10:
            b=b-10
        else: 
            b=0




pgzrun.go()