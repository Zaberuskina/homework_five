from selene import have, be, command
from selene.support.shared import browser
from pathlib import Path


def test_submit_practice_form():
    browser.config.timeout = 10.0
    browser.config.window_width = 1200
    browser.config.window_height = 1000


    browser.open('/automation-practice-form')

    browser.element('#firstName').should(be.visible).type('John')
    browser.element('#lastName').should(be.visible).type('Doe')
    browser.element('#userEmail').should(be.visible).type('john.doe@example.com')
    browser.element('[for="gender-radio-1"]').should(be.clickable).click()
    browser.element('#userNumber').should(be.visible).type('1234567890')


    browser.element('#dateOfBirthInput').should(be.clickable).click()
    browser.element('.react-datepicker__month-select').type('May')
    browser.element('.react-datepicker__year-select').type('1990')
    browser.element('.react-datepicker__day--015').click()


    browser.element('#subjectsInput').should(be.visible).type('Maths').press_enter()


    browser.element('[for="hobbies-checkbox-1"]').perform(command.js.click)
    browser.element('[for="hobbies-checkbox-3"]').perform(command.js.click)

    if (Path(__file__).parent / 'test_image.jpg').exists():
        browser.element('#uploadPicture').set_value(
            str(Path(__file__).parent / 'test_image.jpg')
        )

    browser.element('#currentAddress').should(be.visible).type('123 Main St, Apt 1')

    state = browser.element('#state')
    browser.driver.execute_script("arguments[0].scrollIntoView(true);", state.locate())
    state.perform(command.js.click)
    browser.element('#react-select-3-option-0').click()

    city = browser.element('#city')
    browser.driver.execute_script("arguments[0].scrollIntoView(true);", city.locate())
    city.perform(command.js.click)
    browser.element('#react-select-4-option-0').click()

    submit = browser.element('#submit')
    browser.driver.execute_script("arguments[0].scrollIntoView(true);", submit.locate())
    submit.click()

    browser.element('#example-modal-sizes-title-lg').should(
        have.text('Thanks for submitting the form')
    )
    browser.all('tbody tr').should(have.exact_texts(
        'Student Name John Doe',
        'Student Email john.doe@example.com',
        'Gender Male',
        'Mobile 1234567890',
        'Date of Birth 15 May,1990',
        'Subjects Maths',
        'Hobbies Sports, Music',
        'Picture test_image.jpg' if (Path(__file__).parent / 'test_image.jpg').exists() else '',
        'Address 123 Main St, Apt 1',
        'State and City NCR Delhi'
    ))