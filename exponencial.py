from manim import *
import numpy as np

class CrescimentoExponencial(Scene):
    def construct(self):
        # Eixos
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 10, 2],
            axis_config={"include_numbers": False},
        )

        labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Função exponencial
        graph = axes.plot(lambda x: np.exp(x), color=BLUE)

        

        # Tracker para animar o ponto
        tracker = ValueTracker(0)

        # Ponto que se move ao longo da curva
        dot = Dot(color=YELLOW)

        # Linha vertical (mostra crescimento)
        line = always_redraw(lambda: axes.get_vertical_line(
            axes.c2p(tracker.get_value(), np.exp(tracker.get_value())),
            color=GRAY
        ))

        dot.add_updater(lambda d: d.move_to(
            axes.c2p(tracker.get_value(), np.exp(tracker.get_value()))
        ))

       

        # Animações
        self.play(Create(axes), Write(labels))
        self.play(Create(graph))
        self.play(FadeIn(dot), FadeIn(line))
        

        # Movimento do ponto (crescimento)
        self.play(tracker.animate.set_value(3.5), run_time=6, rate_func=smooth)

        self.wait()
