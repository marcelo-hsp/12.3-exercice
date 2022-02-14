class Settings():
    """Uma classe para armazenar todas as configurações da Invasão Alienígena"""

    def __init__(self):
        """Inicializa as configuraçoes do jogo"""
        # Configurações da tela
        self.screen_width = 930
        self.screen_height = 640
        self.bg_color = (230, 230, 230)

        # configurações de espaçonave
        self.ship_speed_factor = 0.75

        # configurações de projéteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Configurações de alienígenas
        self.alien_speed_factor = 0.70
        self.fleet_drop_speed = 10
        # fleet_direction igual a 1 representa a direita; -1 representa a esquerda
        self.fleet_direction = 1