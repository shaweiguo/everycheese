import pytest

from ..models import Cheese
from .factories import CheeseFactory


pytestmark = pytest.mark.django_db


def test___str__():
    # cheese = Cheese.objects.create(
    #     name='Stracchino',
    #     description='Semi-sweet cheese that goes well with starches.',
    #     firmness=Cheese.Firmness.SOFT,
    # )
    # cheese = CheeseFactory(name='Stracchino')
    # assert cheese.__str__() == 'Stracchino'
    # assert str(cheese) == 'Stracchino'
    cheese = CheeseFactory()
    assert cheese.__str__() == cheese.name
    assert str(cheese) == cheese.name
