from selene import have, be
from selene.support.shared import browser


def test_submit_practice_form():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('John')
    browser.element('#lastName').type('Doe')
    browser.element('#userEmail').type('john.doe@example.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('1234567890')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('May')
    browser.element('.react-datepicker__year-select').type('1990')
    browser.element('.react-datepicker__day--015').click()

    browser.element('#subjectsInput').type('Maths').press_enter()

    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()

    browser.element('#currentAddress').type('123 Main St, Apt 1')

    browser.element('#state').click()
    browser.element('#react-select-3-option-0').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()

    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(
        have.text('Thanks for submitting the form')
    )
