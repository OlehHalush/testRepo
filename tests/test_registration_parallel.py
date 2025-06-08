from pages.business_page import BusinessPage
from pages.check_email_page import CheckEmailPage
from pages.thanks_for_confirming_email_page import ThanksForConfirmingEmailPage
from utils.faker_utils import FakerUtils


def test_free_account_registration_form1(page):

    create_account_page, new_tab = BusinessPage(page) \
        .open_page() \
        .click_start_for_free()

    create_account_page \
        .verify_page_header("Create an account") \
        .verify_sign_up_button_is_enabled(False) \
        .enter_name(FakerUtils.fake_name()) \
        .enter_business_email(FakerUtils.fake_email()) \
        .enter_password("P@ssw0rd") \
        .verify_sign_up_button_is_enabled(True)


def test_free_account_registration_form2(page):

    create_account_page, new_tab = BusinessPage(page) \
        .open_page() \
        .click_start_for_free()

    create_account_page \
        .verify_page_header("Create an account") \
        .verify_sign_up_button_is_enabled(False) \
        .enter_name(FakerUtils.fake_name()) \
        .enter_business_email(FakerUtils.fake_email()) \
        .enter_password("P@ssw0rd") \
        .verify_sign_up_button_is_enabled(True)


def test_free_account_registration_for3(page):

    create_account_page, new_tab = BusinessPage(page) \
        .open_page() \
        .click_start_for_free()

    create_account_page \
        .verify_page_header("Create an account") \
        .verify_sign_up_button_is_enabled(False) \
        .enter_name(FakerUtils.fake_name()) \
        .enter_business_email(FakerUtils.fake_email()) \
        .enter_password("P@ssw0rd") \
        .verify_sign_up_button_is_enabled(True)


def test_free_account_registration_form4(page):

    create_account_page, new_tab = BusinessPage(page) \
        .open_page() \
        .click_start_for_free()

    create_account_page \
        .verify_page_header("Create an account") \
        .verify_sign_up_button_is_enabled(False) \
        .enter_name(FakerUtils.fake_name()) \
        .enter_business_email(FakerUtils.fake_email()) \
        .enter_password("P@ssw0rd") \
        .verify_sign_up_button_is_enabled(True)


def test_free_account_registration_form5(page):

    create_account_page, new_tab = BusinessPage(page) \
        .open_page() \
        .click_start_for_free()

    create_account_page \
        .verify_page_header("Create an account") \
        .verify_sign_up_button_is_enabled(False) \
        .enter_name(FakerUtils.fake_name()) \
        .enter_business_email(FakerUtils.fake_email()) \
        .enter_password("P@ssw0rd") \
        .verify_sign_up_button_is_enabled(True)
