from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import datetime
import pytest
import sys
import argparse
#sys.path.append('../')


class Test_Currency_Converter_Tab():
    def setup_class(cls):
        print('Loading a oanda website')
        cls.currency_converter_website = 'https://www.oanda.com/currency/converter/'
        ### Please add the executable path for chrome
        cls.driver = webdriver.Chrome(executable_path='/Users/divya/Downloads/chromedriver')


    @classmethod
    def teardown_class(cls):
        print('sleep for 10 seconds before closing the browser')
        time.sleep(10)
        cls.driver.quit()


    def setting_value_by_element_id(self,id,value):
        element = self.driver.find_element_by_id(id)
        element.send_keys(value)
        element.send_keys(Keys.RETURN)

    def setting_value_by_element_id_after_clearing_def_value(self,id,value):
        element = self.driver.find_element_by_id(id)
        element.clear()
        element.send_keys(value)
        element.send_keys(Keys.RETURN)

    def getting_attribute_element_id(self,id,value):
        element = self.driver.find_element_by_id(id).get_attribute(value)
        return element

    def today_date_in_utc_short_form(self):
        t = datetime.datetime.utcnow().date()
        t = t.strftime("%B %d, %Y")
        p = t.split(' ')
        p[0] = p[0][:3]
        return ' '.join(p)

    def clicking_by_link(self,value):
        self.driver.find_element_by_link_text(value).click()

    def setting_value_by_xpath(self,path,value):
        element = self.driver.find_element_by_xpath(path)
        element.send_keys(value)
        element.send_keys(Keys.RETURN)

    def clicking_by_xpath(self,value):
        self.driver.find_element_by_xpath(value).click()

    def clicking_by_text(self,value):
        self.driver.find_element_by_link_text(value).click()

#    @pytest.mark.skip
    def test_currency_converter_tab_tc1(self):
        # Section 2.7- Currency Converter Tab
        # Testcase8 from testplan
        # Description - Currency I have as INR, Currency I want as USD, Amount as 80
        # InterBank rate as 1%
        # End Date - 28th Oct 2017
        # positive test

        cur_input = 'INR'
        cur_output = 'USD'
        expected_output = 1.21529

        self.driver.get(self.currency_converter_website)
        print('setting quote currency input as INR')
        self.setting_value_by_element_id('quote_currency_input',cur_input)

        print('setting base currency input as USD')
        self.setting_value_by_element_id('base_currency_input', cur_output)

        print('setting interbank rates input as 1%')
        self.setting_value_by_element_id('interbank_rates_input', 1)

        print('enter Date as 28th Oct 2017')
        self.setting_value_by_element_id_after_clearing_def_value('end_date_input','10/28/2017')

        print('enter the quote amount input as 80')
        self.setting_value_by_element_id_after_clearing_def_value('quote_amount_input', 80)

        time.sleep(5)
        print('get base amount output for USD')
        actual_output = self.getting_attribute_element_id('base_amount_input','value')

        time.sleep(5)
        print('actual output is {}'.format(actual_output))
        print('expected ouput is {}'.format(expected_output))
        assert (actual_output == str(expected_output)), ("acutal value {0} not equal to expected output {1:.5f}".format(actual_output,expected_output))

#    @pytest.mark.skip
    def test_currency_converter_tab_tc2(self):
        # Section 2.7- Currency Converter Tab
        # Testcase8 from testplan
        # Description - Currency I have as USD, Currency I want as EUR, Amount as -2
        # InterBank rate as 1%
        # End Date - 28th Oct 2016
        # check if the acutal output is calculated as input is always the absolute value
        # negative test

        cur_input = 'USD'
        cur_output = 'EUR'
        expected_output = 1.81508

        self.driver.get(self.currency_converter_website)
        print('setting quote currency input as USD')
        self.setting_value_by_element_id('quote_currency_input', cur_input)

        print('setting base currency input as EUR')
        self.setting_value_by_element_id('base_currency_input', cur_output)

        print('setting interbank rates input as 1%')
        self.setting_value_by_element_id('interbank_rates_input', 1)

        print('enter Date as 28th Oct 2016')
        self.setting_value_by_element_id_after_clearing_def_value('end_date_input','10/28/2016')

        print('enter the quote amount input as -2')
        self.setting_value_by_element_id_after_clearing_def_value('quote_amount_input', -2)

        time.sleep(5)
        print('get base amount output for EUR currency')
        actual_output = self.getting_attribute_element_id('base_amount_input', 'value')
        time.sleep(5)
        print('actual output is {}'.format(actual_output))
        print('expected ouput is {}'.format(expected_output))
        assert (actual_output != 0.00000),('actual output should not be 0.00000')
        assert (actual_output == str(expected_output)), ("acutal value {0} not equal to expected output {1:.5f}".format(actual_output,expected_output))

