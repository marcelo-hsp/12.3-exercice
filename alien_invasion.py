import pygame
from pygame.sprite import Group
from settings import Settings
import game_functions as gf
from ship import Ship
from alien import Alien
from bullet import Bullet

def run_game():
    #inicializa o pygame, as configurações e o objeto screen
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Cria uma espaçonave
    ship = Ship(ai_settings, screen)

    # Cria um grupo no qual serão armazenados os projéteis
    bullets = Group()
    aliens = Group()

    # Cria um alienígena
    # alien = Alien(ai_settings, screen)

    # Cria uma frota de alienígenas
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Inicia o laço principal do jogo
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()