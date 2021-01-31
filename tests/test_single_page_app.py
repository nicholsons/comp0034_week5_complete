from time import sleep
from dash.testing.application_runners import import_app
from selenium.webdriver.support.select import Select


# The function name follows this pattern: test_{tcid}_{test title}.
# The tcid (test case ID) is an abbreviation pattern of aaaddd => app name abbreviation + three digits.


def test_spa001_h1textequals(dash_duo):
    app = import_app("single_page_app.app")
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=4)
    h1_text = dash_duo.find_element("h1").text
    sleep(3)
    assert h1_text.casefold() == 'Waste and recycling'.casefold()


def test_spa002_areadropdowncontainslondon(dash_duo):
    app = import_app("single_page_app.app")
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=4)
    sleep(3)
    assert 'London' in dash_duo.find_element("#area_select").text, "'London' should appear in the area dropdown"


def test_spa002_areadropdownchangesstats(dash_duo):
    """
    Write your own test here to assert that when the area dropdown is changed to Hackney that the card title for the
    stats panel is also changed to Hackney.

    You will need to use the select_dcc_dropdown function to select an option in the dropdown which has the following
    syntax:
        select_dcc_dropdown(elem_or_selector, value=None, index=None)
    """
    app = import_app("single_page_app.app")
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=4)
    sleep(3)
    dash_duo.select_dcc_dropdown("#area_select", value='Hackney')
    sleep(3)
    assert 'Hackney' in dash_duo.find_element("#card_name").text, "'Hackney' should appear in as the card name"
