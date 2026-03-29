from manim import *

class euler(Scene):
    def construct(self):
        # Cria o símbolo 'e'
        e = MathTex("e").scale(6)  # começa grande (zoom)
        derivada = MathTex(r"f'(x) =lim_{h \to 0} \frac{f(x+h) - f(x)}{h}")
        expo = MathTex("f(x) = a^x")
        dexpo = MathTex(r"f'(x) = lim_{h \to 0} \frac{a^{x+h} - a^x}{h}")
        dexpo.next_to(expo, DOWN)
        dexpo2 = MathTex(r"= lim_{h \to 0} \frac{a^xa^h - a^x}{h}")       
        dexpo3 = MathTex(r"= lim_{h \to 0} \frac{a^x(a^h - 1)}{h}")     
        dexpo4 = MathTex(r"f'(x)= a^xlim_{h \to 0} \frac{a^h - 1}{h}")
        dexpo5 = MathTex(r"f'(0)= a^0lim_{h \to 0} \frac{a^h - 1}{h}")       
        dexpo6 = MathTex(r"lim_{h \to 0} \frac{a^h - 1}{h} = f'(0)")       
        conc = MathTex("f'(x) = a^xf'(0)")
        problem = MathTex(r"\text{queremos encontrar um número tal que} f'(0) = 1")
        problem2 = Paragraph(
        "pois encontrando esse número teremos",
        "uma função em que f'(x) = f(x)"
        )
        conclusao = MathTex(r"\text{existe um número a com}, 2<a<3 \text{ tal que } f'(0) = 1")
        conclusao.next_to(problem , DOWN)

        #exemples
        ex1 = MathTex(r"\text{para a} = 2,\ f'(0) = \lim_{h \to 0} \frac{2^h - 1}{h} \approx 0{,}69")
        ex2 = MathTex(r"\text{para a} = 3,\ f'(0) = \lim_{h \to 0} \frac{3^h - 1}{h} \approx 1{,}10")
        ex2.next_to(ex1, DOWN)

        d1 = MathTex(r"\frac{d}{dx}(2^x) \approx (0,69)2^x")
        d2 = MathTex(r"\frac{d}{dx}(3^x) \approx (1,10)3^x")
        d2.next_to(d1, DOWN)

        final = MathTex(r"\text{chamamos esse numero de } e")
        texto = Tex("e é um número tal que")
        formula = MathTex(r"\lim_{h \to 0} \frac{e^h - 1}{h} = 1")

        grupo = VGroup(texto, formula).arrange(DOWN)
        grupo.next_to(final, DOWN)
        valor = MathTex(r"e \approx 2{,}71828")

        #Gráfico

        axes = Axes(
            x_range=[-2,2,1],
            y_range=[0,8,1],
            axis_config={"include_numbers": True}
        )

        labels = axes.get_axis_labels(x_label="x", y_label="y")
        graph = axes.plot(lambda x: np.exp(x), color=BLUE)
        graph_label = MathTex("y = e^x").next_to(
            axes.c2p(-1.5, np.exp(-1.5)), UP
        )
        
        x0 = 0
        y0 = np.exp(x0)
        dot0 = Dot(axes.c2p(x0, y0), color=BLUE)
        tangent0 = axes.plot(
            lambda x: 1*(x - x0) + y0,
            color=PINK
        )
        label0 = Tex("inclinação = 1").next_to(
            axes.c2p(0.5, 1.2), RIGHT
        )
        x1 = 1
        y1 = np.exp(x1)
        dot1 = Dot(axes.c2p(x1, y1), color=BLUE)

        # Tangente em x = 1 (inclinação = e^x)
        slope1 = np.exp(x1)
        tangent1 = axes.plot(
            lambda x: slope1*(x - x1) + y1,
            color=PINK
        )

        label1 = MathTex(r"\text{inclinação } = e^x").next_to(
            axes.c2p(1.2, 4), RIGHT
            
        )

        point_label = MathTex(r"(x, e^x)").next_to(
            dot1, RIGHT
        )
        



        # Adiciona na cena
        self.play(FadeIn(e))
        self.wait(3)

        # "Desfaz o zoom" (volta ao tamanho normal)
        self.play(e.animate.scale(1/6), run_time=3)
        self.wait(1)

        # Fade out enquanto mantém o tamanho final
        self.play(FadeOut(e), run_time=2)
        self.play(Write(derivada))
        self.wait(3.5)
        self.play(FadeOut(derivada))
        self.play(Write(expo))
        self.wait()
        self.play(Write(dexpo))
        self.wait(3)
        self.play(FadeOut(expo))
        self.play(dexpo.animate.shift(2*UP))
        self.play(ReplacementTransform(dexpo, dexpo2))
        self.wait(5)
        self.play(ReplacementTransform(dexpo2, dexpo3))
        self.wait(3)
        self.play(ReplacementTransform(dexpo3, dexpo4))
        self.wait(5)
        self.play(ReplacementTransform(dexpo4, dexpo5))
        self.wait(3)
        self.play(ReplacementTransform(dexpo5, dexpo6))
        self.wait(2)
        self.play(ReplacementTransform(dexpo6, conc))
        self.wait(6)
        self.play(FadeOut(conc))
        self.play(Write(problem))
        self.wait(3)
        self.play(FadeOut(problem))
        self.play(Write(problem2))
        self.wait(3)
        self.play(FadeOut(problem2))
        self.play(Write(ex1))
        self.play(Write(ex2))
        self.wait()
        self.play(FadeOut(ex1), FadeOut(ex2))
        self.play(Create(d1))
        self.play(Create(d2))
        self.wait(2)
        self.play(FadeOut(d1), FadeOut(d2))
        self.wait()
        self.play(Write(conclusao))
        self.wait(5)
        self.play(FadeOut(conclusao))
        self.play(Write(final), Write(grupo))
        self.wait(5)
        self.play(FadeOut(final), FadeOut(grupo))
        self.play(Write(valor))
        self.wait()
        self.play(FadeOut(valor))
        self.play(Create(axes), Write(labels))
        self.play(Create(graph), Write(graph_label))
        self.wait()

        self.play(FadeIn(dot0), Create(tangent0), Write(label0))
        self.wait()

       
        self.wait(3)
