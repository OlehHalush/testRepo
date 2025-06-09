from pages.registration_pages.business_page import BusinessPage
from pages.registration_pages.check_email_page import CheckEmailPage
from pages.registration_pages.thanks_for_confirming_email_page import ThanksForConfirmingEmailPage
from utils.faker_utils import FakerUtils


def test_free_account_registration(page, mail_client):
    name = FakerUtils.fake_name()
    email, password = mail_client.create_account()

    create_account_page, new_tab = BusinessPage(page) \
        .open_page() \
        .click_start_for_free()

    create_account_page \
        .verify_page_header("Create an account") \
        .verify_sign_up_button_is_enabled(False) \
        .enter_name(name) \
        .enter_business_email(email) \
        .enter_password(password) \
        .verify_sign_up_button_is_enabled(True) \
        .click_sign_up()

    CheckEmailPage(new_tab) \
        .verify_title() \
        .verify_email(email)

    message = mail_client.wait_for_email(email, password, "Rebrandly email verification")
    activation_link = mail_client.get_link_from_email(email, password, message.id, "activate")

    CheckEmailPage(new_tab).open_url(activation_link)

    ThanksForConfirmingEmailPage(new_tab) \
        .verify_title() \
        .click_enter_dashboard_link() \
        .verify_title() \
        .verify_get_started_btn_is_visible() \
        .click_get_started() \
        .verify_title() \
        .click_skip_fow_now() \
        .verify_menu_is_selected("Links", True) \
        .click_account_button() \
        .verify_acc_name_from_acc_panel(name) \
        .verify_acc_email_from_acc_panel(email)


def test_user_can_login_and_logout(page):
    name = "Auto - Mendy 803836"
    email = "testuser-worker0-06ec5a@punkproof.com"
    password = "P@ssw0rd123"

    BusinessPage(page) \
        .open_page() \
        .click_login() \
        .verify_login_button_is_enabled(False) \
        .enter_email(email) \
        .enter_password(password) \
        .verify_login_button_is_enabled(True) \
        .click_login() \
        .verify_menu_is_selected("Links", True) \
        .click_account_button() \
        .verify_acc_name_from_acc_panel(name) \
        .verify_acc_email_from_acc_panel(email) \
        .select_option_from_account_panel("Sign out") \
        .verify_title() \
        .verify_login_to_your_account_button_is_enabled(True)
