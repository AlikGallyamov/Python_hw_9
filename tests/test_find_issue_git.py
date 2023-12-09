import allure
import pytest
from selene import browser, be, by
from conftest import git_url, rep, number_issue
import conftest


def test_only_with_selene(config_browser):
    annotations = conftest.Annotation(tag="web", severity="TRIVIAL", owner="AlikGallyamov",
                                      feature="Задачи в репозитории",
                                      story="Не авторизованный пользователь не может создать задачу", link=git_url,
                                      name_link="Test")
    annotations.attach_annotations()
    browser.open(git_url)
    browser.element('[class="search-input"]').click()
    browser.element('#query-builder-test').should(be.blank).type(rep).submit()
    browser.element(by.link_text(rep)).click()
    browser.element('#issues-tab').click()
    browser.element(by.partial_text(f'#{number_issue}')).should(be.visible)


def test_issue_with_step(config_browser):
    annotations = conftest.Annotation(tag="web", severity="CRITICAL", owner="IvanIvanov",
                                      feature="Задачи в репозитории",
                                      story="Не авторизованный пользователь не может создать задачу", link=git_url,
                                      name_link="Test")
    annotations.attach_annotations()

    with allure.step("Открываем главную страницу"):
        browser.open(git_url)
    with allure.step("Клик на поле поиска репозитория"):
        browser.element('[class="search-input"]').click()
    with allure.step("Вводим текст в развернувшееся поле поиска"):
        browser.element('#query-builder-test').should(be.blank).type(rep).submit()
    with allure.step(f"Ищем репозиторий {rep} и кликаем на него"):
        browser.element(by.link_text(rep)).click()
    with allure.step("Ищем вкладку Issue"):
        browser.element('#issues-tab').click()
    with allure.step("Ищем issue под номером 1"):
        browser.element(by.partial_text(f'#{number_issue}')).should(be.visible)


def test_issue_with_steps(config_browser):
    annotations = conftest.Annotation(tag="web", severity="BLOCKER", owner="AlikGallyamov",
                                      feature="Задачи в репозитории",
                                      story="Авторизованный пользователь не может создать задачу", link=git_url,
                                      name_link="Test")
    annotations.attach_annotations()
    conftest.open_main_page()
    conftest.find_rep()
    conftest.find_issue_blocks()
    conftest.find_issue()
