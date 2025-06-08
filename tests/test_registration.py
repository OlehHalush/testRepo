from pages.business_page import BusinessPage
from pages.check_email_page import CheckEmailPage
from pages.thanks_for_confirming_email_page import ThanksForConfirmingEmailPage
from utils.faker_utils import FakerUtils


def test_free_account_registration(page, mail_client):
    email, password = mail_client.create_account()

    create_account_page, new_tab = BusinessPage(page) \
        .open_page() \
        .click_start_for_free()

    create_account_page \
        .verify_page_header("Create an account") \
        .verify_sign_up_button_is_enabled(False) \
        .enter_name(FakerUtils.fake_name()) \
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
        .verify_get_started_btn_is_visible()
