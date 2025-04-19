import xlrd
from datetime import date
from xlrd.xldate import xldate_as_datetime


def _load_sheet_holidays() -> xlrd.sheet.Sheet:
    """
    Carrega o arquivo dos feriados da anbima

    Returns:
        <class 'xlrd.sheet.Sheet'>: Um objeto contendo os dados do xls.

    Examples:
        >>> _load_sheet_holidays()
        <class 'xlrd.sheet.Sheet'>
    """
    workbook = xlrd.open_workbook("src/feriados/feriados_anbima.xls")
    sheet = workbook.sheet_by_index(0)
    return sheet


def holidays() -> list[date]:
    """
    Buscar os feriados nacionais da anbima.

    Returns:
        list[date]: Lista contendo datas de feriados no formato datetime.

    Examples:
        >>> holidays()
        date(2019, 6, 20)
        date(2019, 9, 7)
    """
    sheet = _load_sheet_holidays()
    return [
        xldate_as_datetime(sheet.cell_value(row_idx, 0), sheet.book.datemode).date()
        for row_idx in range(sheet.nrows)
        if isinstance(sheet.cell_value(row_idx, 0), float)
    ]
