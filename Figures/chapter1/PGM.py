"""
Script to create the PGM figure examples for chapter 1 of my PhD thesis
"""

import matplotlib.pyplot as plt
from matplotlib import rc
import daft

rc("font", family="serif", size=15)


def PGM_examples(render=True, save=True, fig_name="1pt2_pgm_examples.png"):
    y_height = 3
    pgm = daft.PGM([20, y_height], origin=[0, 0])

    print type(pgm)
    # retrieve the figure from daft
    ax = pgm._ctx.ax()

    # subplot one
    base_y = y_height / 2.0
    x_offset1 = 0
    y_offset1 = 0
    pgm.add_node(daft.Node("A1", r"A", 1 + x_offset1, base_y + y_offset1))
    pgm.add_node(daft.Node("B1", r"B", 2.5 + x_offset1, base_y + y_offset1,
                 observed=True))
    pgm.add_node(daft.Node("C1", r"C", 4 + x_offset1, base_y + y_offset1))
    pgm.add_edge("A1", "B1")
    pgm.add_edge("B1", "C1")

    # subplot two
    x_offset2 = 5
    y_offset2 = 0
    pgm.add_node(daft.Node("A2", r"A", 1 + x_offset2, base_y + y_offset2))
    pgm.add_node(daft.Node("B2", r"B", 2.5 + x_offset2, base_y + y_offset2,
                 observed=True))
    pgm.add_node(daft.Node("C2", r"C", 4 + x_offset2, base_y + y_offset2))
    pgm.add_edge("C2", "B2")
    pgm.add_edge("B2", "A2")

    # subplot three
    x_offset3 = 10
    y_offset3 = 0
    pgm.add_node(daft.Node("A3", r"A", 1 + x_offset3, base_y + y_offset3))
    pgm.add_node(daft.Node("B3", r"B", 2.5 + x_offset3, base_y + y_offset3,
                 observed=True))
    pgm.add_node(daft.Node("C3", r"C", 4 + x_offset3, base_y + y_offset3))
    pgm.add_edge("B3", "A3")
    pgm.add_edge("B3", "C3")

    # subplot four
    x_offset4 = 15
    y_offset4 = 0
    pgm.add_node(daft.Node("A4", r"A", 1 + x_offset4, base_y + y_offset4))
    pgm.add_node(daft.Node("B4", r"B", 2.5 + x_offset4, base_y + y_offset4,
                 observed=True))
    pgm.add_node(daft.Node("C4", r"C", 4 + x_offset4, base_y + y_offset4))
    pgm.add_edge("A4", "B4")
    pgm.add_edge("C4", "B4")

    # add labels
    base_x_loc = 4.0
    x_offset = 9.9
    fontsize = 20

    ax.annotate("Fig. 1.2.1", xy=(base_x_loc, base_y), fontsize=fontsize)
    ax.annotate("Fig. 1.2.2", xy=(base_x_loc + x_offset * 1, base_y),
                fontsize=fontsize)
    ax.annotate("Fig. 1.2.3", xy=(base_x_loc + x_offset * 2, base_y),
                fontsize=fontsize)
    ax.annotate("Fig. 1.2.4", xy=(base_x_loc + x_offset * 3, base_y),
                fontsize=fontsize)

    if render:
        pgm.render()

    if save:
        pgm.figure.savefig(fig_name)

    return pgm

if __name__ == "__main__":
    pgm = PGM_examples()
