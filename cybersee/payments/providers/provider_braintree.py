import braintree
import logging

from braintree.exceptions import NotFoundError
from django.contrib import messages

from cybersee.payments.models import Subscription

logger = logging.getLogger(__name__)


def template_scripts():
    return '<script>var authorization = "{token}";</script>'.format(token=braintree.ClientToken.generate())


def handle_braintree_errors(result):
    for error in result.errors.deep_errors:
        logger.error('Attribute {} errored {} with message {}'.format(error.attribute, error.code, error.message))
    return False


def get_customer(user, payment_method_nonce=None):
    customer = {
        "id": str(user.id),
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email
    }
    try:
        result = braintree.Customer.update(str(user.id), customer)
    except NotFoundError:
        if payment_method_nonce:
            customer['payment-method-nonce'] = payment_method_nonce
        result = braintree.Customer.create(customer)

    logger.error(dir(result.customer.payment_methods))
    if result.is_success:
        return result.customer
    return handle_braintree_errors(result)


def request_payment_method(request, customer):
    if 'payment-method-nonce' in request.POST:
        result = braintree.PaymentMethod.create({
            "customer_id": request.user.id,
            "payment_method_nonce": request.POST['payment-method-nonce']
        })
        if result.is_success:
            return result.payment_method
        return handle_braintree_errors(result)

    if 'payment-method' in request.POST and request.POST['payment-method'] in customer.payment_methods:
        return customer.payment_methods[request.POST['payment-method']]

    if len(customer.payment_methods) > 0:
        for payment_method in customer.payment_methods:
            if payment_method.default:
                return payment_method
    return False


def subscribe(plan, request):
    customer = get_customer(request.user)
    if customer is False:
        messages.warning(request, 'Failed creating customer')
        return False

    payment = request_payment_method(request, customer)
    if payment is False:
        messages.warning(request, 'Unable to create payment method')
        return False

    result = braintree.Subscription.create({
        "payment_method_token": customer.payment_methods[0].token,
        "plan_id": plan.braintree_id
    })

    if result.is_success:
        logging.info('Created subscription {}. Transaction {}'.format(result.subscription.id, result.subscription.id))
        Subscription(braintree_id=result.subscription.id, user=request.user, active=True).save()
        messages.success(request, 'Subscription created')
        return True

    messages.warning(request, 'Failed processing subscription')
    for error in result.errors.deep_errors:
        logger.error('Attribute {} errored {} with message {}'.format(
            error.attribute, error.code, error.message), extra={'request': request})
    return False
