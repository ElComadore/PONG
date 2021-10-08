import pygame as pg
from Paddle import Paddle
from Ball import Ball
from Score import Score
from mediaHandling import load_image, load_sound
from startMenu import gameMode, soundOption


def startmenu(background):
    screen = pg.display.get_surface()

    titleImage, titlerect = load_image('PONG!.png', -1)
    titleImage = pg.transform.scale(titleImage, (titleImage.get_width()*6, titleImage.get_height()*6))
    muteButton = soundOption()

    sPlayer = gameMode('Single Player', (screen.get_rect().centerx, screen.get_rect().bottom*2/3 - 40))
    tPlayer = gameMode('Two Player', (screen.get_rect().centerx, screen.get_rect().bottom*2/3 + 40))

    modeSprites = pg.sprite.RenderPlain(sPlayer, tPlayer)
    allSprites = pg.sprite.RenderPlain(muteButton, modeSprites.sprites())

    gameRunning = True
    clock = pg.time.Clock()

    while gameRunning:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return
            elif event.type == pg.MOUSEBUTTONDOWN and pg.mouse.get_pressed(3)[0]:
                if sPlayer.rect.collidepoint(pg.mouse.get_pos()):
                    singleplayer(background, muteButton.soundOn)
                elif tPlayer.rect.collidepoint(pg.mouse.get_pos()):
                    multiplayer(background, muteButton.soundOn)
                elif muteButton.rect.collidepoint(pg.mouse.get_pos()):
                    muteButton.muteToggle()
            for modes in modeSprites.sprites():
                if modes.rect.collidepoint(pg.mouse.get_pos()):
                    modes.isHovered((0, 0, 255))
                else:
                    modes.notHovered()

        screen.blit(background, (0, 0))
        allSprites.draw(screen)
        screen.blit(titleImage, (screen.get_rect().centerx - titleImage.get_width()/2, screen.get_height()/3 - titleImage.get_height()/2))
        pg.display.flip()


def singleplayer(background, sound):
    screen = pg.display.get_surface()

    paddleleft = Paddle(1)
    paddleright = Paddle(2)
    paddles = pg.sprite.Group(paddleleft, paddleright)

    ball = Ball()

    score = Score()
    scoreRender = pg.sprite.RenderPlain(score)
    movingsprites = pg.sprite.RenderPlain(paddleright, paddleleft, ball)

    movingsprites.draw(screen)
    scoreRender.draw(screen)

    pg.display.flip()

    clock = pg.time.Clock()

    while 1:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return
            elif event.type == pg.KEYDOWN and event.key == pg.K_w:
                paddleleft.changeUp()
            elif event.type == pg.KEYDOWN and event.key == pg.K_s:
                paddleleft.changeDown()
            elif event.type == pg.KEYUP and event.key == pg.K_w:
                paddleleft.changeUp()
            elif event.type == pg.KEYUP and event.key == pg.K_s:
                paddleleft.changeDown()

        ballX = pg.font.Font(None, 72).render(str(ball.getvelocity()[0]), True, (255, 255, 255))

        ball.update(paddles.sprites(), score, sound)
        paddleright.aiUpdate(ball)
        paddles.update()

        screen.blit(background, (0, 0))
        screen.blit(ballX, (screen.get_rect().centerx, screen.get_rect().bottom - ballX.get_height()))
        movingsprites.draw(screen)
        scoreRender.draw(screen)
        pg.display.flip()


def multiplayer(background, sound):
    screen = pg.display.get_surface()

    paddleleft = Paddle(1)
    paddleright = Paddle(2)
    paddles = pg.sprite.Group(paddleleft, paddleright)

    ball = Ball()

    score = Score()
    scoreRender = pg.sprite.RenderPlain(score)
    movingsprites = pg.sprite.RenderPlain(paddleright, paddleleft, ball)

    movingsprites.draw(screen)
    scoreRender.draw(screen)

    pg.display.flip()

    clock = pg.time.Clock()

    while 1:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return
            elif event.type == pg.KEYDOWN and event.key == pg.K_w:
                paddleleft.changeUp()
            elif event.type == pg.KEYDOWN and event.key == pg.K_s:
                paddleleft.changeDown()
            elif event.type == pg.KEYUP and event.key == pg.K_w:
                paddleleft.changeUp()
            elif event.type == pg.KEYUP and event.key == pg.K_s:
                paddleleft.changeDown()
            elif event.type == pg.KEYDOWN and event.key == pg.K_UP:
                paddleright.changeUp()
            elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
                paddleright.changeDown()
            elif event.type == pg.KEYUP and event.key == pg.K_UP:
                paddleright.changeUp()
            elif event.type == pg.KEYUP and event.key == pg.K_DOWN:
                paddleright.changeDown()

        ball.update(paddles.sprites(), score, sound)
        paddles.update()

        screen.blit(background, (0, 0))
        movingsprites.draw(screen)
        scoreRender.draw(screen)
        pg.display.flip()


def main():
    pg.init()

    screen = pg.display.set_mode((1200, 800))
    pg.display.set_caption('Mega cringe test thingy')

    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    startmenu(background)


main()
