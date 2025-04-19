# 📅 feriados-anbima
Biblioteca para facilitar a listagem de feriados bancários da ANBIMA, com fácil integração com bibliotecas como `bizdays` e `business_calendar`.

## 📦 Instalação
```bash
pip install -r requirements.txt
```

## 🔧 Como usar
### Usando bizdays
```python 
from bizdays import Calendar
from src.core import holidays
cal = Calendar(holidays=holidays(), weekends=['Saturday', 'Sunday'])
```

### Usando business_calendar
```python
from datetime import date
from src.core import holidays
from business_calendar import Calendar

cal = Calendar(holidays=holidays())
isbusday = cal.isbusday(date(2025, 4, 21))
isholiday = cal.isholiday(date(2025, 4, 21))
```

## 📁 Estrutura do Projeto

``` bash
feriados-anbima/
├── README.md             # Documentação principal
├── requirements.txt      # Dependências do projeto
├── setup.py              # Script de instalação do pacote
│
└── src/
    ├── anbima.py          # Funções para listar os feriados
    │
    ├── feriados/
    │   └── feriados_anbima.xls  # Arquivo com os feriados da ANBIMA
    │
    └── tests/
        └── test_holidays.py     # Testes usando Pytest
```

## ✅ Testes
Use o Pytest para rodar os testes:
```bash
pytest .
```
