"""
Script to create the PGM figure examples for chapter 1 of my PhD thesis
"""

import matplotlib.pyplot as plt
from matplotlib import rc
import daft
import sys

rc("font", family="serif", size=20)


def PGM_examples(render=True, save=True, fig_name="1pt2_pgm_examples.png"):
    y_height = 2
    pgm = daft.PGM([20, y_height], origin=[0, 0])

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
    y_label_height = base_y - 0.5

    ax.annotate("Fig. 1.2.1", xy=(base_x_loc, y_label_height),
                fontsize=fontsize)
    ax.annotate("Fig. 1.2.2", xy=(base_x_loc + x_offset * 1, y_label_height),
                fontsize=fontsize)
    ax.annotate("Fig. 1.2.3", xy=(base_x_loc + x_offset * 2, y_label_height),
                fontsize=fontsize)
    ax.annotate("Fig. 1.2.4", xy=(base_x_loc + x_offset * 3, y_label_height),
                fontsize=fontsize)

    if render:
        pgm.render()

    if save:
        pgm.figure.savefig(fig_name)

    return pgm


def SIDM_PGM(render=True, save=True, fig_name="SIDM_pgm.png"):
    y_height = 5
    pgm = daft.PGM([5, y_height], origin=[0, 0])

    # retrieve the figure from daft
    ax = pgm._ctx.ax()

    # subplot one
    base_y = 0
    node_scale = 2.
    pgm.add_node(daft.Node("sigma_SIDM", r"$\sigma_{\rm SIDM}$", 1.,
                           base_y + 4, scale=node_scale))
    pgm.add_node(daft.Node("s_merger", r"$s_{\rm merger}$", 4,
                           base_y + 2.5, scale=node_scale))
    pgm.add_node(daft.Node("Delta_s", r"$\Delta \vec{s}$", 2.5,
                           base_y + 1, observed=True, scale=node_scale))
    pgm.add_plate(daft.Plate([0.25, 0.25, 4.5, 3.],
                             label="clusters"))
    pgm.add_edge("sigma_SIDM", "Delta_s")
    pgm.add_edge("s_merger", "Delta_s")

    if render:
        pgm.render()

    if save:
        pgm.figure.savefig(fig_name)

    return pgm


def confounding_alpha_PGM(render=True, save=True,
                          fig_name="confounding_alpha_PGM.png"):
    y_height = 5
    pgm = daft.PGM([6, y_height], origin=[0, 0])

    # subplot one
    base_y = 0
    node_scale = 2.
    pgm.add_node(daft.Node("alpha", r"$\alpha$", 2.5,
                           base_y + 4, scale=node_scale))
    pgm.add_node(daft.Node("TSP", r"TSP", 1,
                           base_y + 1., scale=node_scale))
    pgm.add_node(daft.Node("Delta_s", r"$\Delta \vec{s}$", 4,
                           base_y + 1, observed=True, scale=node_scale))
    pgm.add_node(daft.Node("", r"$\Delta \vec{s}$", 4,
                           base_y + 1, observed=True, scale=node_scale))

    pgm.add_node(daft.Node("sigma_SIDM", r"$\sigma_{\rm SIDM}$", 5.,
                           base_y + 4, scale=node_scale))
    pgm.add_edge("alpha", "TSP")
    pgm.add_edge("alpha", "Delta_s")
    pgm.add_edge("TSP", "Delta_s")
    pgm.add_edge("sigma_SIDM", "Delta_s")

    if render:
        pgm.render()

    if save:
        pgm.figure.savefig(fig_name)

    return pgm


if __name__ == "__main__":

    if len(sys.argv) != 2:
        raise ValueError("Usage: Supply one integer argument, \n" +
                         "0 means make all plots\n" +
                         "1 means make 1st plot\n" +
                         "2 means make 2nd plot\n" +
                         "3 means make 3rd plot")
    if sys.argv[1] == "0":
        pgm1 = PGM_examples()
        pgm2 = SIDM_PGM()
        pgm3 = confounding_TSP_PGM()
    elif sys.argv[1] == "1":
        print "Making PGM example plot"
        pgm1 = PGM_examples()
    elif sys.argv[1] == "2":
        print "Making SIDM PGM plot"
        pgm2 = SIDM_PGM()
    elif sys.argv[1] == "3":
        print "Making TSP PGM plot"
        pgm3 = confounding_alpha_PGM()