#    @pytest.mark.skip
    def test_currency_converter_tab_tc3(self):
        # Section 2.7- Currency Converter Tab
        # Testcase8 from testplan
        # Description - Currency I have as USD, Currency I want as INR, Amount as "strposfkwe"
        # InterBank rate as 5%
        # End Date - 28th Oct 2017
        # Expected output is -
        # negative test

        cur_input = 'USD'
        cur_output = 'INR'
        expected_output = '-'

        self.driver.get(self.currency_converter_website)
        print('setting quote currency input as USD')
        self.setting_value_by_element_id('quote_currency_input', cur_input)

        print('setting base currency input as INR')
        self.setting_value_by_element_id('base_currency_input', cur_output)

        print('setting interbank rates input as 5%')
        self.setting_value_by_element_id('interbank_rates_input', 5)

        print('enter Date as 28th Oct 2017')
        self.setting_value_by_element_id_after_clearing_def_value('end_date_input', '10/28/2017')

        print('enter the quote amount input as "strposfkwe"')
        self.setting_value_by_element_id_after_clearing_def_value('quote_amount_input', 'strposfkwe')
        time.sleep(5)
        print('get base amount output for USD')
        actual_output = self.getting_attribute_element_id('base_amount_input', 'value')
        time.sleep(5)
        print('actual output is {}'.format(actual_output))
        print('expected ouput is {}'.format(expected_output))
        assert (actual_output == expected_output), ("acutal value {0} not equal to expected output {1}".format(actual_output,expected_output))

#    @pytest.mark.skip
    def test_currency_converter_tab_tc4(self):
        # Section 2.7- Currency Converter Tab
        # Testcase8 from testplan
        # Description - Currency I have as USD, Currency I want as INR, Amount as special charecters
        # InterBank rate as 1%
        # End Date - 28th Oct 2017
        # Expected output is -
        # negative test

        cur_input = 'USD'
        cur_output = 'INR'
        expected_output = '-'

        self.driver.get(self.currency_converter_website)
        print('setting quote currency input as USD')
        self.setting_value_by_element_id('quote_currency_input', cur_input)

        print('setting base currency input as INR')
        self.setting_value_by_element_id('base_currency_input', cur_output)

        print('setting interbank rates input as 1%')
        self.setting_value_by_element_id('interbank_rates_input', 1)

        print('enter Date as 28th Oct 2017')
        self.setting_value_by_element_id_after_clearing_def_value('end_date_input', '10/28/2017')

        print('enter the quote amount input as #$#$#')
        self.setting_value_by_element_id_after_clearing_def_value('quote_amount_input', '#$#$#')
        time.sleep(5)
        print('get base amount output for USD')
        actual_output = self.getting_attribute_element_id('base_amount_input', 'value')
        time.sleep(5)
        print('actual output is {}'.format(actual_output))
        print('expected ouput is {}'.format(expected_output))
        assert (actual_output == expected_output), ("acutal value {0} not equal to expected output {1}".format(actual_output,expected_output))

#    @pytest.mark.skip
    def test_currency_converter_tab_tc5(self):
        # Section 2.7- Currency Converter Tab
        # Testcase8 from testplan
        # Description - Currency I have as EUR, Currency I want as JYP, Amount for JYP as 500
        # InterBank rate as 1%
        # End Date - 28th Oct 2017
        # negative test

        cur_input = 'EUR'
        cur_output = 'JPY'
        expected_output = 3.81548

        self.driver.get(self.currency_converter_website)
        print('setting quote currency input as EUR')
        self.setting_value_by_element_id('quote_currency_input', cur_input)

        print('setting base currency input as JPY')
        self.setting_value_by_element_id('base_currency_input', cur_output)

        print('setting interbank rates input as 1%')
        self.setting_value_by_element_id('interbank_rates_input', 1)

        print('enter Date as 28th Oct 2017')
        self.setting_value_by_element_id_after_clearing_def_value('end_date_input', '10/28/2017')

        print('enter the quote amount input as 500')
        self.setting_value_by_element_id_after_clearing_def_value('base_amount_input', 500)

        time.sleep(5)
        print('get base amount output for USD')
        actual_output = self.getting_attribute_element_id('quote_amount_input', 'value')
        time.sleep(5)
        print('actual output is {}'.format(actual_output))
        print('expected ouput is {}'.format(expected_output))
        assert (actual_output == str(expected_output)), ("acutal value {0} not equal to expected output {1:.5f}".format(actual_output,expected_output))

