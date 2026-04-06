
from manim import *
import numpy as np

class ErastotenesRaiosHorizontais(Scene):
    def construct(self):

        # Terra
        terra = Circle(radius=1.5, color=BLUE)
        terra.set_fill(BLUE_E, opacity=0.3)
        
        raio = 2

        # Ângulo entre as cidades
        angulo =15 * DEGREES  # use 7.2*DEGREES se quiser realista
      
        

        # Pontos na 
        
        centro = terra.get_center()
        ponto_syene = terra.point_at_angle(6)
        ponto_alex = terra.point_at_angle(angulo)
        pontog = terra.point_at_angle(7*PI/2)
        vetor_radial = normalize(ponto_alex)
        vetor_radial_syene = normalize(ponto_syene - centro)
        pontob = terra.point_at_angle(angulo)
        o =Point(terra.get_center())
        

        # ==============================
        # ESTACAS RADIAIS (CORRETO)
        # ==============================

       
        estaca_syene = Line(
            ponto_syene,
            ponto_syene + vetor_radial_syene*1,
            color=LIGHT_BROWN
        )

        

        estaca_alex = Line(
            pontob,
            pontob + vetor_radial * 1,
            color=LIGHT_BROWN
        )

        

        ponta_syene = estaca_syene.get_end()

        ponta_alex = estaca_alex.get_end()

        y0 = ponta_alex[1] - centro[1]
        x = np.sqrt(raio**2 - y0**2)
        ponto_borda = np.array([x, y0, 0])

        linha1 = Line(
            o, ponto_alex
        )

        linha2 = Line(
            o, ponto_syene
        )
        

       
        ponto_borda = np.array([
            centro[0] + x,
            ponta_alex[1],
            0
        ])

        # ==============================
        # RAIOS SOLARES HORIZONTAIS
        # ==============================

        raio_alex = Line(
            ponta_alex + vetor_radial_syene*8,
            ponta_alex,
            color = YELLOW
        )

        direcao_sol = normalize(-vetor_radial_syene)

        seta_alex = Arrow(
            raio_alex.point_from_proportion(0.6),
            raio_alex.point_from_proportion(0.6) + direcao_sol*0.5,
            buff = 0,
            max_tip_length_to_length_ratio= 0.5,
            color = YELLOW
        )

        raio_syene = Line(
            ponta_syene + vetor_radial_syene *8,
            ponta_syene,
            color=YELLOW
        )

        seta_syene = Arrow(
            raio_syene.point_from_proportion(0.6),
            raio_syene.point_from_proportion(0.6) + direcao_sol*0.5,
            buff = 0,
            max_tip_length_to_length_ratio= 0.5,
            color = YELLOW
        )

        hip = Line(ponta_alex,
                   ponta_alex - vetor_radial_syene*1.42,
                   color = YELLOW)

       
        # ==============================
        # ÂNGULO CORRETO ENTRE LINHAS
        # ==============================

        


        linha_raio = Line(
            ponta_alex,
            ponta_alex + LEFT*0.1
        )

        linha_estaca = Line(ponta_alex,
        ponta_alex - vetor_radial*2)
        


# Arco manual no interior
        arco = Angle(
            hip,
            linha_estaca,
            radius=0.6,
            color = GREEN,
            other_angle=False
        )

        anguloc = Angle(
            linha2,
            linha1,
            radius=0.6,
            color=GREEN
        )

        anguloc_lable = MathTex(r"\theta")
        anguloc_lable.next_to(anguloc, UP)

        angulo_label = MathTex(r"\theta")
        angulo_label.next_to(arco, UP)

        raio = MathTex("r")
        raio.next_to(linha2, DOWN)
        raio.shift(0.3*LEFT, 0.2*UP)

        point_alex = Dot(terra.point_at_angle(6), color=PURE_GREEN)
        point_syena = Dot(terra.point_at_angle(angulo), color=PURE_GREEN)
       
        distancia = ArcBetweenPoints(
          point_alex.get_center(),
          point_syena.get_center(),
          radius=terra.radius,
          color=RED_C
        )

       

        marca1 = Line(ORIGIN, RIGHT*0.2).move_to(point_alex)
        marca2 = Line(ORIGIN, RIGHT*0.2).move_to(point_syena)


        label_s = MathTex("S")
        label_s.next_to(distancia, RIGHT)


        alex_lable = Text("Alexandria", font_size= 20)
        alex_lable.next_to(point_alex, RIGHT)
        syena_lable = Text("Syene", font_size=20)
        syena_lable.next_to(point_syena, RIGHT)

        introd = VGroup(alex_lable, point_alex, point_syena, syena_lable)

        theta = MathTex(r"\theta\approx 7,2^\circ")
        theta.shift(3*LEFT)
        s = MathTex("S = 800km")
        s.shift(3*LEFT, 1*DOWN)

        prop = MathTex(r"\frac{S}{2\pi r} = \frac{\theta}{360^\circ}")
        prop.shift(3.3*LEFT)

        eq = MathTex(r"\frac{800}{2\pi r} = \frac{7,2}{360}")
        eq.shift(3.3*LEFT)

        eq2 = MathTex(r"\frac{800}{2\pi r} = \frac{1}{50}")
        eq2.shift(3.3*LEFT)

        eq3 = MathTex(r"2\pi r = 40000")
        eq3.shift(3.3*LEFT)

        eq4 = MathTex(r"r\approx\frac{40000}{6,29}")
        eq4.shift(3.3*LEFT)

        eq5 = MathTex(r"r\approx 6371km")
        eq5.shift(3.3*LEFT)

        

        self.play(Create(terra))
        self.wait(2)
        self.play(Create(point_alex), Create(point_syena), Write(alex_lable), Write(syena_lable))
        self.wait(2)
        self.play(FadeOut(introd))
        self.play(Create(estaca_syene), Create(estaca_alex))
        self.wait(3)
        self.play(Create(raio_syene), Create(seta_syene), Create(raio_alex), Create(hip), Create(seta_alex))
        self.wait(1)

        self.play(Create(arco), Write(angulo_label))
        
        self.wait(3)
        self.play(Create(o))
        self.play(Create(linha1), Create(linha2))
        self.play(Create(anguloc), Write(anguloc_lable))
        self.play(Write(raio))
        self.play(Create(distancia))
        self.play(Create(marca1), Create(marca2))
        self.play(Write(label_s)) 
        self.wait(2)
        self.play(Write(theta))
        self.wait()
        self.play(Write(s))
        self.wait()
        self.play(FadeOut(s), FadeOut(theta))
        self.play(Create(prop))
        self.wait()
        self.play(ReplacementTransform(prop, eq))
        self.wait(2)
        self.play(ReplacementTransform(eq, eq2))
        self.wait(2)
        self.play(ReplacementTransform(eq2, eq3))
        self.wait(2)
        self.play(ReplacementTransform(eq3, eq4))
        self.wait(2)
        self.play(ReplacementTransform(eq4, eq5))
        self.wait(2)