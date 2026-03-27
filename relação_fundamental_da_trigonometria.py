from manim import *
import numpy as np


class RelacaoFundamentalTrigonometria(Scene):
    def construct(self):
        # Título
        title = MathTex(r"\sin^2(\theta) + \cos^2(\theta) = 1")
        title.to_edge(UP)
        subtitle = Text("Relação fundamental da trigonometria", font_size=28)
        subtitle.next_to(title, DOWN, buff=0.25)

        # Plano cartesiano
        plane = NumberPlane(
            x_range=[-1.8, 1.8, 1],
            y_range=[-1.8, 1.8, 1],
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.35,
            },
            axis_config={"include_numbers": False},
        )

        circle = Circle(radius=1, color=WHITE)
        circle.move_to(ORIGIN)

        theta = ValueTracker(0.7)

        point = always_redraw(
            lambda: Dot(
                point=[
                    np.cos(theta.get_value()),
                    np.sin(theta.get_value()),
                    0,
                ],
                color=YELLOW,
            )
        )

        radius_line = always_redraw(
            lambda: Line(ORIGIN, point.get_center(), color=YELLOW)
        )

        x_proj = always_redraw(
            lambda: DashedLine(
                start=[point.get_x(), 0, 0],
                end=point.get_center(),
                color=BLUE,
                dash_length=0.08,
            )
        )

        y_proj = always_redraw(
            lambda: DashedLine(
                start=[0, point.get_y(), 0],
                end=point.get_center(),
                color=GREEN,
                dash_length=0.08,
            )
        )

        x_axis_segment = always_redraw(
            lambda: Line(ORIGIN, [point.get_x(), 0, 0], color=BLUE)
        )

        y_axis_segment = always_redraw(
            lambda: Line(ORIGIN, [0, point.get_y(), 0], color=GREEN)
        )

        angle_arc = always_redraw(
            lambda: Arc(
                radius=0.35,
                start_angle=0,
                angle=theta.get_value(),
                color=RED,
            )
        )

        angle_label = always_redraw(
            lambda: MathTex(r"\theta")
            .scale(0.8)
            .set_color(RED)
            .move_to(0.45 * np.array([np.cos(theta.get_value() / 2), np.sin(theta.get_value() / 2), 0]))
        )

        cos_label = always_redraw(
            lambda: MathTex(r"\cos(\theta)").scale(0.85).set_color(BLUE).next_to(
                [point.get_x() / 2, 0, 0], DOWN, buff=0.15
            )
        )

        sin_label = always_redraw(
            lambda: MathTex(r"\sin(\theta)").scale(0.85).set_color(GREEN).next_to(
                [0, point.get_y() / 2, 0], LEFT, buff=0.15
            )
        )

        radius_label = always_redraw(
            lambda: MathTex(r"1").scale(0.9).next_to(radius_line, UP, buff=0.15)
        )

        identity_box = RoundedRectangle(
            corner_radius=0.2,
            width=5.8,
            height=1.1,
            color=WHITE,
            stroke_opacity=0.55,
        ).to_edge(DOWN)

        identity = MathTex(
            r"\cos^2(\theta) + \sin^2(\theta) = 1"
        ).move_to(identity_box.get_center())

        self.play(FadeIn(title, shift=DOWN), FadeIn(subtitle, shift=DOWN))
        self.play(Create(plane), Create(circle))
        self.play(Create(radius_line), FadeIn(point), Create(angle_arc), FadeIn(angle_label))
        self.play(Create(x_axis_segment), Create(y_axis_segment), Create(x_proj), Create(y_proj))
        self.play(FadeIn(cos_label), FadeIn(sin_label), FadeIn(radius_label))

        self.wait(1)

        self.play(FadeIn(identity_box), Write(identity))
        self.wait(1)

        self.play(theta.animate.set_value(2.2), run_time=3)
        self.play(theta.animate.set_value(0.9), run_time=2)
        self.wait(2)
