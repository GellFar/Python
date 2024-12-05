import pytest
from stringUtils import StringUtils

testwr = StringUtils()


def test_capitilize():
    # Позитивные тесты
    assert testwr.capitilize("skypro") == "Skypro"
    assert testwr.capitilize("hello world") == "Hello world"
    assert testwr.capitilize("123abc") == "123abc"

    # Негативные тесты
    assert testwr.capitilize("") == ""
    assert testwr.capitilize("   ") == "   "


def test_trim():
    # Позитивные тесты
    assert testwr.trim("   skypro") == "skypro"
    assert testwr.trim("skypro   ") == "skypro   "
    assert testwr.trim("   skypro   ") == "skypro   "

    # Негативные тесты
    assert testwr.trim("") == ""
    assert testwr.trim("   ") == ""


def test_to_list():
    # Позитивные тесты
    assert testwr.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert testwr.to_list("1:2:3", ":") == ["1", "2", "3"]
    assert testwr.to_list("") == []

    # Негативные тесты
    assert testwr.to_list("a b c", " ") == ["a", "b", "c"]
    assert testwr.to_list("a,b,c,,d", ",") == ["a", "b", "c", "", "d"]


def test_contains():
    # Позитивные тесты
    assert testwr.contains("SkyPro", "S") is True
    assert testwr.contains("SkyPro", "k") is True

    # Негативные тесты
    assert testwr.contains("SkyPro", "U") is False
    assert testwr.contains("", "a") is False


def test_delete_symbol():
    # Позитивные тесты
    assert testwr.delete_symbol("SkyPro", "k") == "SyPro"
    assert testwr.delete_symbol("SkyPro", "Pro") == "Sky"

    # Негативные тесты
    assert testwr.delete_symbol("SkyPro", "x") == "SkyPro"
    assert testwr.delete_symbol("", "a") == ""


def test_starts_with():
    # Позитивные тесты
    assert testwr.starts_with("SkyPro", "S") is True
    assert testwr.starts_with("SkyPro", "Sk") is True

    # Негативные тесты
    assert testwr.starts_with("SkyPro", "P") is False
    assert testwr.starts_with("", "S") is False


def test_end_with():
    # Позитивные тесты
    assert testwr.end_with("SkyPro", "o") is True
    assert testwr.end_with("SkyPro", "Pro") is True

    # Негативные тесты
    assert testwr.end_with("SkyPro", "y") is False
    assert testwr.end_with("", "o") is False


def test_is_empty():
    # Позитивные тесты
    assert testwr.is_empty("") is True
    assert testwr.is_empty(" ") is True
    assert testwr.is_empty("\t") is True

    # Негативные тесты
    assert testwr.is_empty("SkyPro") is False
    assert testwr.is_empty(" a ") is False


def test_list_to_string():
    # Позитивные тесты
    assert testwr.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert testwr.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    assert testwr.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"

    # Негативные тесты
    assert testwr.list_to_string([]) == ""
    assert testwr.list_to_string([None]) == "None"
