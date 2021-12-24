from typing import Tuple

class Particle:
    def __init__(
        self, 
        pos:Tuple[float, float], 
        inertia_weight:float, 
        cognitive_coef:float, 
        social_coef:float, 
        equation
    ):
        self.pos = pos
        self.best_pos = pos
        self.inertia_weight = inertia_weight
        self.cognitive_coef = cognitive_coef
        self.social_coef = social_coef
        self.velocity:Tuple[float, float] = (0, 0)
        self.adaptation = float('inf')
        self.best_adaptation = self.adaptation
        self.equation = equation

    def calc_adaptation(self):
        self.adaptation = self.equation(*self.pos)
        if self.adaptation < self.best_adaptation:
            self.best_adaptation = self.adaptation
            self.best_pos = self.pos

    def update_position(
        self, 
        best_swarm_pos:Tuple[int, int],
        cognitive_rand:float,
        social_rand:float,
        min_xy:Tuple[float, float],
        max_xy:Tuple[float, float]
    ):
        """
        prędkosć = inercja + komponent poznawczy + komponent społeczny 

        gdzie:
        inercja = waga inercji * aktualna prędkość
        waga inercji w przedziale [0, 1]

        komponent poznawczy = przyśpieszenie poznawcze * (najlepsza pozycja cząstku - aktualna pozycja)
        przyśpieszenie poznawcze = współczynnik poznawczy * losowy poziom komponentu poznawczego
        współczynnik poznawczy w przedziale [0, 2]
        losowy poziom komponentu poznawczego w przedziale [0, 1]

        koponent społeczny = przyśpieszenie społeczne * (najlepsza pozycja w roju - aktualna pozycja)
        przyśpieszenie społeczne = współczynnik społeczny * losowy poziom komponentu społecznego
        losowy poziom komponentu społecznego w przedziale [0, 1]
        """
        inertia = (
            self.inertia_weight * self.velocity[0],
            self.inertia_weight * self.velocity[1]
        )
        
        cognitive_acc = self.cognitive_coef * cognitive_rand
        cognitive_comp = (
            cognitive_acc * (self.best_pos[0] - self.pos[0]),
            cognitive_acc * (self.best_pos[1] - self.pos[1])
        )

        social_acc = self.social_coef * social_rand
        social_comp = (
            social_acc * (best_swarm_pos[0] - self.pos[0]),
            social_acc * (best_swarm_pos[1] - self.pos[1])
        )

        self.velocity = (
            inertia[0] + cognitive_comp[0] + social_comp[0],
            inertia[1] + cognitive_comp[1] + social_comp[1]
        )
        self.pos = (
            max(
                min(
                    self.pos[0] + self.velocity[0], 
                    max_xy[0]
                ), 
                min_xy[0]
            ),
            max(
                min(
                    self.pos[1] + self.velocity[1], 
                    max_xy[1]
                ), 
                min_xy[1]
            )
        )
