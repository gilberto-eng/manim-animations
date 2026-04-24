from manim import *
import numpy as np

class inclinacao(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-4, 4],
            y_range=[-4, 4],
        )

        labels = axes.get_axis_labels(
        x_label="t",
        y_label="s"
        )

        self.play(Create(axes), Write(labels))

        # InclinaÃ§Ã£o variÃ¡vel
        m = ValueTracker(0.5)

        # Pontos base
        x1 = 1
        x2 = 3

        # FunÃ§Ã£o da reta dinÃ¢mica
        def f(x):
            return m.get_value() * x
        
        function_label = MathTex("S(t)").set_color(YELLOW)
        function_label.shift(3*RIGHT, 1.5*UP)

        # Reta
        graph = always_redraw(
            lambda: axes.plot(f, x_range=[-4, 4], color=YELLOW)
        )
        

        # Pontos na reta
        p1 = always_redraw(lambda: Dot(axes.c2p(x1, f(x1)), color=BLUE))
        p2 = always_redraw(lambda: Dot(axes.c2p(x2, f(x2)), color=BLUE))

        # Î”x (horizontal)
        dx_line = always_redraw(
            lambda: Line(
                axes.c2p(x1, f(x1)),
                axes.c2p(x2, f(x1)),
                color=GREEN
            )
        )

        # Î”y (vertical)
        dy_line = always_redraw(
            lambda: Line(
                axes.c2p(x2, f(x1)),
                axes.c2p(x2, f(x2)),
                color=RED
            )
        )

        # Braces
        brace_dx = always_redraw(lambda: Brace(dx_line, DOWN))
        brace_dy = always_redraw(lambda: Brace(dy_line, RIGHT))

        # Labels
        label_dx = always_redraw(
            lambda: MathTex(r"\Delta t").next_to(brace_dx, DOWN)
        )

        label_dy = always_redraw(
            lambda: MathTex(r"\Delta s").next_to(brace_dy, RIGHT)
        )
        reta = always_redraw(
        lambda: Line(
        axes.c2p(x1, f(x1)),
        axes.c2p(x2, f(x2)),
        color=YELLOW
        )
        )
        reta = always_redraw(
        lambda: Line(
        axes.c2p(x1, f(x1)),
        axes.c2p(x2, f(x2)),
        color=YELLOW
        )
        )
        

        def angle_of_line(p1, p2):
           v = p2 - p1
           return np.arctan2(v[1], v[0])

        angulo = always_redraw(
        lambda: Arc(
        radius=0.8,
        start_angle=angle_of_line(
            axes.c2p(x1, f(x1)),
            axes.c2p(x2, f(x1))
        ),
        angle=angle_of_line(
            axes.c2p(x1, f(x1)),
            axes.c2p(x2, f(x2))
        ) - angle_of_line(
            axes.c2p(x1, f(x1)),
            axes.c2p(x2, f(x1))
        ),
        arc_center=axes.c2p(x1, f(x1)),
        color=WHITE
       )
       )
        

       

        angulo_label = always_redraw(
         lambda: MathTex(r"\theta").next_to(angulo, RIGHT)
        )

        

         
        tangente = MathTex(r"V_m = tg(\theta) = \frac{\Delta s}{\Delta t}")
        tangente.shift(3*UP, 5*LEFT)
        inclin = always_redraw(
        lambda: MathTex(
        r"V_m =",
        f"{m.get_value():.2f}"
        ).move_to(tangente.get_center())
        )
        

        # Adiciona tudo
        self.play(Create(graph))
        self.play(Write(function_label))
        self.wait(4)
        self.add( p1, p2)
        
        self.play(Create(dx_line), Create(dy_line), Create(brace_dx), Create(brace_dy),
                  Create(label_dx), Create(label_dy))
        self.play(Create(angulo), Write(angulo_label))
        self.play(FadeOut(function_label))
        self.play(Write(tangente))
        self.wait(2)
        

        # Anima a inclinaÃ§Ã£o
        self.play(FadeOut(tangente))
        self.play(Create(inclin))
        self.play(m.animate.set_value(2), run_time=5)
        self.wait()
        self.play(m.animate.set_value(-1), run_time=4)
        self.wait()
        self.play(m.animate.set_value(1), run_time=3)
                  
        self.wait(3)

