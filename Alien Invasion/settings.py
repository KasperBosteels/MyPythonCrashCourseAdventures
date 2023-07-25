class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.ship_speed = 0.4
        self.bg_color = (230,230,230)
        self.ship_limit = 3
        self.score_scale = 1.5

        self.bullet_limit = 3
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)

        self.alien_speed = 2.0
        self.fleet_drop_speed = 3.0
        self.fleet_direction = 1
        self.speedup_scale = 1.3
        self.initialize_dynamic_settings()
        self.alien_points = 50

    def initialize_dynamic_settings(self):
        self.ship_speed = 0.5
        self.bullet_speed = 1.0
        self.alien_speed = 0.2
        self.fleet_direction = 1

    def increase_speed(self):
        self.alien_points = int(self.alien_points * self.score_scale)
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale


