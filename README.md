# Stripe Webhook Handler

A Python-based webhook handler for automating payment processing with Stripe.

## What it does

- Listens for Stripe payment events
- Handles checkout.session.completed event
- Extracts customer email and payment amount
- Ready to trigger course access, email notifications, or CRM updates

## Tech Stack

- Python 3
- Flask
- Stripe API

## Use Case

This handler was built to automate post-payment workflows — for example, granting course access after a successful payment via Stripe.

## Setup

1. Clone the repository
2. Install dependencies:
   pip install flask stripe
3. Set environment variables:
   STRIPE_SECRET_KEY=your_secret_key
   STRIPE_WEBHOOK_SECRET=your_webhook_secret
4. Run the server:
   python webhook_handler.py

## Author

Freelance integration specialist — available on Upwork
