import flask
import stripe
import os

app = flask.Flask(_name_)

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
webhook_secret = os.environ.get('STRIPE_WEBHOOK_SECRET')


@app.route('/webhook', methods=['POST'])
def handle_webhook():
    payload = flask.request.data
    sig_header = flask.request.headers.get('Stripe-Signature')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, webhook_secret
        )
    except ValueError:
        return {'error': 'Invalid payload'}, 400
    except stripe.error.SignatureVerificationError:
        return {'error': 'Invalid signature'}, 400

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        customer_email = session.get('customer_details', {}).get('email')
        amount = session.get('amount_total', 0) / 100
        print(f'Payment received: {amount} from {customer_email}')
        # Here you can trigger course access, send email, etc.

    return {'status': 'success'}, 200


if _name_ == '_main_':
    app.run(port=5000)
