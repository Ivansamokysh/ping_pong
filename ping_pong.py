import pygame 
import modules.image_class as m_cl

pygame.init()



 
#прапорці, що відповідають за стан гри
game = True
finish = False
clock = pygame.time.Clock()
FPS = 60

 
pygame.font.init()
font = pygame.font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))
 
speed_x = 3
speed_y = 3
 
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
  
    if finish != True:
        m_cl.window.fill(m_cl.back)
        m_cl.racket1.update_l()
        m_cl.racket2.update_r()
        m_cl.ball.rect.x += speed_x
        m_cl.ball.rect.y += speed_y
    
        if pygame.sprite.collide_rect(m_cl.racket1, m_cl.ball) or pygame.sprite.collide_rect(m_cl.racket2, m_cl.ball):
            speed_x *= -1
            speed_y *= 1
        
        #якщо м'яч досягає меж екрана, змінюємо напрямок його руху
        if m_cl.ball.rect.y > m_cl.win_height-50 or m_cl.ball.rect.y < 0:
            speed_y *= -1
    
        #якщо м'яч відлетів далі ракетки, виводимо умову програшу для першого гравця
        if m_cl.ball.rect.x < 0:
            finish = True
            m_cl.window.blit(lose1, (200, 200))
            game_over = True
    
        #якщо м'яч полетів далі ракетки, виводимо умову програшу другого гравця
        if m_cl.ball.rect.x > m_cl.win_width:
            finish = True
            m_cl.window.blit(lose2, (200, 200))
            game_over = True
    
        m_cl.racket1.reset()
        m_cl.racket2.reset()
        m_cl.ball.reset()
    
    pygame.display.update()
    clock.tick(FPS)
