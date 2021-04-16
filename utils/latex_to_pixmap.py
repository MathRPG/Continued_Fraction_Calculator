import matplotlib.pyplot as plt
from PyQt5 import QtGui
from matplotlib.backends.backend_agg import FigureCanvasAgg


# Source: https://stackoverflow.com/questions/32035251/displaying-latex-in-pyqt-pyside-qtablewidget
def latex_to_pixmap(latex, font_size=12):
    fig = plt.figure()
    fig.patch.set_facecolor('none')
    fig.set_canvas(FigureCanvasAgg(fig))
    renderer = fig.canvas.get_renderer()

    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    t = ax.text(0, 0, latex, ha='left', va='bottom', fontsize=font_size)

    fig_width, fig_height = fig.get_size_inches()
    fig_bbox = fig.get_window_extent(renderer)
    text_bbox = t.get_window_extent(renderer)

    tight_fig_width = text_bbox.width * fig_width / fig_bbox.width
    tight_fig_height = text_bbox.height * fig_height / fig_bbox.height

    fig.set_size_inches(tight_fig_width, tight_fig_height)

    buf, size = fig.canvas.print_to_buffer()
    plt.close(fig)

    q_image = QtGui.QImage.rgbSwapped(QtGui.QImage(buf, size[0], size[1], QtGui.QImage.Format_ARGB32))
    q_pixmap = QtGui.QPixmap(q_image)

    return q_pixmap
