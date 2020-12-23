from typing import List


class EmailValidator:
    def __init__(self, min_length: int, mails: list, domains: List):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __validate_name(self, name):
        return len(name) >= self.min_length

    def __validate_mail(self, mail):
        return mail in self.mails

    def __validate_domain(self, domain):
        return domain in self.domains

    def validate(self, email):
        name = email.split('@')[0]
        help_mail = email.split('@')[1]
        mail = help_mail.split('.')[0]
        domain = help_mail.split('.')[1]
        if not self.__validate_name(name):
            return False
        elif not self.__validate_mail(mail):
            return False
        elif not self.__validate_domain(domain):
            return False
        return True







mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