class SecanteParaTangente(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-4, 5],
            y_range=[-1, 9],
        )

        def s(t):
            return t**2

        graph = axes.plot(s, color=YELLOW)

        # ðŸ”¥ Trackers
        t = ValueTracker(1)
        dt = ValueTracker(2)

        # Pontos
        p1 = always_redraw(
            lambda: Dot(
                axes.c2p(t.get_value(), s(t.get_value())),
                color=BLUE
            )
        )

        s_p1 = always_redraw(
            lambda: Dot(
                axes.c2p(0, s(t.get_value())),
                color=GRAY
            )
        )

        p1_linha = always_redraw(
         lambda: DashedLine(
          p1.get_center(),
          s_p1.get_center()
         )
        )
        p1linha_label = always_redraw(
        lambda: MathTex("s(t)").next_to(s_p1, LEFT)
        )

        p2 = always_redraw(
            lambda: Dot(
                axes.c2p(t.get_value() + dt.get_value(), s(t.get_value() + dt.get_value())),
                color=BLUE
            )
        )

        s_p2 = always_redraw(
            lambda: Dot(
                axes.c2p(0, s(t.get_value() + dt.get_value())),
                color=GRAY
            )
        )

        p2_linha = always_redraw(
        lambda: DashedLine(
         axes.c2p(t.get_value() + dt.get_value(), s(t.get_value() + dt.get_value())),
         axes.c2p(0, s(t.get_value() + dt.get_value()))
        )
        )
        p2linha_label = always_redraw(
         lambda: MathTex("s(t + \\Delta t)").next_to(
          axes.c2p(0, s(t.get_value() + dt.get_value())),
          LEFT
         )
        )


        # ðŸ”¥ Secante
        secante = always_redraw(
            lambda: Line(
                p1.get_center(),
                p2.get_center(),
                color=GREEN
            )
        )

        # Î”t (linha horizontal)
        dt_line = always_redraw(
            lambda: Line(
                axes.c2p(t.get_value(), s(t.get_value())),
                axes.c2p(t.get_value() + dt.get_value(), s(t.get_value())),
                color=WHITE
            )
        )

        ds_line = always_redraw(
           lambda: Line(
              axes.c2p(t.get_value() + dt.get_value(), s(t.get_value())),
              axes.c2p(t.get_value() + dt.get_value(), s(t.get_value() + dt.get_value())),
              color=RED
           )
        )

        # Brace Î”t
        brace_dt = always_redraw(
            lambda: Brace(dt_line, DOWN)
        )

        label_dt = always_redraw(
            lambda: MathTex(r"\Delta t").next_to(brace_dt, DOWN)
        )

         # Brace Î”s
        brace_ds = always_redraw(
            lambda: Brace(ds_line, RIGHT)
        )

        label_ds = always_redraw(
            lambda: MathTex(r"\Delta s").next_to(brace_ds, RIGHT)
        )

        label_p1 = always_redraw(
         lambda: MathTex("t").next_to(p1, UP)
         )

        label_p2 = always_redraw(
         lambda: MathTex("t + \Delta t").next_to(p2, UP)
        )

        funcao_label = MathTex("s(t)")
        funcao_label.set_color(YELLOW)

        limite = MathTex(r"\Delta t \to 0")
        limite2 = MathTex(r"\Delta t \neq 0").next_to(limite, DOWN)
        limite3 = MathTex(r"lim_{\Delta t \to 0}")

        delta_s = VGroup(label_ds, p1linha_label, p2linha_label)
        equacao = MathTex(
        r"\Delta s",
        "=",
        r"s(t + \Delta t)",
        "-",
        r"s(t)"
        )

        delta_t = MathTex("\Delta t = \Delta t")
        delta_t.next_to(equacao)
        delta_t.shift(1.2*DOWN, 5.1*LEFT)
        m = MathTex(r"m",  "=", r"tg(\theta)", "=",  r"\frac{\Delta s}{\Delta t}",  "=", r"\frac{ s(t + h) - s(t)}{\Delta t}")
        

        self.play(Create(axes), Create(graph), Write(funcao_label))
        self.wait(2)
        self.play(FadeOut(funcao_label))
        self.add(p1, p2)
        self.play(Write(label_p1), Write( label_p2))
        self.wait()
        self.play(Create(secante))
        self.wait()

        self.play(Create(dt_line), Create(brace_dt), Write(label_dt))
        self.play(Create(ds_line), Create(brace_ds), Write(label_ds))

        self.wait(1)

        self.play(Create(s_p1), Create(p1_linha), Write(p1linha_label))
        self.play(Create(s_p2),Create(p2_linha),Write(p2linha_label))

        # ðŸ”¥ ANIMAÃ‡ÃƒO PRINCIPAL
        self.play(dt.animate.set_value(1.2), run_time=4)
        self.wait()
        self.play(dt.animate.set_value(0.7), run_time=4)
        self.wait()
        self.play(dt.animate.set_value(0.5), run_time=4)
        self.wait()
        self.play(dt.animate.set_value(1.5), run_time=2)
        self.wait()
        self.play(
        FadeOut(
          VGroup(
            axes, graph, secante,
            dt_line, ds_line,
            brace_dt, brace_ds,
            p1, p2, s_p1, s_p2, p1_linha, p2_linha,label_p1,label_p2,p1linha_label,
            p2linha_label,label_ds,delta_t

          )
        )
        )
        self.play(TransformMatchingTex(label_dt, limite))
        self.play(Write(limite2))
        self.wait(3)
        self.play(FadeOut(limite2), TransformMatchingTex(limite, limite3))
        self.wait(2)
        self.play(FadeOut(limite3))
        self.play(FadeIn(
          VGroup(
            axes, graph, secante,
            dt_line, ds_line,
            brace_dt, brace_ds,
            p1, p2, s_p1, s_p2, p1_linha, p2_linha,label_p1,label_p2,p1linha_label,
            p2linha_label,label_ds,label_dt

          )
        ))
        self.wait(3)
        self.play(FadeOut(
          VGroup(
            axes, graph, secante,
            dt_line, ds_line,
            brace_dt, brace_ds,
            p1, p2, s_p1, s_p2, p1_linha, p2_linha,label_p1,label_p2,label_dt
            

          )
        ))
      
        self.play(
        TransformMatchingTex(
        delta_s,
        equacao
        )
        )
        self.play(Write(delta_t))
        self.wait(3)
        self.play(FadeOut(delta_t), FadeOut(equacao))
        self.play(Write(m))
        self.wait(2)
        self.play(
        FadeOut(VGroup(*m[:-1]))
        )
        self.play(m[-1].animate.move_to(ORIGIN))
        self.wait(2)

