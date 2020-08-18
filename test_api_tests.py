import pytest
import requests
import men_json


# test if we have the post
def test_post():
    this_post = requests.post('http://127.0.0.1:5000/second-post')
    assert this_post.status_code == 200


# test if the json format is know
def test_trim():
    this_str = men_json.remove_unwanted("  XX ")
    assert this_str == "XX"


# test First + Last NAME to  UPPERCASE
def test_upper():
    this_str = men_json.to_upper("meN ", " ziN ")
    assert this_str == "MEN ZIN"


# test lower or upper from 40
def test_lower_40():
    l = men_json.LorU(39)
    u = men_json.LorU(41)
    e = men_json.LorU(40)
    assert l+e+u == "lower=upper"

def test_json_string():
    this_json= {"first_name" : "menashe", "last_name": " zinger", "the_answer":"#42"}
    this_str = men_json.return_string(this_json)
    assert this_str=="Hello MENASHE ZINGER, \n The answer is 42 upper then 40"



