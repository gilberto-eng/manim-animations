from manim import *
import numpy as np


config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class CorrenteAlternada(Scene):
    def construct(self):
        self.camera.background_color = "#08111f"

        title = Text("Corrente alternada", font_size=44, color=WHITE)
        subtitle = Text(
            "O sentido da corrente inverte periodicamente",
            font_size=24,
            color=GRAY_A,
        )
        title.to_edge(UP, buff=0.5)
        subtitle.next_to(title, DOWN, buff=0.12)

        top_panel = RoundedRectangle(
            width=8.3,
            height=5.2,
            corner_radius=0.18,
            stroke_color=BLUE_E,
            stroke_width=2,
            fill_color=BLACK,
            fill_opacity=0.24,
        ).move_to(UP * 2.35)

        graph_panel = RoundedRectangle(
            width=8.3,
            height=5.25,
            corner_radius=0.18,
            stroke_color=GREEN_E,
            stroke_width=2,
            fill_color=BLACK,
            fill_opacity=0.24,
        ).move_to(DOWN * 3.05)

        top_label = Text("Circuito", font_size=22, color=BLUE_A)
        top_label.next_to(top_panel.get_top(), DOWN, buff=0.15).align_to(top_panel, LEFT).shift(
            RIGHT * 0.35
        )

        graph_label = Text("Forma de onda da corrente", font_size=22, color=GREEN_A)
        graph_label.next_to(graph_panel.get_top(), DOWN, buff=0.15).align_to(
            graph_panel, LEFT
        ).shift(RIGHT * 0.35)

        circuit_y = 2.95
        bottom_y = 1.15
        left_x = -3.3
        right_x = 3.3

        source = Circle(
            radius=0.42,
            stroke_color=BLUE_C,
            stroke_width=3,
            fill_color=BLUE_E,
            fill_opacity=0.2,
        ).move_to(LEFT * 2.55 + UP * circuit_y)
        source_label = MathTex(r"\sim").scale(1.1).move_to(source)
        source_caption = Text("fonte AC", font_size=18, color=BLUE_A)
        source_caption.next_to(source, DOWN, buff=0.12)

        load = RoundedRectangle(
            width=1.05,
            height=0.9,
            corner_radius=0.12,
            stroke_color=ORANGE,
            stroke_width=3,
            fill_color=ORANGE,
            fill_opacity=0.14,
        ).move_to(RIGHT * 2.55 + UP * circuit_y)
        load_label = MathTex("R").scale(0.95).move_to(load)
        load_caption = Text("carga", font_size=18, color=ORANGE)
        load_caption.next_to(load, DOWN, buff=0.12)

        top_left_wire = Line(
            LEFT * 3.95 + UP * circuit_y,
            source.get_left() + LEFT * 0.05,
            color=GRAY_B,
            stroke_width=10,
        )
        top_mid_wire = Line(
            source.get_right() + RIGHT * 0.05,
            load.get_left() + LEFT * 0.05,
            color=GRAY_B,
            stroke_width=10,
        )
        top_right_wire = Line(
            load.get_right() + RIGHT * 0.05,
            RIGHT * 3.95 + UP * circuit_y,
            color=GRAY_B,
            stroke_width=10,
        )
        bottom_wire = Line(
            RIGHT * 3.95 + UP * bottom_y,
            LEFT * 3.95 + UP * bottom_y,
            color=GRAY_B,
            stroke_width=10,
        )
        left_vertical = Line(
            LEFT * 3.95 + UP * circuit_y,
            LEFT * 3.95 + UP * bottom_y,
            color=GRAY_B,
            stroke_width=10,
        )
        right_vertical = Line(
            RIGHT * 3.95 + UP * circuit_y,
            RIGHT * 3.95 + UP * bottom_y,
            color=GRAY_B,
            stroke_width=10,
        )

        phase = ValueTracker(0.0)

        def current_sign():
            return np.sin(phase.get_value())

        arrow_y = circuit_y + 0.63
        current_arrow_right = Arrow(
            start=np.array([-1.75, arrow_y, 0]),
            end=np.array([1.75, arrow_y, 0]),
            buff=0,
            stroke_width=8,
            max_tip_length_to_length_ratio=0.22,
            color=YELLOW,
        )
        current_arrow_left = Arrow(
            start=np.array([1.75, arrow_y, 0]),
            end=np.array([-1.75, arrow_y, 0]),
            buff=0,
            stroke_width=8,
            max_tip_length_to_length_ratio=0.22,
            color=RED_C,
        )
        current_arrow = VGroup(current_arrow_right, current_arrow_left)

        def update_current_arrows(_mob):
            s = current_sign()
            current_arrow_right.set_opacity(0.22 + 0.78 * max(0.0, s))
            current_arrow_left.set_opacity(0.22 + 0.78 * max(0.0, -s))

        current_arrow.add_updater(update_current_arrows)
        current_text = always_redraw(
            lambda: MathTex(r"i(t)").scale(0.8).next_to(current_arrow, UP, buff=0.1)
        )
        current_value_label = Text("valor instantaneo", font_size=16, color=GRAY_A)
        current_value_number = DecimalNumber(
            0,
            num_decimal_places=2,
            color=WHITE,
        ).scale(0.7)
        current_value = VGroup(current_value_label, current_value_number).arrange(
            DOWN, buff=0.06
        )
        current_value.to_corner(UR, buff=0.35).shift(DOWN * 1.3)
        current_value_number.add_updater(lambda mob: mob.set_value(current_sign()))

        electron_xs = np.linspace(-1.8, 1.8, 7)
        electron_phases = np.linspace(0, np.pi, len(electron_xs))
        electrons = VGroup()
        for x0, offset in zip(electron_xs, electron_phases):
            dot = Dot(radius=0.075, color=TEAL_A)

            def updater(mob, x_base=x0, phase_offset=offset):
                displacement = 0.5 * np.sin(phase.get_value() + phase_offset)
                mob.move_to(np.array([x_base + displacement, circuit_y, 0]))

            dot.add_updater(updater)
            electrons.add(dot)

        graph_axes = Axes(
            x_range=[0, 4 * np.pi, np.pi],
            y_range=[-1.5, 1.5, 0.5],
            x_length=7.1,
            y_length=2.8,
            axis_config={"color": GRAY_B, "stroke_width": 2},
            tips=False,
        ).move_to(DOWN * 2.45)

        graph_window = 4 * np.pi

        graph_curve = always_redraw(
            lambda: graph_axes.plot(
                lambda x: np.sin(x + phase.get_value()),
                x_range=[0, graph_window],
                color=BLUE_C,
                stroke_width=4,
            )
        )

        moving_dot = always_redraw(
            lambda: Dot(
                graph_axes.c2p(
                    graph_window,
                    np.sin(graph_window + phase.get_value()),
                ),
                radius=0.08,
                color=YELLOW,
            )
        )

        tracer = always_redraw(
            lambda: DashedLine(
                graph_axes.c2p(
                    graph_window,
                    0.0,
                ),
                graph_axes.c2p(
                    graph_window,
                    (
                        0.08
                        if abs(np.sin(graph_window + phase.get_value())) < 0.08
                        else np.sign(np.sin(graph_window + phase.get_value()))
                        * abs(np.sin(graph_window + phase.get_value()))
                    ),
                ),
                color=YELLOW,
                dash_length=0.08,
                stroke_width=2,
            )
        )

        graph_formula = MathTex(r"i(t)=I_0\sin(\omega t)").scale(0.8)
        graph_formula.next_to(graph_axes, UP, buff=0.18).align_to(graph_axes, LEFT)
        graph_formula.shift(3.5*RIGHT, 0.5*DOWN)

        positive_tag = Text("sentido positivo", font_size=16, color=YELLOW)
        negative_tag = Text("sentido negativo", font_size=16, color=RED_C)
        polarity_tags = VGroup(positive_tag, negative_tag).arrange(RIGHT, buff=0.4)
        polarity_tags.next_to(graph_axes, DOWN, buff=0.18)

        self.play(FadeIn(title, shift=DOWN), FadeIn(subtitle, shift=DOWN))
        self.play(FadeIn(top_panel), FadeIn(graph_panel))
        self.play(FadeIn(top_label), FadeIn(graph_label))

        self.play(
            Create(left_vertical),
            Create(right_vertical),
            Create(bottom_wire),
            Create(top_left_wire),
            Create(top_mid_wire),
            Create(top_right_wire),
        )
        self.play(
            FadeIn(source),
            FadeIn(source_label),
            FadeIn(source_caption),
            FadeIn(load),
            FadeIn(load_label),
            FadeIn(load_caption),
        )
        self.play(FadeIn(current_arrow), FadeIn(current_text), FadeIn(current_value))
        self.play(FadeIn(electrons, lag_ratio=0.08), run_time=0.8)

        self.play(Create(graph_axes), Create(graph_curve))
        self.play(FadeIn(graph_formula), FadeIn(polarity_tags))
        self.play(FadeIn(tracer), FadeIn(moving_dot))

        self.wait(0.4)
        self.play(phase.animate.set_value(4 * np.pi), run_time=9, rate_func=linear)
        self.wait(1.5)
