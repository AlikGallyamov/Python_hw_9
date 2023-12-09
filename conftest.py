from allure_commons.types import Severity
from selenium import webdriver
import allure
import pytest
from selene import browser, be, by

rep = "AlikGallyamov/Python_hw_9"
git_url = "https://github.com/"
number_issue = 2


@pytest.fixture
def config_browser():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)

    browser.config.driver = driver
    browser.config.window_height = 960
    browser.config.window_width = 1600

    yield

    browser.quit()


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open(git_url)


@allure.step(f"Ищем репозиторий {rep}")
def find_rep():
    browser.element('[class="search-input"]').click()
    browser.element('#query-builder-test').should(be.blank).type(rep).submit()
    browser.element(by.link_text(rep)).click()


@allure.step(f"Ищем вкладку issue")
def find_issue_blocks():
    browser.element('#issues-tab').click()


@allure.step(f"Ищем issue под номером {number_issue}")
def find_issue():
    browser.element(by.partial_text(f'#{number_issue}')).should(be.visible)


class Annotation:
    tag: str
    severity: str
    owner: str
    feature: str
    story: str
    link: str
    name_link: str

    def __init__(self, tag, severity, owner, feature, story, link, name_link):
        self.tag = tag
        self.severity = severity
        self.owner = owner
        self.feature = feature
        self.story = story
        self.link = link
        self.name_link = name_link

    def attach_annotations(self):
        allure.dynamic.tag(self.tag)
        allure.dynamic.label("owner", self.owner)
        allure.dynamic.feature(self.feature)
        allure.dynamic.story(self.story)
        allure.dynamic.link(self.link, name=self.name_link)

        if self.severity == "BLOCKER":
            allure.dynamic.severity(Severity.BLOCKER)
        if self.severity == "CRITICAL":
            allure.dynamic.severity(Severity.CRITICAL)
        if self.severity == "NORMAL":
            allure.dynamic.severity(Severity.NORMAL)
        if self.severity == "MINOR":
            allure.dynamic.severity(Severity.MINOR)
        if self.severity == "TRIVIAL":
            allure.dynamic.severity(Severity.TRIVIAL)
