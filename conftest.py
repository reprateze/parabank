import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()


@pytest.fixture
def request_context():
    with sync_playwright() as p:
        context = p.request.new_context(
            base_url=os.getenv("BASE_URL"),
            extra_http_headers={"Accept": "application/json"},
        )

        yield context

        context.dispose()

@pytest.fixture
def account_id():
    return int(os.getenv("ACCOUNT_ID"))

@pytest.fixture
def customer_id():
    return int(os.getenv("CUSTOMER_ID"))