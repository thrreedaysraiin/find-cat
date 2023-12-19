import pytest
from find_cats import Board, Game, Card


@pytest.fixture
def board():
    return Board()


@pytest.fixture
def game():
    return Game()


def test_board_has_10_cards(board):
    assert len(board.cards) == 10


def test_get_card(board):
    card = board.get_card(0)  #проверка на принадлежность к классу
    assert isinstance(card, Card)


def test_get_random_card(board):
    card = board.get_random_card() #проверка на принадлежность к классу
    assert isinstance(card, Card)


def test_game_initial_state(game):
    assert game.score == 0
    assert game.round == 1
    assert game.max_score == 5
    assert game.is_playing is True


def test_roll_dice(game, board):
    card = game.roll_dice()
    assert isinstance(card, tuple)
    assert len(card) == 3
    color, action, pattern = card
    assert color in board.colors
    assert action in board.actions
    assert pattern in board.patterns