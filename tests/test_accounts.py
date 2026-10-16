import os

def test_get_account(request_context,account_id, customer_id):
    response = request_context.get(f"accounts/{account_id}")

    assert response.status == 200

    body = response.json()

    assert body["id"] == account_id
    assert body["customerId"] == customer_id

def test_get_transactions(request_context, account_id):
    response = request_context.get(f"accounts/{account_id}/transactions")

    assert response.status == 200

    body = response.json()
    print(body)

def test_deposit(request_context, account_id):
    response = request_context.post(
        "deposit",
        params={"accountId": account_id, "amount": 15}
    )
    print(response.status)
    print(response.text())


