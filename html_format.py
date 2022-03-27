import difflib


def html_style():
    """ This function to keep the sytle or formatting
    for the html output file and can be edited if needed.
    """

    styles = """
        table.diff {font-family:"Courier"; border:medium; font-size:90%; color:Black}
        .diff_header {background-color:#e0e0e0}
        td.diff_header {text-align:right}
        .diff_next {background-color:#c0c0c0}
        .diff_add {background-color:#aaffaa}
        .diff_chg {background-color:#ffff77}
        .diff_sub {background-color:#ffaaaa}"""

    template = """
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
                  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html>
        <head>
            <meta http-equiv="Content-Type"
                  content="text/html; charset=%(charset)s" />
            <title> ConfDiff </title>
            <style type="text/css">%(styles)s</style>
        </head>
        <body>
            <h1 style="font-family:monospace;text-align:center;color:DodgerBlue;background-color:White;margin:0;padding:0;">
              <b>Configuration Difference (ConfDiff)</b>
            </h1>
            <h4 style="font-family:monospace;text-align:center;padding:0px;margin-top:auto;margin-bottom:auto;"><span id='date-time'></span></h4>
                %(legend)s
                %(table)s
            <br>
        </body>
        <script>
            var dt = new Date();
            document.getElementById('date-time').innerHTML=dt;
        </script>
        </html>"""

    table_template = """
        <table class="diff" id="difflib_chg_%(prefix)s_top"
               cellspacing="0" cellpadding="3" align="center" rules="groups" >
            <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup>
            <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup>
                %(header_row)s
            <tbody>
                %(data_rows)s
            </tbody>
        </table>"""

    legend = """
        <span style="text-align:center;background-color:white;color:Black;font-size:16px;padding:0px;margin-top:auto;margin-bottom:auto;">
            <p style="font-family:Courier;"><b>Legends: </b>
            <a class="diff_add">&nbsp;Added&nbsp</a>
            <a class="diff_chg"> Changed</a>
            <a class="diff_sub"> Deleted</a></p>
        </span>
        <span style="text-align:center;background-color:white;color:Black;font-size:16px;padding:0px;margin-top:auto;margin-bottom:auto;">
            <p style="font-family:Courier;">(<a><u>f</u></a>)irst change;
            <a>(<a><u>n</u></a>)ext change;
            <a>(<a><u>t</u></a>)op</p>
        </span>
        """

    d = difflib.HtmlDiff(wrapcolumn=100)
    d._file_template = template
    d._styles = styles
    d._legend = legend
    d._table_template = table_template

    return d
