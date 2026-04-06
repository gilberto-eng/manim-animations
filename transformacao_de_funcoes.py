from manim import *
from scipy import special
import math
import numpy as np


config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16



class eixos(Scene):
    def construct(self):

        titulo= Text("Evolução das Funções")

        #criando eixos
        eixo = Axes(
            x_range=[-4, 4, 1],#começo,fim,passo
            y_range=[-4, 4, 1],#começo,fim,passo
            x_length= 8, #comprimento eixo x
            y_length= 8, #comprimento eixo y
            axis_config = {'color': WHITE, 'include_ticks': True},
            tips = True


            
        )

       

        #dando nome para os eixos
        labels = eixo.get_axis_labels(x_label='x', y_label='y')

        
        funcao0 = eixo.plot(lambda x: 1, color= PURE_GREEN)
        #nome da função
        funcao0_lable=MathTex('f(x)=1', color=PURE_GREEN).next_to(funcao0, DOWN)
        #criando função
        funcao1 = eixo.plot(lambda x: x, color= PINK)
        #nome da função
        funcao1_lable=MathTex('f(x)=x', color=PINK).next_to(funcao1, LEFT)
        funcao1_lable.shift(2*RIGHT,1*UP)

        funcao2 = eixo.plot(lambda x: x**2, color= PURE_BLUE)
        funcao2_lable=MathTex('f(x)=x^2', color=PURE_BLUE).next_to(funcao2, DOWN)

        funcao2_1 = eixo.plot(lambda x: x**3, color= LOGO_BLUE)
        funcao2_1lable=MathTex('f(x)=x^3', color=LOGO_BLUE).next_to(funcao2_1, LEFT)
        funcao2_1lable.shift(2*RIGHT,1*UP)

        funcao3 = eixo.plot(lambda x: 2**x, color=RED_C)
        funcao3_lable=MathTex('f(x)=2^x', color=RED_C).next_to(funcao3, DOWN)

        funcao4 = eixo.plot(lambda x: np.log(x), x_range=[0.01,4], color= PURPLE_D)
        funcao4_lable=MathTex('f(x)=ln(x)', color=PURPLE_D).next_to(funcao4, LEFT)
        funcao4_lable.shift(3*RIGHT)

        funcao5 = eixo.plot(lambda x: np.sin(x), color= YELLOW_A)
        funcao5_lable=MathTex('f(x)=sen(x)', color=YELLOW_A).next_to(funcao5, UP)

        funcao6 = eixo.plot(lambda x: np.tan(x),x_range=[-PI, PI], discontinuities=[-PI/2, PI/2], dt=0.1, color= ORANGE)
        funcao6_lable=MathTex('f(x)=tan(x)', color=ORANGE).next_to(funcao6, RIGHT)
        funcao6_lable.shift(2*LEFT,1*UP)

        funcao7 = eixo.plot(lambda x: np.sin(1/x), color= YELLOW_A)
        funcao7_lable=MathTex('f(x)=sen(1/x)', color=YELLOW_A).next_to(funcao7, DOWN)

        funcaofe = eixo.plot(lambda x: np.tan(1/x),x_range=[-1, -0.05], color= LIGHT_PINK)
        

        funcaofr = eixo.plot(lambda x: np.tan(1/x),x_range=[0.05,1], color= LIGHT_PINK)
        funcaofr_l=MathTex('f(x)=tan(1/x)', color=LIGHT_PINK).next_to(funcaofe, LEFT)
        funcaofr_l.shift(0.5*RIGHT)

        

        final=VGroup(funcaofr, funcaofe)

                # -----------------------
        # ESPIRAL FINAL
        # -----------------------

        espiral = ParametricFunction(
            lambda t: np.array([
                0.25 * t * np.cos(t),
                0.25 * t * np.sin(t),
                0
            ]),
            t_range=[0, 8*PI],
            color=GOLD
        )

        espiral_lable = MathTex(
            r"x=t\cos(t)\quad y=t\sin(t)",
            color=GOLD
        ).scale(0.7)

        espiral_lable.to_edge(DOWN)



        self.play(Write(titulo))
        self.wait()
        self.play(FadeOut(titulo))
        self.play(Create(eixo))
        self.play(Create(labels))
        self.play(Create(funcao0,), Write(funcao0_lable))
        self.wait(2)
        self.play(ReplacementTransform(funcao0, funcao1), ReplacementTransform(funcao0_lable, funcao1_lable))
        self.wait(2)
        self.play(ReplacementTransform(funcao1, funcao2), ReplacementTransform(funcao1_lable, funcao2_lable))
        self.wait(2)
        self.play(ReplacementTransform(funcao2, funcao2_1), ReplacementTransform(funcao2_lable, funcao2_1lable))
        self.wait(2)
        self.play(ReplacementTransform(funcao2_1, funcao3), ReplacementTransform(funcao2_1lable, funcao3_lable))
        self.wait(2)
        self.play(ReplacementTransform(funcao3, funcao4), ReplacementTransform(funcao3_lable, funcao4_lable))
        self.wait(2)
        self.play(ReplacementTransform(funcao4, funcao5), ReplacementTransform(funcao4_lable, funcao5_lable))
        self.wait(2)
        self.play(ReplacementTransform(funcao5, funcao6), ReplacementTransform(funcao5_lable, funcao6_lable))
        self.wait(2)
        self.play(ReplacementTransform(funcao6, funcao7), ReplacementTransform(funcao6_lable, funcao7_lable))
        self.wait(2)
        self.play(ReplacementTransform(funcao7, final), ReplacementTransform(funcao7_lable, funcaofr_l))
        self.wait(2)
        self.play(ReplacementTransform(final, espiral), ReplacementTransform(funcaofr_l, espiral_lable), run_time=3)
        self.play(Rotate(espiral, angle=2*PI),run_time=2)
        self.wait(2)
