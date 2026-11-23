from locators.faq_locators import FaqPageLocators


FAQ_DATA = [
    (
        FaqPageLocators.QUESTION_COST,
        FaqPageLocators.ANSWER_COST,
        "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
        "cost"
    ),
    (
        FaqPageLocators.QUESTION_MULTIPLE_ORDERS,
        FaqPageLocators.ANSWER_MULTIPLE_ORDERS,
        "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
        "multiple_orders"
    ),
    (
        FaqPageLocators.QUESTION_RENTAL_TIME,
        FaqPageLocators.ANSWER_RENTAL_TIME,
        "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
        "rental_time"
    ),
    (
        FaqPageLocators.QUESTION_ORDER_TODAY,
        FaqPageLocators.ANSWER_ORDER_TODAY,
        "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
        "order_today"
    ),
    (
        FaqPageLocators.QUESTION_ORDER_EXTENSION,
        FaqPageLocators.ANSWER_ORDER_EXTENSION,
        "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
        "order_extension"
    ),
    (
        FaqPageLocators.QUESTION_CHARGER,
        FaqPageLocators.ANSWER_CHARGER,
        "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
        "charger"
    ),
    (
        FaqPageLocators.QUESTION_ORDER_CANCELLATION,
        FaqPageLocators.ANSWER_ORDER_CANCELLATION,
        "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
        "order_cancellation"
    ),
    (
        FaqPageLocators.QUESTION_DELIVERY_OUTSIDE_MKAD,
        FaqPageLocators.ANSWER_DELIVERY_OUTSIDE_MKAD,
        "Да, обязательно. Всем самокатов! И Москве, и Московской области.",
        "delivery_outside_mkad"
    )
]