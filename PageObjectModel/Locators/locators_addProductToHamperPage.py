class Locators():

    # Scrolltop strony
    execute_script = "window.scrollTo(0, document.body.scrollHeight);"

    #Dodanie_okularów_do_koszyka
    add_glasses_css_selector = "div:nth-child(1)>div:nth-child(1)>div>div>div>input"
    glasses_click_xpath = "//button[@data-product-name='Okulary']"

    #Dodanie_piłki_do_koszyka
    add_ball_css_selector = "div:nth-child(1)>div:nth-child(2)>div>div>div>input"
    ball_click_xpath = "//button[@data-product-price='39.22']"

    #Dodanie_zeszytu_do_koszyka
    add_notebook_css_selector = "div:nth-child(3)>div:nth-child(3)>div>div>div>input"
    notebook_click_xpath = "//button[@data-product-name='Zeszyt']"

    #Dodanie_kostka_do_koszyka
    add_ankle_xpath = "html/body/div[1]/div/div[2]/div[1]/form/div[3]/div[4]/div/div/div/input"
    ankle_click_xpath = "//button[@data-product-name='Kostka']"

    #Dodanie_kamera_do_koszyka
    add_camera_xpath = "html/body/div[1]/div/div[2]/div[1]/form/div[2]/div[2]/div/div/div/input"
    camera_click_xpath = "//button[@data-product-name='Kamera']"

    #Dodanie_sluchawki_do_koszyka
    add_headphones_xpath = "html/body/div[1]/div/div[2]/div[1]/form/div[2]/div[1]/div/div/div/input"
    headphones_click_xpath = "//button[@data-product-name='Słuchawki']"

    #Dodanie_kabel_do_koszyka
    add_cable_xpath = "html/body/div[1]/div/div[2]/div[1]/form/div[1]/div[4]/div/div/div/input"
    cable_click_xpath = "//button[@data-product-name='Kabel']"

    #Dodanie_aparat_do_koszyka
    add_theCamera_xpath = "html/body/div[1]/div/div[2]/div[1]/form/div[2]/div[3]/div/div/div/input"
    theCamera_click_xpath = "//button[@data-product-name='Aparat']"

    #Łączna_ilość_produktów
    theTotalNumberOf_products_text = "div.col-md-12.basket-summary>p:nth-child(1)>span"

    #Do_zapłaty
    toPay_text = "div.col-md-12.basket-summary>p:nth-child(2)>span"