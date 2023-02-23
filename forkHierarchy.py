from manim import *

class ForkingHierarchy(Scene):
    def construct(self):

        #============================================================================================================================================#
        # Title and Subtitle
        title = Text("Fork Hierarchy").align_to(ORIGIN, LEFT).to_edge(UL)
        self.play(Create(title))

        subtitle = Text("A simple Fork() implemented in C:", slant=ITALIC).scale(0.75).next_to(title, DOWN, buff=0.27).align_to(title, LEFT)
        self.play(Create(subtitle))

        #============================================================================================================================================#
        # Display the program code
        rendered_code = Code(
            "fork_1.c",
            tab_width=4,
            background_stroke_width=1,
            background_stroke_color=WHITE,
            insert_line_no=True,
            style=Code.styles_list[15],
            background="window",
            language="C",
        ).next_to(subtitle, DOWN).to_edge(LEFT)

        self.play(Write(rendered_code))
        self.wait(2)

        #============================================================================================================================================#
        # Define the nodes and their labels
        node1 = Circle(radius=0.27, fill_opacity=0.3, stroke_width=1)
        node2 = Circle(radius=0.27, fill_opacity=0.3, stroke_width=1)
        node3 = Circle(radius=0.27, fill_opacity=0.3, stroke_width=1)
        node4 = Circle(radius=0.27, fill_opacity=0.3, stroke_width=1)
        node5 = Circle(radius=0.27, fill_opacity=0.3, stroke_width=1)
        node6 = Circle(radius=0.27, fill_opacity=0.3, stroke_width=1)
        node7 = Circle(radius=0.27, fill_opacity=0.3, stroke_width=1)
        node8 = Circle(radius=0.27, fill_opacity=0.3, stroke_width=1)
        node9 = Circle(radius=0.27, fill_opacity=0.3, stroke_width=1)
        node10 = Circle(radius=0.27, fill_opacity=0.3, stroke_width=1)
        node11 = Circle(radius=0.27, fill_opacity=0.3, stroke_width=1)
        node12 = Circle(radius=0.27, fill_opacity=0.3, stroke_width=1)
        node13 = Circle(radius=0.27, fill_opacity=0.3, stroke_width=1)
        node14 = Circle(radius=0.27, fill_opacity=0.3, stroke_width=1)
        node15 = Circle(radius=0.27, fill_opacity=0.3, stroke_width=1)

        label1 = Text("Parent", font_size=16, weight=BOLD).set_color(BLUE)
        label2 = Text("Parent", font_size=16, weight=BOLD).set_color(BLUE)
        label3 = Text("C 1", font_size=16, weight=BOLD).set_color(BLUE)

        label4 = Text("Parent", font_size=16, weight=BOLD).set_color(BLUE)
        label5 = Text("C 2", font_size=16, weight=BOLD).set_color(BLUE)
        label6 = Text("C 3", font_size=16, weight=BOLD).set_color(BLUE)
        label7 = Text("C 1", font_size=16, weight=BOLD).set_color(BLUE)

        label8 = Text("Parent", font_size=16, weight=BOLD).set_color(BLUE)
        label9 = Text("C 4", font_size=16, weight=BOLD).set_color(BLUE)
        label10 = Text("C 2", font_size=16, weight=BOLD).set_color(BLUE)
        label11 = Text("C 5", font_size=16, weight=BOLD).set_color(BLUE)
        label12 = Text("C 3", font_size=16, weight=BOLD).set_color(BLUE)
        label13 = Text("C 6", font_size=16, weight=BOLD).set_color(BLUE)
        label14 = Text("C 1", font_size=16, weight=BOLD).set_color(BLUE)
        label15 = Text("C 7", font_size=16, weight=BOLD).set_color(BLUE)

        # Position the nodes and labels
        node1.move_to(RIGHT) # Parent
        label1.move_to(node1.get_center())

        node2.next_to(node1, DOWN, buff=0.4) # Parent
        label2.move_to(node2.get_center())

        node3.next_to(node2, RIGHT, buff=0.4) # Child 1
        label3.move_to(node3.get_center())

        node4.next_to(node2, DOWN, buff=0.4) # Parent
        label4.move_to(node4.get_center())

        node5.next_to(node4, RIGHT, buff=0.4) # Child 2
        label5.move_to(node5.get_center())

        node6.next_to(node5, RIGHT, buff=0.4) # Child 3
        label6.move_to(node6.get_center())

        node7.next_to(node6, RIGHT, buff=0.4) # Child 1
        label7.move_to(node7.get_center())

        node8.next_to(node4, DOWN, buff=0.4) # Parent
        label8.move_to(node8.get_center())

        node9.next_to(node8, RIGHT, buff=0.4) # Child 4
        label9.move_to(node9.get_center())

        node10.next_to(node9, RIGHT, buff=0.4) # Child 2
        label10.move_to(node10.get_center())

        node11.next_to(node10, RIGHT, buff=0.4) # Child 5
        label11.move_to(node11.get_center())

        node12.next_to(node11, RIGHT, buff=0.4) # Child 3
        label12.move_to(node12.get_center())

        node13.next_to(node12, RIGHT, buff=0.4) # Child 6
        label13.move_to(node13.get_center())

        node14.next_to(node13, RIGHT, buff=0.4) # Child 1
        label14.move_to(node14.get_center())

        node15.next_to(node14, RIGHT, buff=0.4) # Child 7
        label15.move_to(node15.get_center())


        # Create the edges

        edge1 = ArcBetweenPoints(node1.get_center(),node2.get_center(),radius=-3)
        edge2 = ArcBetweenPoints(node1.get_center(), node3.get_center(),radius=4)

        edge3 = ArcBetweenPoints(node2.get_center(), node4.get_center(),radius=-3)
        edge4 = ArcBetweenPoints(node2.get_center(), node5.get_center(),radius=4)
        
        edge5 = ArcBetweenPoints(node3.get_center(), node6.get_center(),radius=-3)
        edge6 = ArcBetweenPoints(node3.get_center(), node7.get_center(),radius=4)

        edge7 = ArcBetweenPoints(node4.get_center(), node8.get_center(),radius=-3)
        edge8 = ArcBetweenPoints(node4.get_center(), node9.get_center(),radius=4)

        edge9 = ArcBetweenPoints(node5.get_center(), node10.get_center(),radius=-3)
        edge10 = ArcBetweenPoints(node5.get_center(), node11.get_center(),radius=4)

        edge11 = ArcBetweenPoints(node6.get_center(), node12.get_center(),radius=5)
        edge12 = ArcBetweenPoints(node6.get_center(), node13.get_center(),radius=-7)

        edge13 = ArcBetweenPoints(node7.get_center(), node14.get_center(),radius=-4)
        edge14 = ArcBetweenPoints(node7.get_center(), node15.get_center(),radius=-5)

        # Create the tree and add to the scene
        node_tree = VGroup(node1, node2, node3, node4, node5, node6, node7, node8, node9, node10, node11, node12, node13, node14, node15, label1, label2, label3, label4, label5, label6, label7, label8, label9, label10, label11, label12, label13, label14, label15, edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12, edge13, edge14).next_to(rendered_code).to_edge(LEFT*13.7)
        self.play(Write(node_tree))
        self.wait(2)