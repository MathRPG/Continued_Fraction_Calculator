# This did not work
# class MainWindowSVG(MainWindow):
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         plt.rc('mathtext', fontset='cm')
#         self.result_render_area = QtSvg.QSvgWidget()
#
#     def display_result_latex(self, latex: str):
#         fig = plt.figure(figsize=(0.01, 0.01))
#         fig.text(0, 0, f'${latex}$', fontsize=12)
#         output_file = io.BytesIO()
#         fig.savefig(output_file, dpi=300, transparent=True,
#                     format='svg', bbox_inches='tight', pad_inches=0.0)
#         plt.close(fig)
#         output_file.seek(0)
#         self.result_render_area.load(output_file.read())
#         self.result_render_area.show()

