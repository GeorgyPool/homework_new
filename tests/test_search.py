from src.search import process_bank_operations, process_bank_search


def test_process_bank_search_is_positive(search_dict):
    assert process_bank_search(search_dict, "ok") == [{"description": "its_ok"}]


def test_process_bank_search_is_no_search(search_dict):
    assert process_bank_search(search_dict, "hello") == []


def test_process_bank_search_is_not_description(search_not_description):
    assert process_bank_search(search_not_description, "its_ok") == []


def test_process_bank_operations_is_positive(
    search_dict,
):
    assert process_bank_operations(search_dict, ["its_ok"]) == {"its_ok": 1}


def test_process_bank_operations_is_not_description(search_not_description):
    assert process_bank_operations(search_not_description, ["its_ok"]) == {}
