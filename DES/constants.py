from .Extract_ConstantesDES import recupConstantesDES


class Constants:
    def __init__(self):
        self.const_dict = recupConstantesDES('Bonus/ConstantesDES.txt')

    def cp1(self):
        return self.const_dict['CP_1']

    def cp2(self):
        return self.const_dict['CP_2']
