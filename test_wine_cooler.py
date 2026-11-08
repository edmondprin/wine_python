from wine_cooler import verify_numbers, calculate_max_discount_packs, format_message, main
import pytest

def test_verify_numbers_valid():
    result = verify_numbers('24', '12', '6')
    expected = [24, 12, 6]
    assert result == expected

def test_verify_numbers_inventory_exceeds_capacity():
    with pytest.raises(ValueError):
        verify_numbers('24', '26', '6')

def test_verify_numbers_negative_inventory():
    with pytest.raises(ValueError):
        verify_numbers('24', '-2', '6')

def test_verify_numbers_invalid_capacity():
    with pytest.raises(ValueError):
        verify_numbers('0', '24', '6')

def test_verify_numbers_invalid_pack():
    with pytest.raises(ValueError):
        verify_numbers('24', '10', '0')

def test_verify_numbers_invalid_text():
    with pytest.raises(ValueError):
        verify_numbers("24", "abc", "5")

def test_verify_numbers_negative_pack_size():
    with pytest.raises(ValueError):
        verify_numbers("24", "20", "-4")

def test_calculate_max_pack_empty_cooler():
    result = calculate_max_discount_packs(24, 0, 6)
    expected = 4
    assert result == expected

def test_calculate_max_pack_full_cooler():
    result = calculate_max_discount_packs(54, 54, 6)
    expected = 0
    assert result == expected

def test_calculate_max_pack_exactly_enough_room():
    result = calculate_max_discount_packs(54, 42, 6)
    expected = 2
    assert result == expected

def test_calculate_max_pack_insufficient_room():
    result = calculate_max_discount_packs(54, 50, 6)
    expected = 0
    assert result == expected

def test_calculate_max_pack_partial_pack_remaining():
    result = calculate_max_discount_packs(54, 47, 6)
    expected = 1
    assert result == expected

def test_format_message_zero():
    result = format_message(0, 6)
    # assert result.startswith("Not enough room")
    assert result == "Not enough room at the moment to get a full pack of 6 bottles!"

def test_format_message_positive_singular_short():
    result = format_message(1, 6)
    assert "full packs" not in result
    assert "1 full pack" in result

def test_format_message_positive_plural_short():
    result = format_message(2, 6)
    assert "full packs" in result

def test_format_message_positive_plural_long():
    result = format_message(4, 6)
    expected = "You can now buy 4 full packs to get closer to filling your wine cooler!"
    assert result == expected

def test_main_str(monkeypatch, capsys):
    responses = iter(["hello", "0", "6", "54", "0", "6"])
    monkeypatch.setattr("builtins.input", lambda _:next(responses))
    main()
    captured = capsys.readouterr()
    assert "invalid literal for int()" in captured.out
    assert "Incorrect input" in captured.out
    assert "9 full packs" in captured.out

def test_main_three_loops(monkeypatch, capsys):
    responses = iter(["54", "-1", "6", "0", "30", "6", "24", "20", "6"])
    monkeypatch.setattr("builtins.input", lambda _:next(responses))
    main()
    captured = capsys.readouterr()
    assert "Inventory cannot be below 0" in captured.out
    assert "Number needs to be positive" in captured.out
    assert "Not enough room at the moment to get a full pack of 6 bottles!" in captured.out
    assert captured.out.count("Incorrect input:") == 2


