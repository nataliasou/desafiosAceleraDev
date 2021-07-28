import requests
from main import get_temperature


class MockResponse:
    def __init__(self, answer):
        self.answer = answer

    def json(self):
        return {
            'currently': {'temperature': self.answer}
        }


# Aqui faço um atalho do mock para não precisar repetir essa linhas de código
def atalho_mock(monkeypatch, temperature):
    def mock_get(*args, **kwargs):
        return MockResponse(temperature)
    monkeypatch.setattr(requests, 'get', mock_get)


# Testa a função get_temperature
def test_get_temperature_by_lat_lng(monkeypatch):
    lat = -14.235004
    lng = -51.92528
    temperature = 62
    expected = 16
    atalho_mock(monkeypatch, temperature)
    result = get_temperature(lat, lng)

    assert result == expected


# Testa o que acontece quando a temperatura é nula
def test_when_temperature_is_none(monkeypatch):
    lat = -14.235004
    lng = -51.92528
    temperature = ''
    answer_expected = None
    atalho_mock(monkeypatch, temperature)
    result = get_temperature(lat, lng)
    assert result == answer_expected


# Testa se a conversão está correta
def test_conversion_to_celsius(monkeypatch):
    lat = -14.235004
    lng = -51.92528
    temperature = 62
    conversion = int((temperature - 32) * 5.0 / 9.0)
    atalho_mock(monkeypatch, temperature)
    result = get_temperature(lat, lng)
    assert result == conversion
