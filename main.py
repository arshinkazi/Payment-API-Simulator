# save this as main.py
from fastapi import FastAPI, HTTPException
import random

app = FastAPI(title="Payment API Simulator")

# Dummy accounts (cardNumber: balance)
accounts = {
    "4111111111111111": 1000.0,
    "5555555555554444": 500.0
}

def luhn_check(card_number: str) -> bool:
    """Simple Luhn Algorithm check for card validity"""
    digits = [int(d) for d in card_number]
    checksum = 0
    parity = len(digits) % 2
    for i, digit in enumerate(digits):
        if i % 2 == parity:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
    return checksum % 10 == 0

@app.post("/pay")
def process_payment(cardNumber: str, amount: float, currency: str = "USD"):
    if not luhn_check(cardNumber):
        raise HTTPException(status_code=400, detail="Invalid card number")

    balance = accounts.get(cardNumber, 0)
    if balance >= amount:
        accounts[cardNumber] -= amount
        return {"status": "approved", "transactionId": f"TXN{random.randint(10000,99999)}"}
    else:
        return {"status": "declined", "reason": "Insufficient funds"}

@app.post("/refund")
def refund_payment(cardNumber: str, amount: float):
    if not luhn_check(cardNumber):
        raise HTTPException(status_code=400, detail="Invalid card number")
    accounts[cardNumber] = accounts.get(cardNumber, 0) + amount
    return {"status": "refunded", "newBalance": accounts[cardNumber]}
