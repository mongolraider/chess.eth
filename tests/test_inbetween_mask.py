import pytest
from brownie import Chess, accounts, web3, reverts

@pytest.fixture
def chess_contract():
    return accounts[0].deploy(Chess)

@pytest.mark.parametrize("from_pos,to_pos,expected_mask", 
    [
        # 1- Square movements should return 0
        # No move
        ("0x1b", "0x1b", "0x0000000000000000000000000000000000000000000000000000000000000000"),
        # 1 Up
        ("0x1b", "0x23", "0x0000000000000000000000000000000000000000000000000000000000000000"),
        # 1 Down
        ("0x1b", "0x13", "0x0000000000000000000000000000000000000000000000000000000000000000"),
        # 1 Right
        ("0x1b", "0x1c", "0x0000000000000000000000000000000000000000000000000000000000000000"),
        # 1 Left
        ("0x1b", "0x1a", "0x0000000000000000000000000000000000000000000000000000000000000000"),
        # 1 Right 1 Up
        ("0x1b", "0x24", "0x0000000000000000000000000000000000000000000000000000000000000000"),
        # 1 Left 1 Up
        ("0x1b", "0x22", "0x0000000000000000000000000000000000000000000000000000000000000000"),
        # 1 Left 1 Down
        ("0x1b", "0x12", "0x0000000000000000000000000000000000000000000000000000000000000000"),
        # 1 Right 1 Down
        ("0x1b", "0x14", "0x0000000000000000000000000000000000000000000000000000000000000000"),

        # 2 Up
        ("0x1b", "0x2b", "0x0000000000000000000000000000F00000000000000000000000000000000000"),
        # 2 Down
        ("0x1b", "0x0b", "0x00000000000000000000000000000000000000000000F0000000000000000000"),
        # 2 Right
        ("0x1b", "0x1d", "0x00000000000000000000000000000000000F0000000000000000000000000000"),
        # 2 Left
        ("0x1b", "0x19", "0x0000000000000000000000000000000000000F00000000000000000000000000"),
        # 2 Right 2 Up
        ("0x1b", "0x2d", "0x000000000000000000000000000F000000000000000000000000000000000000"),
        # 2 Left 2 Up
        ("0x1b", "0x29", "0x00000000000000000000000000000F0000000000000000000000000000000000"),
        # 2 Left 2 Down
        ("0x1b", "0x09", "0x000000000000000000000000000000000000000000000F000000000000000000"),
        # 2 Right 2 Down
        ("0x1b", "0x0d", "0x0000000000000000000000000000000000000000000F00000000000000000000"),

        # All Up
        ("0x07", "0x3f", "0x00000000F0000000F0000000F0000000F0000000F0000000F000000000000000"),
        # All Down
        ("0x3f", "0x07", "0x00000000F0000000F0000000F0000000F0000000F0000000F000000000000000"),
        # All Up 2
        ("0x00", "0x38", "0x000000000000000F0000000F0000000F0000000F0000000F0000000F00000000"),
        # All Down 2
        ("0x38", "0x00", "0x000000000000000F0000000F0000000F0000000F0000000F0000000F00000000"),

        # All Right
        ("0x00", "0x07", "0x000000000000000000000000000000000000000000000000000000000FFFFFF0"),
        # All Left
        ("0x07", "0x00", "0x000000000000000000000000000000000000000000000000000000000FFFFFF0"),
        # All Right 2
        ("0x38", "0x3f", "0x0FFFFFF000000000000000000000000000000000000000000000000000000000"),
        # All Left 2
        ("0x3f", "0x38", "0x0FFFFFF000000000000000000000000000000000000000000000000000000000"),

        # All Right all Up
        ("0x00", "0x3f", "0x000000000F00000000F00000000F00000000F00000000F00000000F000000000"),
        # All Left all Down
        ("0x3f", "0x00", "0x000000000F00000000F00000000F00000000F00000000F00000000F000000000"),
        # All Right all Down
        ("0x38", "0x07", "0x00000000000000F000000F000000F000000F000000F000000F00000000000000"),
        # All Left all Up
        ("0x07", "0x38", "0x00000000000000F000000F000000F000000F000000F000000F00000000000000"),

    
    ])
def test_commit_move(chess_contract, from_pos, to_pos, expected_mask):
    assert chess_contract.getInBetweenMask(from_pos, to_pos) == expected_mask
