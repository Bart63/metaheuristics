from typing import Dict, List
from math import pi, e, exp, cos, sin

params:Dict[str, List] = {
    "particles_count": [50, 80, 100],
    
    "inertia_weight" : [0.1, 0.3, 0.5, 0.7, 0.9], # w przedziale [0, 1]
    "cognitive_coef" : [0.1, 0.3, 0.5, 0.7, 1, 1.3, 1.5, 1.7, 1.9], # w przedziale [0, 2]
    "social_coef" : [0.1, 0.3, 0.5, 0.7, 1, 1.3, 1.5, 1.7, 1.9], # w przedziale [0, 2]
    
    "max_iterations": [1000],
    "max_stagnations": [200], 

    "equation_params" : [
        {
            "equation" : {
                "Ackley" : 
                    lambda x, y : 
                        -20 * exp(
                            -0.2 * ((0.5 * (x*x + y*y)) ** 0.5)
                        ) - exp(
                            0.5 * (cos(2*pi*x) + cos(2*pi*y))
                        ) + e + 20,
            },
            "min_x" : -5,
            "max_x" : 5,
            "min_y" : -5,
            "max_y" : 5
        },
        {
            "equation" : {
                "Beale" : 
                    lambda x, y :
                        (1.5 - x + x*y) * (1.5 - x + x*y)
                        + (2.25 - x + x * (y*y)) * (2.25 - x + x * (y*y))
                        + (2.625 - x + x * (y*y)) * (2.625 - x + x * (y*y)),
            },
            "min_x" : -4.5,
            "max_x" : 4.5,
            "min_y" : -4.5,
            "max_y" : 4.5
        },
        {
            "equation" : {
                "GoldsteinPrice" : 
                    lambda x, y :
                        (
                            1 + (x + y + 1) * (x + y + 1)
                            * (19 - 14*x + 3*(x*x) - 14*y + 6*x*y + 3*(y*y))
                        ) * (
                            30 + ((2*x - 3*y) * (2*x - 3*y)) 
                            * (18 - 32*x + 12*(x*x) + 48*y - 36*x*y + 27*(y*y))
                        ),
            },
            "min_x" : -2,
            "max_x" : 2,
            "min_y" : -2,
            "max_y" : 2
        },
        {
            "equation" : {
                "Booth" : 
                    lambda x, y :
                        (x + 2*y - 7) * (x + 2*y - 7)
                        + (2*x + y - 5) * (2*x + y - 5),
            },
            "min_x" : -10,
            "max_x" : 10,
            "min_y" : -10,
            "max_y" : 10
        },
        {
            "equation" : {
                "Bukin" : 
                    lambda x, y :
                        100 * (abs(y - 0.01 * x*x) ** 0.5)
                        + 0.01 * abs(x + 10),
            },
            "min_x" : -15,
            "max_x" : -5,
            "min_y" : -3,
            "max_y" : 3
        },
        {
            "equation" : {
                "Himmelblau" : 
                    lambda x, y :
                        (x*x + y - 11) * (x*x + y - 11) 
                        + (x + y*y - 7) * (x + y*y - 7),
            },
            "min_x" : -5,
            "max_x" : 5,
            "min_y" : -5,
            "max_y" : 5
        },
        {
            "equation" : {
                "Easom" : 
                    lambda x, y :
                        - cos(x) * cos(y) * exp(
                            - (
                                (x - pi) * (x - pi)
                                + (y - pi) * (y - pi) 
                            )
                        ),
            },
            "min_x" : -5,
            "max_x" : 5,
            "min_y" : -5,
            "max_y" : 5
        },
        {
            "equation" : {
                "Cross_in_tray" : 
                    lambda x, y :
                        - 0.0001 * (
                            abs(sin(x) * sin(y) * exp(abs(
                                    100
                                    - (x*x + y*y) / pi 
                                ))
                            ) + 1
                        ) ** 0.1,
            },
            "min_x" : -10,
            "max_x" : 10,
            "min_y" : -10,
            "max_y" : 10
        },
        {
            "equation" : {
                "Eggholder" : 
                    lambda x, y :
                        - (y + 47) * sin(
                            abs(x/2 + y + 47) ** 0.5
                        ) - x * sin(
                            abs(x - y - 47) ** 0.5
                        ),
            },
            "min_x" : -512,
            "max_x" : 512,
            "min_y" : -512,
            "max_y" : 512
        },
        {
            "equation" : {
                "Holder_table" : 
                    lambda x, y :
                        - abs(
                            sin(x) 
                            * cos(y) 
                            * exp(
                                abs(
                                1 - (((x*x + y*y) ** 0.5) / pi)
                            ))
                        ),
            },
            "min_x" : -10,
            "max_x" : 10,
            "min_y" : -10,
            "max_y" : 10
        },
        {
            "equation" : {
                "Schaffer2" : 
                    lambda x, y :
                        0.5 + (
                            sin(x*x - y*y) 
                            * sin(x*x - y*y) - 0.5
                        ) / (
                            (1 + 0.001*(x*x + y*y)) 
                            * (1 + 0.001*(x*x + y*y))
                            
                        ),
            },
            "min_x" : -100,
            "max_x" : 100,
            "min_y" : -100,
            "max_y" : 100
        },
        {
            "equation" : {
                "Schaffer4" : 
                    lambda x, y :
                        0.5 + (
                            cos(sin(abs(x*x - y*y)))
                            * cos(sin(abs(x*x - y*y)))
                            - 0.5
                        ) / (
                            (1 + 0.001*(x*x + y*y))
                            * (1 + 0.001*(x*x + y*y))
                        ),
            },
            "min_x" : -100,
            "max_x" : 100,
            "min_y" : -100,
            "max_y" : 100
        }
    ]
}
