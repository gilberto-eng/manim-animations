from manim import *
import math
import numpy as np

class pitagoras(MovingCameraScene):
    def construct (self):
       
        A = np.array([-2, -1, 0])
        B = np.array([ 1, -1, 0])
        C = np.array([-2,  3, 0]) 
        E = np.array([ 6, -1, 0])
        F = np.array([ 6,  2, 0])


        #triangulo 1
        lA=Line(A, B)
        lB=Line(C, A)
        lC=Line(C, B)

        a = MathTex("a").next_to(lA, DOWN, buff=0.1)
        b = MathTex("b").next_to(lB, LEFT, buff=0.1)
        c = MathTex("c").next_to(lC, RIGHT, buff=0.1)
        c.next_to(0.1*RIGHT, 2.5*UP)
        letras=(a,b,c)

        triangulo=VGroup(lA,lB,lC)
        
        triangulo_area = Polygon(A, B, C)
        triangulo_area.set_fill(BLUE_C, opacity=0.0)
        triangulo_area.set_stroke(width=0)  # sem borda

        triangulo_area2 = Polygon(B, F, C)
        triangulo_area2.set_fill(YELLOW_C, opacity=0.0)
        triangulo_area2.set_stroke(width=0)  # sem borda

        triangulo_area3 = Polygon(B, E, F)
        triangulo_area3.set_fill(RED_C, opacity=0.0)
        triangulo_area3.set_stroke(width=0)  # sem borda
        
        



        area1 = MathTex(r"A_1")
        area1.move_to(triangulo_area.get_center())
        area1.next_to(2*LEFT)

        area2 = MathTex(r"A_2")
        area2.move_to(triangulo_area2.get_center())
        area2.next_to(1*RIGHT, 1*UP)

        area3 = MathTex(r"A_3")
        area3.move_to(triangulo_area3.get_center())
        area3.next_to(4*RIGHT)


        

        angulo_reto1 = RightAngle(lA, lB, quadrant=(1,-1), length=0.4, color=YELLOW)
        formula=MathTex("a^2 + b^2 = c^2 ?")
        formula.next_to(2*RIGHT, 1*UP)


        #triangulo2
        lb=Line(B, E)
        la=Line(F, E)
        lc=Line(B, F)
        ld= Line(C, F)
        

        a1 = MathTex("a").next_to(la, RIGHT, buff=0.1)
        b1 = MathTex("b").next_to(lb, DOWN, buff=0.1)
        c1 = MathTex("c").next_to(lc, LEFT, buff=0.1)
        c1.next_to(3*RIGHT, 1.5*UP)
        letras1=VGroup(a1,b1,c1)

        triangulo1=VGroup(lb,la,lc,ld)


        angulo_reto2 = RightAngle(lC, lc, quadrant=(-1, 1), length=0.4, color=YELLOW)
        angulo_reto3 = RightAngle(lb, la, quadrant=(-1,-1), length=0.4, color=YELLOW)
        
        angulo_teta1 = Angle(lb, lc, radius=0.4, color=YELLOW)
        theta = MathTex(r"\theta")
        theta.next_to(angulo_teta1, RIGHT*0.5)

        angulo_teta2 = Angle(lB, lC, radius=0.4, color=YELLOW)
        theta2 = MathTex(r"\theta")
        theta2.next_to(angulo_teta2, RIGHT*0.5)

        angulo_alfa1=Angle(lC, lA,quadrant=(-1,-1), radius=0.4, color=YELLOW)
        alfa1 = MathTex(r"\alpha")
        alfa1.next_to(angulo_alfa1, LEFT*0.5)

        angulo_alfa2=Angle(lc, la, quadrant=(-1,1),radius=0.4, color=YELLOW)
        alfa2 = MathTex(r"\alpha")
        alfa2.next_to(angulo_alfa2, RIGHT*0.5)



        angulos=VGroup(angulo_alfa2, alfa2 ,angulo_alfa1, alfa1, angulo_teta1, theta, angulo_teta2, theta2, angulo_reto1, angulo_reto2, angulo_reto3)

        figure_area=Polygon(A, E, F, C)
        figure_area.set_fill(color=PURPLE, opacity=0.0)
        area_f = MathTex(r"A_T")
        area_f.move_to(triangulo_area2.get_center())
        area_f.next_to(1*RIGHT, 1*UP)
       
        figure=VGroup(triangulo, triangulo1,a,b,c,a1,c1,b1, angulos, figure_area, area_f)
        figure2=VGroup( triangulo1,a1,c1,b1, angulos, figure_area, area_f)
        figure3=VGroup( triangulo1,a1,c1,b1, angulos,)

        areas=VGroup(triangulo_area, triangulo_area2, triangulo_area3, area1, area2, area3)
        
        demonstracao= MathTex(r"A_T = A_1 + A_2 + A_3")
        at = MathTex(r"\frac{(a+b)}{2}\cdot (a+b) = "r"\frac{ab}{2} + \frac{ab}{2} + \frac{c^2}{2}")

        demonstracao.next_to(figure, DOWN, buff=0.6)
        at.next_to(demonstracao, DOWN)
        at.align_to(demonstracao)
        at2 = MathTex(r"\frac{(a+b)^2}{", r"2", r"} = ",r"\frac{2ab}{", r"2", r"} + ",r"\frac{c^2}{", r"2", r"}")

        at2.next_to(at, DOWN)
        at2.align_to(at)
        at3 = MathTex(
    r"a^2 + ", r"{2ab}", r" + b^2 = ", r"{2ab}", r" + c^2"
)
        at3.next_to(at2, DOWN)
        at3.align_to(at2)
        at5=MathTex("a^2 + b^2 = c^2 ")
        at5.next_to(at3, DOWN)
        at5.align_to(at3)

        # riscos de cancelamento (forma estável e bonita)
        cortes = VGroup()

        for i in [1, 4, 7]:  # índices dos "2" nos denominadores
            centro = at2[i].get_center()
            corte = Line(
                centro + 0.15*LEFT + 0.15*UP,
                centro + 0.15*RIGHT + 0.15*DOWN,
                color=RED,
                stroke_width=4
            )
            cortes.add(corte)
        cortes.shift(1.6*UP)

       

        cqd=Text('C.Q.D')
        cqd.next_to(at5, RIGHT, buff=0.3)
        cqd.shift(4.4*UP)

        out_trapezio=VGroup(lc, lC, angulos, c, c1)

      
   


        self.play(Create(triangulo))
        self.play(Create(a))
        self.play(Create(b))
        self.play(Create(c))
        self.play(Create(angulo_reto1))
        self.play(Create(formula))
        self.wait(2)
        self.play(FadeOut(formula))

        self.camera.frame.save_state()

        
        self.play(Create(triangulo1), run_time=1.5)
        self.play(Create(angulo_reto2))
        self.play(Create(a1), run_time=1.5)
        self.play(Create(b1), run_time=1.5)
        self.play(Create(c1), run_time=1.5)
        self.play(Create(angulo_reto3))
        self.play(Create(angulo_teta1), Write(theta))
        self.play(Create(angulo_teta2), Write(theta2))
        self.play(Create(angulo_alfa1), Write(alfa1))
        self.play(Create(angulo_alfa2), Write(alfa2))
        self.play(triangulo_area.animate.set_fill(opacity=0.7), run_time=2)
        self.play(Create(area1))
        self.play(triangulo_area2.animate.set_fill(opacity=0.7), run_time=2)
        self.play(Create(area2))
        self.play(triangulo_area3.animate.set_fill(opacity=0.7), run_time=2)
        self.play(Create(area3))

        self.wait()
        self.play(FadeOut(areas))
        self.play(figure_area.animate.set_fill(opacity=0.8),run_time=2)
        self.play(FadeOut(out_trapezio))
        self.play(Create(area_f))
        self.play(figure.animate.shift(2*LEFT))
        
        
        self.play(Create(demonstracao))
        self.play(self.camera.frame.animate.move_to(demonstracao).scale(0.7), run_time=2)
        self.play(Restore(self.camera.frame), run_time=2)
        self.play(FadeIn(out_trapezio))
        self.play(FadeOut(figure_area, area_f))
        self.play(Create(at))
        self.play(FadeOut(demonstracao))
        self.play(at.animate.shift(1.2*UP))
        self.play(self.camera.frame.animate.move_to(at).scale(0.7), run_time=2)
        self.play(Create(at2))
        self.play(FadeOut(at))
        self.play(at2.animate.shift(1.6*UP))
        self.play(Create(cortes), run_time=1.5)
        self.play(Create(at3))
        self.play(FadeOut(cortes))
        self.play(FadeOut(at2))
        self.play(at3.animate.shift(3*UP))
        
        
        self.play(Create(at5))
        
        self.play(FadeOut(at3))
        self.play(FadeOut(figure3))
        self.play(at5.animate.shift(5.5*UP))
        self.play(Write(cqd))
        
        self.play(Restore(self.camera.frame), run_time=2)
        
        

        
        
        self.wait(2)

