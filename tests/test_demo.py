def test_demo(app):
    app.login_page().open_page()
    app.login_page().login_user(user_role='regular_user')
    main_page = app.main_page()
    main_page.should_have_the_navigate_name("Home")