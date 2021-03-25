import sys
from io import BytesIO

import matplotlib as mpl
import matplotlib.pyplot as plt
from PyQt5 import QtGui as QtG
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication
from matplotlib.backends.backend_agg import FigureCanvasAgg


# Source: https://stackoverflow.com/questions/32035251/displaying-latex-in-pyqt-pyside-qtablewidget
def latex_to_pixmap(latex, font_size=20):
    mpl.pyplot.close('all')  # TODO: This is dumb

    fig = mpl.pyplot.figure()
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

    q_image = QtG.QImage.rgbSwapped(QtG.QImage(buf, size[0], size[1], QtG.QImage.Format_ARGB32))

    q_pixmap = QtG.QPixmap(q_image)

    return q_pixmap


# Alternative latex rendering (I think SVG):
# https://gist.github.com/gmarull/dcc8218385014559c1ca46047457c364
# import sys
# from PyQt5.QtWidgets import QApplication
# from PyQt5.QtSvg import QSvgWidget
#
# from io import BytesIO
# import matplotlib.pyplot as plt
#
#
# # matplotlib: force computer modern font set
# plt.rc('mathtext', fontset='cm')
#
#
# def tex2svg(formula, fontsize=12, dpi=300):
#     """Render TeX formula to SVG.
#     Args:
#         formula (str): TeX formula.
#         fontsize (int, optional): Font size.
#         dpi (int, optional): DPI.
#     Returns:
#         str: SVG render.
#     """
#
#     fig = plt.figure(figsize=(0.01, 0.01))
#     fig.text(0, 0, r'${}$'.format(formula), fontsize=fontsize)
#
#     output = BytesIO()
#     fig.savefig(output, dpi=dpi, transparent=True, format='svg',
#                 bbox_inches='tight', pad_inches=0.0, frameon=False)
#     plt.close(fig)
#
#     output.seek(0)
#     return output.read()
#
#
# def main():
#     FORMULA = r'\int_{-\infty}^\infty e^{-x^2}\,dx = \sqrt{\pi}'
#
#     app = QApplication(sys.argv)
#
#     svg = QSvgWidget()
#     svg.load(tex2svg(FORMULA))
#     svg.show()
#
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()

def latex_to_svg(latex, font_size=12, dpi=300):
    fig = plt.figure(figsize=(0.01, 0.01))
    fig.text(0, 0, latex, fontsize=font_size)

    output_file = BytesIO()

    fig.savefig(output_file, dpi=dpi, transparent=True, format='svg', bbox_inches='tight', pad_inches=0.0)
    plt.close(fig)

    output_file.seek(0)
    return output_file.read()


if __name__ == '__main__':
    plt.rc('mathtext', fontset='cm')
    latex = r'$1 + \dfrac{1}{1 + \dfrac{1}{3}}$'
    app = QApplication(sys.argv)
    svg = QSvgWidget()
    svg.load(latex_to_svg(latex))
    svg.show()
    sys.exit(app.exec_())