class derivada(Scene):
    def construct(self):
        eq1 = MathTex(r"\frac{ s(t + \Delta t) - s(t)}{\Delta t}")
        eq2 = MathTex(r"\Delta t \to 0")
        eq3 = MathTex(r"\Delta t \neq 0")
        eq3.shift(1*DOWN)
        final = MathTex(r"V = lim_{\Delta t \to 0} \frac{s(t + \Delta t) - s(t)}{\Delta t}")
        
        sorvetao = MathTex(r"S = S_0 + V_0t + \frac{1}{2}at^2")
        s1 = MathTex(r"S(t + \Delta t) = V_0(t + \Delta t) + \frac{1}{2}a(t + \Delta t)^2")
        s2 = MathTex(r"S(t) = V_0t + \frac{1}{2}at^2").next_to(s1, DOWN)
        v1 = MathTex(r"lim_{\Delta t \to 0}\frac{V_0(t + \Delta t) + \frac{1}{2}a(t + \Delta t)^2 - V_0t + \frac{1}{2}at^2}{\Delta t}").shift(3*UP)
        v2 = MathTex(r"lim_{\Delta t \to 0}\frac{V_0t + V_0\Delta t + \frac{1}{2}a (t^2 + 2t\Delta t + \Delta t^2) - (V_0t + \frac{1}{2}at^2)}{\Delta t}").next_to(v1, DOWN)
        v3 = MathTex(r"lim_{\Delta t \to 0}\frac{V_0t + V_0\Delta t + \frac{1}{2}at^2 + at\Delta t + \frac{1}{2}a\Delta t^2) - (V_0t + \frac{1}{2}at^2)}{\Delta t}").next_to(v2, DOWN)
        v4 = MathTex(r"lim_{\Delta t \to 0}\frac{V_0t + V_0\Delta t + \frac{1}{2}at^2 + at\Delta t + \frac{1}{2}a\Delta t^2) - V_0t - \frac{1}{2}at^2}{\Delta t}").next_to(v3, DOWN)
        v5 = MathTex(r"lim_{\Delta t \to 0}\frac{V_0\Delta t + at\Delta t + \frac{1}{2}a\Delta t^2}{\Delta t}").next_to(v4, DOWN)    
        v6 = MathTex(r"lim_{\Delta t \to 0}V_0 + at + \frac{1}{2}a\Delta t").shift(1.5*UP)
        v7 = MathTex("V = V_0 + at")
        box = SurroundingRectangle(v7, color=YELLOW)  
        fade = VGroup(v1, v2, v3, v4)

        self.play(Write(eq1))
        self.wait(2)
        self.play(ReplacementTransform(eq1, final))
        self.wait(4)
        self.play(FadeOut(final))
        self.play(Write(sorvetao))
        self.wait(2)
        self.play(FadeOut(sorvetao))
        self.play(Write(s1))
        self.wait(3)
        self.play(Write(s2))
        self.wait(2)
        self.play(FadeOut(s1), FadeOut(s2))
        self.play(FadeIn(final))
        self.wait(2)
        self.play(TransformMatchingTex(final, v1))
        self.wait(4)
        self.play(Write(v2))
        self.wait(4)
        self.play(Write(v3))
        self.wait(4)
        self.play(Write(v4))
        self.wait(4)
        self.play(Write(v5))
        self.wait(2)
        self.play(FadeOut(fade))
        self.play(v5.animate.to_edge(UP))
        self.wait(2)
        self.play(Write(v6))
        self.wait(5)
        self.play(Write(v7))
        self.play(Create(box))
        self.wait(2)

class equacoes(Scene):
    def construct(self):
        eq = MathTex(r"S = S_0 + V_0t + \frac{1}{2}at^2")
        eq1 = MathTex("S_0 = 0").next_to(eq, DOWN)
        eq2 = MathTex(r"S = V_0t + \frac{1}{2}at^2")
        self.play(Write(eq))
        self.wait(2)
        self.play(Write(eq1))
        self.wait(2)
        self.play(FadeOut(eq), FadeOut(eq1))
        self.play(Write(eq2))
        self.wait(2)
        