#    @pytest.mark.skip
    def test_currency_converter_tab_click1(self):
        # Section 2.7- Currency Converter Tab
        # Testcase5 from testplan
        # Description- When user clicks the triangles in between 'currency I want' and 'currency I have' search boxes
        # InterBank rate as 1%
        # End Date - 28th Oct 2017
        # positive test

        cur_input = 'INR'
        cur_output = 'USD'
        expected_output = '5,150.74'

        self.driver.get(self.currency_converter_website)
        print('setting quote currency input as INR')
        self.setting_value_by_element_id('quote_currency_input', cur_input)

        print('setting base currency input as USD')
        self.setting_value_by_element_id('base_currency_input', cur_output)

        print('setting interbank rates input as 1%')
        self.setting_value_by_element_id('interbank_rates_input', 1)

        print('enter Date as 28th Oct 2017')
        self.setting_value_by_element_id_after_clearing_def_value('end_date_input', '10/28/2017')

        print('enter the quote amount input as 80')
        self.setting_value_by_element_id_after_clearing_def_value('quote_amount_input', 80)

        self.clicking_by_xpath('//*[(@id = "flipper")]')
        time.sleep(5)
        print('get base amount output for USD')
        actual_output = self.getting_attribute_element_id('base_amount_input', 'value')

        print('check if curreny I have amount box has 80')
        qb = self.getting_attribute_element_id('quote_amount_input', 'value')
        assert (qb == str(80)), ("acutal value {0} not equal to expected output 80".format(qb))
        time.sleep(5)
        print('actual output is {}'.format(actual_output))
        print('expected ouput is {}'.format(expected_output))
        assert (actual_output == expected_output), ("acutal value {0} not equal to expected output {1}".format(actual_output,expected_output))

#    @pytest.mark.skip
    def test_currency_converter_tab_tc6(self):
        # Section 2.7- Currency Converter Tab
        #TC6: User empties an amount box in currency i have or currency i want
        #Expected Output: Adjacent amount box should show 0.00000

        cur_input = 'USD'
        cur_output = 'EUR'
        expected_output = '0.00000'

        self.driver.get(self.currency_converter_website)
        print('setting quote currency input as USD')
        self.setting_value_by_element_id('quote_currency_input', cur_input)

        print('setting base currency input as EUR')
        self.setting_value_by_element_id('base_currency_input', cur_output)

        print('setting interbank rates input as 1%')
        self.setting_value_by_element_id('interbank_rates_input', 1)

        print('enter Date as 28th Oct 2017')
        self.setting_value_by_element_id_after_clearing_def_value('end_date_input', '10/28/2017')

        print('enter the quote amount input as blank')
        self.setting_value_by_element_id_after_clearing_def_value('quote_amount_input', ' ')

        time.sleep(5)
        print('get base amount output for EUR currency')
        actual_output = self.getting_attribute_element_id('base_amount_input', 'value')
        time.sleep(5)
        print('actual output is {}'.format(actual_output))
        print('expected ouput is {}'.format(expected_output))
        assert (actual_output == expected_output), ("acutal value {0} not equal to expected output {1}".format(actual_output,expected_output))

        print('enter the base amount input as blank')
        self.setting_value_by_element_id_after_clearing_def_value('base_amount_input', ' ')

        time.sleep(5)
        print('get base amount output for EUR currency')
        actual_output = self.getting_attribute_element_id('quote_amount_input', 'value')
        time.sleep(5)
        print('actual output is {}'.format(actual_output))
        print('expected ouput is {}'.format(expected_output))
        assert (actual_output == str(expected_output)), ("acutal value {0} not equal to expected output {1}".format(actual_output, expected_output))

#    @pytest.mark.skip
    def test_currency_converter_tab_click2(self):
        # Section 2.7- Currency Converter Tab
        #TC9:User clicks on 'Try our Money Transfer service'
        #Expected Output: page should be directed to expected url and also check for the title of the webpage

        expected_title = 'International Money Transfer | Send Money Abroad | OANDA'

        self.driver.get(self.currency_converter_website)
        print('get current url page')
        old_url = self.driver.current_url
        print('click on - Try our Money Transfer service')
        self.clicking_by_link('Try our Money Transfer service')
        current_url = self.driver.current_url
        assert (self.driver.title == expected_title),("driver.title {0} is not same as expected title {1}".format(driver.title,expected_title))
        assert (current_url != old_url),("page didnt get redirected to another page")


