import pytest

from string_utils import StringUtils

string_util = StringUtils()
# Test 1. capitilize


@pytest.mark.parametrize('string, result', [
    # позитивные проверки
    ("mariya", "Mariya"),
    ("Hello, Dear Friend", "Hello, dear friend"),
    ("suMmer", "Summer"),
    ("time-Out", "Time-out"),
    ("kitty123", "Kitty123"),
    ("tablE", "Table"),
    ("JOB", "Job"),
    ("THE SUN IS SHINING", "The sun is shining"),
    ("Timofey", "Timofey"),
    # Негативные проверки:
    ("", ""),
    (" friend", " friend"),
    ("123kitty", "123kitty"),
    ("! hi, dear friend", "! hi, dear friend"),
])
def test_capitalize(string, result):
    string_util = StringUtils()
    res = string_util.capitilize(string)
    assert res == result


# Test 2. trim
@pytest.mark.parametrize('string, result', [
    # позитивные проверки:
    (" cook", "cook"),
    (" tea ", "tea "),
    ("  Hello", "Hello"),
    ("  Welcome to our home", "Welcome to our home"),
    ("  12345", "12345"),
    # Негативные проверки:
    ("", ""),
    (" ", ""),
    ("friend", "friend"),
    ("The sun is shining  ", "The sun is shining  ")
])
def test_trim(string, result):
    string_util = StringUtils()
    res = string_util.trim(string)
    assert res == result
    print(result)


# Test 3: to_list
@pytest.mark.parametrize('string, divider, result', [
    # Позитивные проверки:
    ("first,second,third", ",", ["first", "second", "third"]),
    ("mouse!cat!dog", "!", ["mouse", "cat", "dog"]),
    ("blue;red;white", ";", ["blue", "red", "white"]),
    ("1,2,3,4,5", None, ["1", "2", "3", "4", "5"]),
    ("@^%^#^!^*", "^", ["@", "%", "#", "!", "*"]),
    ("1/n2/n3", "/n", ["1", "2", "3"]),
    # Негативные проверки:
    ("", None, []),
    ("1,2,3,4 5", None, ["1", "2", "3", "4 5"]),
    ("1 2 3 4 5", " ", ["1", "2", "3", "4", "5"]),
    ])
def test_to_list(string, divider, result):
    if divider is None:
        res = string_util.to_list(string)
    else:
        res = string_util.to_list(string, divider)
    assert res == result
    print(result)


# Test 4: contains
@pytest.mark.parametrize('string, symbol, result', [
    # Позитивные проверки:
    ("Mariya", "a", True),
    ("list", "t", True),
    ("Timofey  ", "T", True),
    ("Anna-Mariya", "-", True),
    ("12345", "3", True),
    ("HELLO", "L", True),
    ("", "", True),
    ("qwerty", "qw", True),
    ("  1234", " ", True),
    # Негативные проверки:
    ("Kitty", "k", False),
    ("pyton", "р", False),
    ("hello", "x", False),
    ("hello", "!", False),
    ("", "o", False),
    ("hello", "aij", False)
])
def test_contains(string, symbol, result):
    string_util = StringUtils()
    res = string_util.contains(string, symbol)
    assert res == result


# Test 5: delete_symbol
@pytest.mark.parametrize('string, symbol, result', [
    # позитивные проверки:
    ("park", "k", "par"),
    ("Street", "r", "Steet"),
    ("Never", "N", "ever"),
    ("98765", "7", "9865"),
    ("good", "o", "gd"),
    ("bluish-green", "-", "bluishgreen"),
    ("Thailand", "land", "Thai"),
    ("Sky Pro", " ", "SkyPro"),
    # негативные прверки:
    ("spoon", "k", "spoon"),
    (" ", " ", ""),
    ("", "", ""),
    ("", "g", ""),
    ("milk", "", "milk")
])
def test_delete_symbol(string, symbol, result):
    string_util = StringUtils()
    res = string_util.delete_symbol(string, symbol)
    assert res == result


# Test 6: starts_with
@pytest.mark.parametrize('string, symbol, result', [
    # позитивные прверки:
    ("table", "t", True),
    ("", "", True),
    ("Time", "T", True),
    (" car", " ", True),
    ("Film  ", "F", True),
    ("Anna-Maryia", "A", True),
    ("Maryia Timofeeva", "M", True),
    ("98765", "9", True),
    ("list", "", True),
    ("!@#$%^", "!", True),
    # негативные прверки:
    ("Woman", "w", False),
    ("tea", "T", False),
    ("", "s", False),
    ("Test", "e", False),
    (" twenty", "t", False)
])
def test_starts_with(string, symbol, result):
    string_util = StringUtils()
    res = string_util.starts_with(string, symbol)
    assert res == result


# Test 7:end_with
@pytest.mark.parametrize('string, symbol, result', [
    # позитивные проверки:
    ("month", "h", True),
    ("GIRL", "L", True),
    ("", "", True),
    ("man ", " ", True),
    ("987", "7", True),
    ("I'm very tired", "d", True),
    ("qwerty1", "1", True),
    ("test", "", True),
    # негативные проверки:
    ("morning", "G", False),
    ("evening", "n", False),
    ("door ", "r", False),
    ("", "s", False)
])
def test_end_with(string, symbol, result):
    string_util = StringUtils()
    res = string_util.end_with(string, symbol)
    assert res == result


# Test 8: is_empty
@pytest.mark.parametrize('string, result', [
    # позитивные примеры:
    ("", True),
    (" ", True),
    ("  ", True),
    # негативные примеры:
    ("tree", False),
    (" flower", False),
    ("123", False),
    ("cat ", False)
])
def test_is_empty(string, result):
    string_util = StringUtils()
    res = string_util.is_empty(string)
    assert res == result


# Test 9: list_to_string
@pytest.mark.parametrize('lst, joiner, result', [
    # позитивные примеры:
    (["q", "w", "e"], ",", "q,w,e"),
    ([9, 8, 7, 6, 5], None, "9, 8, 7, 6, 5"),
    (["a", "b", "c"], "", "abc"),
    (["son", "in", "law"], "-", "son-in-law"),
    # негативные примеры:
    ([" ", " ", " "], ",", " , , "),
    ([], None, ""),
    ([], "*", "")
])
def test_list_to_string(lst, joiner, result):
    string_util = StringUtils()
    if joiner is None:
        res = string_util.list_to_string(lst)
    else:
        res = string_util.list_to_string(lst, joiner)
    assert res == result
