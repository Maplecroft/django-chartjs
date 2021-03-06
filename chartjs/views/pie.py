from . import HighchartsView


class HighchartsPieView(HighchartsView):
    chart_type = 'pie'

    def get_series(self):
        series = super(HighchartsPieView, self).get_series()
        for serie in series:
            serie.update({'type': 'pie'})
        return series


class HighchartsDonutView(HighchartsPieView):
    inner_size = '50%'

    def get_series(self):
        series = super(HighchartsDonutView, self).get_series()
        for serie in series:
            serie.update({"innerSize": self.inner_size})
        return series

    def get_plot_options(self):
        options = super(HighchartsDonutView, self).get_plot_options()
        options['pie'].update({"showInLegend": True})
        return options
