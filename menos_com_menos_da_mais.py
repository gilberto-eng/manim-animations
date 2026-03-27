from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class MenosComMenosGeometrico(Scene):
    def construct(self):
        self.camera.background_color = "#0f172a"

        title = Text("Por que (-)x(-)=(+)?", font_size=40, color=WHITE)
        title.to_edge(UP, buff=0.35)
        
        outer_w = 4.7
        outer_h = 3.8
        b = 1.2
        d = 1.0
        left_w = outer_w - b
        bottom_h = outer_h - d
        center = UP * 2.05

        outer = Rectangle(
            width=outer_w,
            height=outer_h,
            color=WHITE,
            stroke_width=3,
        ).move_to(center)

        vertical_cut = DashedLine(
            start=center + RIGHT * (outer_w / 2 - b) + DOWN * (outer_h / 2),
            end=center + RIGHT * (outer_w / 2 - b) + UP * (outer_h / 2),
            color=YELLOW,
            dash_length=0.1,
        )
        horizontal_cut = DashedLine(
            start=center + LEFT * (outer_w / 2) + UP * (outer_h / 2 - d),
            end=center + RIGHT * (outer_w / 2) + UP * (outer_h / 2 - d),
            color=YELLOW,
            dash_length=0.1,
        )

        bottom_left = Rectangle(
            width=left_w,
            height=bottom_h,
            stroke_color=BLUE_C,
            stroke_width=2,
            fill_color=BLUE_C,
            fill_opacity=0.18,
        ).move_to(center + LEFT * (b / 2) + DOWN * (d / 2))

        bottom_right = Rectangle(
            width=b,
            height=bottom_h,
            stroke_color=RED_C,
            stroke_width=2,
            fill_color=RED_C,
            fill_opacity=0.22,
        ).move_to(center + RIGHT * (left_w / 2) + DOWN * (d / 2))

        top_left = Rectangle(
            width=left_w,
            height=d,
            stroke_color=PURPLE_C,
            stroke_width=2,
            fill_color=PURPLE_C,
            fill_opacity=0.20,
        ).move_to(center + LEFT * (b / 2) + UP * (bottom_h / 2))

        top_right = Rectangle(
            width=b,
            height=d,
            stroke_color=GREEN_C,
            stroke_width=2,
            fill_color=GREEN_C,
            fill_opacity=0.32,
        ).move_to(center + RIGHT * (left_w / 2) + UP * (bottom_h / 2))

        a_top_brace = Brace(outer, UP, buff=0.12, color=WHITE)
        c_right_brace = Brace(outer, RIGHT, buff=0.12, color=WHITE)
        ab_brace = Brace(bottom_left, DOWN, buff=0.08, color=BLUE_A)
        b_brace = Brace(bottom_right, DOWN, buff=0.08, color=RED_A)
        cd_brace = Brace(bottom_left, LEFT, buff=0.08, color=BLUE_A)
        d_brace = Brace(top_left, LEFT, buff=0.08, color=PURPLE_A)

        a_top_label = MathTex("a").scale(1.12).next_to(a_top_brace, UP, buff=0.05)
        c_right_label = MathTex("c").scale(1.12).next_to(c_right_brace, RIGHT, buff=0.05)
        ab_label = MathTex("a-b").scale(1.0).next_to(ab_brace, DOWN, buff=0.05)
        b_label = MathTex("b").scale(1.0).next_to(b_brace, DOWN, buff=0.05)
        cd_label = MathTex("c-d").scale(1.0).next_to(cd_brace, LEFT, buff=0.05)
        d_label = MathTex("d").scale(1.0).next_to(d_brace, LEFT, buff=0.05)

        bl_area = MathTex(r"(a-b)(c-d)").scale(0.95).move_to(bottom_left.get_center())
        br_area = MathTex(r"b(c-d)").scale(0.95).move_to(bottom_right.get_center())
        tl_area = MathTex(r"(a-b)d").scale(0.95).move_to(top_left.get_center())
        tr_area = MathTex(r"bd").scale(1.0).move_to(top_right.get_center())

       

        formula_title = Text("Expansão da área", font_size=28, color=BLUE_A)
        formula_title.move_to(2.05 * DOWN)

        e1 = MathTex(r"ac = (a-b)(c-d) + b(c-d) + (a-b)d + bd").scale(0.64)
        e2 = MathTex(
            r"ac =",
            r"(a-b)(c-d)",
            r"+ bc",
            r"- bd",
            r"+ ad",
            r"- bd",
            r"+ bd",
        ).scale(0.64)
        e3 = MathTex(r"\Rightarrow\ (a-b)(c-d) = ac - ad - bc + bd").scale(0.66)

       

        formula_steps = VGroup(
            MathTex(r"ac = (a-b)(c-d) + b(c-d) + (a-b)d + bd").scale(0.64),
            e2,
            MathTex(r"\Rightarrow\ (a-b)(c-d) = ac - ad - bc + bd").scale(0.66),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        formula_steps.next_to(formula_title, DOWN, buff=0.22)

        bd_minus = formula_steps[1][5]
        bd_plus = formula_steps[1][6]
        corte = VGroup(
            Line(
                bd_minus.get_left(),
                bd_minus.get_right(),
                color=RED,
                stroke_width=6,
            ),
            Line(
                bd_plus.get_left(),
                bd_plus.get_right(),
                color=RED,
                stroke_width=6,
            ),
        )
    

        note = Text(
            "O termo bd volta com sinal positivo.",
            font_size=22,
            color=GRAY_A,
        )
        note.next_to(formula_steps, DOWN, buff=0.32)

        note1 = Text(
            "Portanto (-b)x(-d) = +bd",
            font_size=22,
            color=GRAY_A,
        )
        note1.next_to(note, DOWN, buff=0.24)

        area = MathTex("A = c.a").scale(1.15)
        area.move_to(outer.get_center())

        self.play(Write(title))
        self.wait(0.5)
        self.play(FadeOut(title))

        self.play(Create(outer))
        self.play(FadeIn(a_top_brace))
        self.play(FadeIn(c_right_brace))
        self.play(FadeIn(a_top_label), FadeIn(c_right_label))
        self.play(outer.animate.set_fill(BLUE, opacity=0.8))
        self.play(Write(area))
        self.wait(0.3)
        self.play(outer.animate.set_fill(BLUE, opacity=0))
        self.play(FadeOut(area))
        self.wait()

        self.play(Create(vertical_cut))
        self.play(Create(horizontal_cut))
        self.play(
          
            FadeIn(b_brace),
        
            FadeIn(d_brace),
          
            FadeIn(b_label),
            
            FadeIn(d_label),
        )
        self.wait()

        self.play(
            FadeIn(ab_brace),
            FadeIn(ab_label)
        )

        self.play(FadeIn(cd_label),
            FadeIn(cd_brace))

        self.play(FadeIn(bottom_left))
        self.play(FadeIn(bl_area))
        self.play(FadeIn(bottom_right))
        self.play(FadeIn(br_area))
        self.play(FadeIn(top_left))
        self.play(FadeIn(tl_area))
        self.play(FadeIn(top_right))
        self.play(FadeIn(tr_area))
        self.wait()

        self.play(FadeIn(formula_title))
        self.play(Write(formula_steps[0]))
        self.wait()
        self.play(Write(formula_steps[1]))
        self.wait()
        self.play(Create(corte))
        self.play(Write(formula_steps[2]))
        self.play(FadeIn(note))
        self.play(FadeIn(note1))
        self.play(Circumscribe(top_right, color=GREEN, time_width=0.8))

        highlight = SurroundingRectangle(formula_steps[2], color=YELLOW, buff=0.2)
        self.play(Create(highlight))
        self.wait(2)
