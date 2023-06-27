def test_demo(get_config, app):

    login_page = app.login_page()
    login_page.navigate(get_config.get('base_url'))
    login_page.login_user(username="admin", password="123456")
    main_page = app.main_page()
    main_page.verify_the_brand_name("Django administration")