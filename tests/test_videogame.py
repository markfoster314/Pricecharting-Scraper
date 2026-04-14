import pytest
from videogame import VideoGame


def test_videogame_stores_values():
    game = VideoGame("Super Mario Bros", "nes", "5.99", "12.99", "N/A")
    assert game.getTitle() == "Super Mario Bros"
    assert game.getConsole() == "nes"
    assert game.getLoosePrice() == "5.99"
    assert game.getCompletePrice() == "12.99"
    assert game.getNewPrice() == "N/A"


def test_videogame_repr():
    game = VideoGame("Zelda", "nes", "10.00", "20.00", "30.00")
    output = repr(game)
    assert "Zelda" in output
    assert "nes" in output


def test_videogame_na_prices():
    game = VideoGame("Rare Game", "nintendo-64", "N/A", "N/A", "N/A")
    assert game.getLoosePrice() == "N/A"
    assert game.getCompletePrice() == "N/A"
    assert game.getNewPrice() == "N/A"
