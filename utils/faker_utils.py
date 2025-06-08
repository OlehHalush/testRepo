from mimesis import Person, Datetime, Internet


class FakerUtils:

    @staticmethod
    def fake_name():
        return f"Auto - {Person().name()} {Datetime().time().microsecond}"

    @staticmethod
    def fake_last_name():
        return f"Auto - {Person().last_name()} {Datetime().time().microsecond}"

    @staticmethod
    def fake_web_address():
        return Internet().hostname()

    @staticmethod
    def fake_email():
        return Person().email()
