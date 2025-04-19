import pytest
from datetime import date

from src.core import holidays


@pytest.mark.parametrize(
    "expected_date",
    [
        date(2025, 1, 1),  # Confraternização Universal
        date(2025, 3, 3),  # Carnaval (ponto facultativo)
        date(2025, 3, 4),  # Carnaval (ponto facultativo)
        date(2025, 4, 18),  # Paixão de Cristo (Sexta-feira Santa)
        date(2025, 4, 21),  # Tiradentes
        date(2025, 5, 1),  # Dia do Trabalhador
        date(2025, 6, 19),  # Corpus Christi (ponto facultativo)
        date(2025, 9, 7),  # Independência do Brasil
        date(2025, 10, 12),  # Nossa Senhora Aparecida
        date(2025, 11, 2),  # Finados
        date(2025, 11, 15),  # Proclamação da República
        date(2025, 11, 20),  # Dia Nacional de Zumbi e da Consciência Negra
        date(2025, 12, 25),  # Natal
    ],
)
def test_holidays_success(expected_date):
    """
    Testa se as datas de feriados estão presentes na lista de feriados.

    Parâmetros:
        expected_date (datetime.date): A data do feriado que esperamos que esteja
                                        presente na lista de feriados.

    Passos:
        1. Chama a função 'holidays()' para obter a lista de feriados.
        2. Verifica se a data esperada está presente na lista.
    """
    list_holidays = holidays()
    assert expected_date in list_holidays
