from selenium import webdriver  
from selenium.webdriver.common.by import By


def testcase_1():
    driver = webdriver.Chrome()  

    driver.get("https://accounts.google.com/ServiceLogin/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Dpython%2Bcommand%2Bto%2Bwait%2Bfor%2Bselenium%26rlz%3D1C1GCEA_enIN998IN998%26oq%3Dpython%2Bcommand%2Bto%2Bwait%2Bfor%2Bselenium%26aqs%3Dchrome..69i57j33i160l3.28784j0j7%26sourceid%3Dchrome%26ie%3DUTF-8&ec=GAZAAQ&ifkv=AWnogHdwl1CmG2fUUadX888xCqQM5ixXz7lSrH-GSpoH2dwHMcmeCkHv4X4SXCFAKkxSuLGnlZ4PiA&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

    driver.add_cookie({"name" : "OTZ", "value" : "6834916_34_34__34_"})
    driver.add_cookie({"name" : "SMSV", "value" : "ADHTe-Dgu-js8rs6F2UCvF-LYzza6i4KXiOCR-2DEbLyrRVN1PxVBZCsM4RqfpXcqmbaA_X--hUW72yoJ9Dl1qwcEk3fuLLkOEtN12j5C_J-2cQgsPB6Q9E"})
    driver.add_cookie({"name" : "ACCOUNT_CHOOSER", "value" : "AFx_qI5rCGJi1_wpqRwXsf63CSuDdJvMoz5R4wvk5iGZt2N5908bHxuYlJMT5XDLl7pWXLu_IFwQ2PcTHdPhmHz7mCMveHjmTu9tAOizhDuCWzJ8Q1p6CMmn-seyEkgsewFG-aulciZzw4KleBKzvdRP_sS63D_wPKcjAiluQ_0ErVlBe7fGBD5DyZDQA0K68LxlFNLu6ZhGUxcxmZvZv0PIdr2zkzXMV0sVEou-pnKWsX2Lm8VQOc4g27SgAThJulqR0j79Uy9WeqrgmaBls61g2r5PaieueQrbkCjt3s8-cjYtBB47kOQWngogaFo6CSPyqAsEj_enzHtMzFLd2NvTf1WC93m-CGNcPKTtFZ1n37m7JUVGekk"})
    driver.add_cookie({"name" : "LSID", "value" : "o.mail.google.com|o.myaccount.google.com|s.IN|s.youtube:SwjC-WXSwGQgbc9rzuZpzkGfLP8bjEAfMxZYGdCzQn5op7D40rl-aNqRj8AUwDMvE8jZmQ."})
    driver.add_cookie({"name" : "__Host-1PLSID", "value" : "o.mail.google.com|o.myaccount.google.com|s.IN|s.youtube:SwjC-WXSwGQgbc9rzuZpzkGfLP8bjEAfMxZYGdCzQn5op7D4ttKDRuIkPnMt6TBfmXaVkg."})
    driver.add_cookie({"name" : "__Host-3PLSID", "value" : "o.mail.google.com|o.myaccount.google.com|s.IN|s.youtube:SwjC-WXSwGQgbc9rzuZpzkGfLP8bjEAfMxZYGdCzQn5op7D4uj70PwNyye6-asHRZuV_gQ."})
    driver.add_cookie({"name" : "__Host-GAPS", "value" : "1:H2WJTeB58gfJ1pz-1UywYjo42evbDdi59_phurd5mxnf94ozQPZS9CEERuOvUlUXNAAgiA1-UMrqMRpToTvc_N538JcytWyoqMy66QSwA_jL0-xao6HVjPrVajvVsXSuN3pRxoNwE_ti9g:Pj5JdXRtJI4xYync"})





    email_inp = driver.find_element(By.XPATH, '//*[@id="identifierId"]')


    email_inp = driver.find_element(By.ID, "id")

    email_inp.send_keys("prithwirajchakraborty5@gmail.com")

    signin_btn = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button')

    signin_btn.click()



    #signin_btn = driver.find_element(By.CLASS_NAME, "login-button")



    #pass_inp.send_keys("ViewBinder")

    #signin_btn.click()

    #ignore
    return true/false