class Locators():

    #Dodanie_okularów_do_koszyka
    add_glasses_css_selector = "div:nth-child(1)>div:nth-child(1)>div>div>div>input"
    glasses_click_xpath = "//button[@data-product-name='Okulary']"

    #Dodanie_piłki_do_koszyka
    add_ball_css_selector = "div:nth-child(1)>div:nth-child(2)>div>div>div>input"
    ball_click_xpath = "//button[@data-product-price='39.22']"

    #Dodanie_zeszytu_do_koszyka
    execute_script = "window.scrollTo(0, document.body.scrollHeight);"
    add_notebook_css_selector = "div:nth-child(3)>div:nth-child(3)>div>div>div>input"
    notebook_click_xpath = "//button[@data-product-name='Zeszyt']"