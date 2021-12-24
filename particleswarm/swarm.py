from typing import Dict, List
from particle import Particle
from random import uniform, random

class Swarm:
    def __init__(self, params:Dict):
        self.params = params
        self.best_particle:Particle = None
        self.configurate_particles()

    def configurate_particles(self):
        self.swarm:List[Particle] = [
            Particle(
                (
                    uniform(self.params['equation_params']['min_x'], self.params['equation_params']['max_x']),
                    uniform(self.params['equation_params']['min_y'], self.params['equation_params']['max_y'])
                ),
                self.params['inertia_weight'],
                self.params['cognitive_coef'],
                self.params['social_coef'],
                list(self.params['equation_params']['equation'].values())[0]
            )
            for _ in range(self.params['particles_count'])
        ]
    
    def update_best_particle(self):
        for p in self.swarm:
            p.calc_adaptation()
            best_swarm_adaptation = (
                float('inf') 
                if self.best_particle == None 
                else self.best_particle.best_adaptation
            )
            if p.best_adaptation < best_swarm_adaptation:
                self.best_particle = p 

    def update_swarm_pos(self):
        cognitive_rand, social_rand = random(), random()
        for p in self.swarm:
            p.update_position(
                self.best_particle.pos,
                cognitive_rand,
                social_rand,
                (
                    self.params['equation_params']['min_x'], 
                    self.params['equation_params']['min_y']
                ),
                (
                    self.params['equation_params']['max_x'], 
                    self.params['equation_params']['max_y']
                )
            )

    def get_positions(self):
        return [
            p.pos for p in self.swarm
        ]