#    @pytest.mark.skip
    def test_currency_converter_tab_click3(self):
        # Section 2.7- Currency Converter Tab
        #TC11: User clicks on the date/ calendar icon
        #Expected Output:
        # 1. Calendar should drop down
        # 2. User should not be able to go beyond todays date

        expected_output = self.today_date_in_utc_short_form()

        self.driver.get(self.currency_converter_website)
        print('enter Date as 30th Dec 2017')
        self.setting_value_by_element_id_after_clearing_def_value('end_date_input', '12/30/2017')

        actual_output = self.getting_attribute_element_id('end_date_input', 'value')

        assert (actual_output == expected_output), (
        "acutal value {0} not equal to expected output {1}".format(actual_output, expected_output))

#    @pytest.mark.skip
    def test_currency_converter_help(self):
        # Section 2.7- Currency Converter Tab
        #TC16: User clicks on Help (?) icon
        #Expected Output: This should direct the user to currency converter help page.

        expected_title = 'Currency Converter Help | OANDA'

        self.driver.get(self.currency_converter_website)
        print('get current url page')
        old_url = self.driver.current_url
        print('click on - Help')
        self.clicking_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "help_label", " " ))]')
        current_url = self.driver.current_url
        assert (self.driver.title == expected_title),("driver.title {0} is not same as expected title {1}".format(driver.title,expected_title))
        assert (current_url != old_url),("page didnt get redirected to another page")

#    @pytest.mark.skip
    def test_search_box(self):
        '''
        Section 2.3.1 Search field
        TC1: Able to search for given string like 'API'
        Expected output: links for string found or links for string not found should appear in search result window
        :return:
        '''

        expected_title = 'Search | OANDA'

        self.driver.get(self.currency_converter_website)
        print('get current url page')
        old_url = self.driver.current_url
        print('click on - Search box')
        self.setting_value_by_xpath('//input', 'API')
        current_url = self.driver.current_url
        assert (self.driver.title == expected_title),("driver.title {0} is not same as expected title {1}".format(driver.title,expected_title))
        assert (current_url != old_url),("page didnt get redirected to another page")

#    @pytest.mark.skip
    def test_language_change_to_german(self):
        '''
        Section 2.3.2 Language change
        TC1:  User chooses a language 'German' in the drop down menu
        Expected output:
        1.	The drop down menu should exclude the selected language.
        2.	Also the page should get translated to selected language.

        :return:
        '''
        expected_url = 'https://www.oanda.com/lang/de/currency/converter/'

        self.driver.get(self.currency_converter_website)
        print('get current url page')
        old_url = self.driver.current_url
        print('click on - language')
        self.clicking_by_xpath('//*[(@id = "m-lang")]')
        time.sleep(2)
        print('click on - DE - German')
        self.clicking_by_text('DE')
        current_url = self.driver.current_url
        assert (current_url != old_url),("page didnt get redirected to another page")
        assert (current_url == expected_url), ("page not directed to correct url")
        print('click on - language EN')
        self.clicking_by_xpath('//*[(@id = "m-lang")]')
        time.sleep(2)
        self.clicking_by_text('EN')

#    @pytest.mark.skip
    def test_click_on_sign_in_click_on_fxtrade(self):
        '''
        Section 2.3.4 Sign-in
        TC3: User clicks on the 'FX-Trade'
        Expected Output: User should be redirected to the correct login page and correct web title.
        :return:
        '''
        expected_title = 'Secure Sign In | OANDA'

        self.driver.get(self.currency_converter_website)
        print('get current url page')
        old_url = self.driver.current_url
        print('click on Sign-in')
        self.clicking_by_text('SIGN IN')
        time.sleep(2)
        print('click on FXTRADE')
        self.clicking_by_text('FXTRADE')
        current_url = self.driver.current_url
        assert (self.driver.title == expected_title),("driver.title {0} is not same as expected title {1}".format(driver.title,expected_title))
        assert (current_url != old_url),("page didnt get redirected to another page")

    def test_click_on_open_account_click_on_live_trading_account(self):
        '''
        Section 2.3.5 Open an account
        TC3: User clicks on the 'live trading account'
        Expected Output: User should be redirected to the correct login page and correct web title.

        :return:
        '''
        expected_url = 'https://www.oanda.com/register/#/sign-up'

        self.driver.get(self.currency_converter_website)
        print('get current url page')
        old_url = self.driver.current_url
        print('click on Open an account')
        self.clicking_by_text('OPEN AN ACCOUNT')
        time.sleep(2)
        print('click on LIVE TRADING ACCOUNT')
        self.clicking_by_text('LIVE TRADING ACCOUNT')
        current_url = self.driver.current_url
        assert (current_url != old_url),("page didnt get redirected to another page")
        assert (current_url == expected_url), ("page not directed to correct url")