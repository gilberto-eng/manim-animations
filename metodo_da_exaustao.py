from manim import *
import math



config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 60

config.frame_width = 9
config.frame_height = 16


class pi(Scene):
    def construct(self):

        # ===== CONFIGURAÇÃO SHORTS =====
        config.frame_width = 9
        config.frame_height = 16
        self.camera.background_color = BLACK

        titulo = Text(
        "Área do círculo\npor polígonos",
         font_size=38
        )

        

        self.play(Write(titulo), run_time=1)
        self.play(titulo.animate.shift(2*UP))
        self.wait(1)


        # ===== RAIO =====
        R = 2

        # ===== CÍRCULO =====
        circulo = Circle(radius=R)
        circulo.set_stroke(WHITE, width=4)
        circulo.set_fill(BLUE_E, opacity=0.25)
        circulo.shift(LEFT * 1.8 + DOWN * 1.1)

        self.play(Create(circulo), run_time=1)
                # ===== RAIO (INÍCIO DO VÍDEO) =====
        centro = circulo.get_center()
        ponto_raio = centro + RIGHT * R

        raio = Line(
            centro,
            ponto_raio,
            color=YELLOW,
            stroke_width=4
        )

        texto_raio = MathTex(
            r"r = 2",
            font_size=36,
            color=YELLOW
        )
        texto_raio.next_to(raio, UP, buff=0.2)

        self.play(
            Create(raio),
            Write(texto_raio),
            run_time=1
        )
        raco=VGroup(raio, texto_raio)

        self.wait(1)
        self.play(FadeOut(raco))
        


        # ===== POLÍGONO INICIAL =====
        poligono = RegularPolygon(n=3, radius=R)
        poligono.set_fill(ORANGE, opacity=0.7)
        poligono.set_stroke(WHITE, width=3)
        poligono.move_to(circulo)
        poligono.shift(0.45*UP)

        self.play(Create(poligono), run_time=1)
        self.wait(1)

        # ===== FÓRMULA FIXA =====
        formula = MathTex(
            r"A_n = \frac{n R^2}{2}\,\sin\!\left(\frac{2\pi}{n}\right)",
            font_size=34
        )
        formula.to_edge(RIGHT, buff=0.6)
        formula.shift(DOWN * 0.8)

        self.play(Write(formula), run_time=1.2)
        self.wait(1.2)

        # ===== VALOR DA ÁREA (INICIAL) =====
        area = (3 / 2) * R**2 * math.sin(2 * math.pi / 3)

        valor_area = MathTex(
            rf"A_3 \approx {area:.2f}",
            font_size=34
        )
        valor_area.next_to(formula, DOWN, buff=0.6)

        self.play(Write(valor_area), run_time=1)
        self.wait(1.2)

        # ===== LOOP ATÉ 14 LADOS =====
        for n in range(4, 15):

            # pausa ANTES de trocar
            self.wait(0.8)

            novo_poligono = RegularPolygon(n=n, radius=R)
            novo_poligono.set_fill(ORANGE, opacity=0.7)
            novo_poligono.set_stroke(WHITE, width=3)
            novo_poligono.move_to(circulo.get_center())

            area = (n / 2) * R**2 * math.sin(2 * math.pi / n)

            novo_valor = MathTex(
                rf"A_{n} \approx {area:.2f}",
                font_size=34
            )
            novo_valor.next_to(formula, DOWN, buff=0.6)

            self.play(
                ReplacementTransform(poligono, novo_poligono),
                ReplacementTransform(valor_area, novo_valor),
                run_time=1.2
            )

            # pausa DEPOIS da troca
            poligono = novo_poligono
            valor_area = novo_valor
            self.wait(1)

                    # ===== PAUSA FINAL =====
                # ===== PAUSA FINAL =====
        self.wait(1.2)

        # ===== REMOVE O ÚLTIMO POLÍGONO =====
        self.play(FadeOut(poligono), run_time=1)

        # ===== LINHA DO RAIO =====
        centro = circulo.get_center()
        ponto_raio = centro + RIGHT * R

        raio = Line(
            centro,
            ponto_raio,
            color=YELLOW,
            stroke_width=4
        )

        texto_raio = MathTex(
            r"r = 2",
            font_size=36,
            color=YELLOW
        )
        texto_raio.next_to(raio, UP, buff=0.2)

        self.play(
            Create(raio),
            Write(texto_raio),
            run_time=1.2
        )

        self.wait(1.5)


        # ===== ÁREA REAL DO CÍRCULO =====
        area_circulo = PI * R**2

        area_real = MathTex(
            r"A = \pi R^2",
            font_size=36
        )
        area_real.to_edge(RIGHT, buff=0.6)
        area_real.shift(DOWN * 0.8)

        valor_real = MathTex(
            rf"A \approx {area_circulo:.2f}",
            font_size=36
        )
        valor_real.next_to(area_real, DOWN, buff=0.6)

        # Transição da área do polígono para a área real
        self.play(
            ReplacementTransform(formula, area_real),
            ReplacementTransform(valor_area, valor_real),
            run_time=1.4
        )

        self.wait(2)


        
