
from django import forms


class EmailForm(forms.Form):
    email = forms.EmailField()


def form_test():
    input = "123@456.com"

    email_form = EmailForm(input)

    if email_form.is_valid():
        print("valid")
    else:
        print("not valid")


if __name__ == "__main__":
    form_test()
