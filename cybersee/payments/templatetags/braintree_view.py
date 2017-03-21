from django import template
import braintree
register = template.Library()


@register.filter(is_safe=True)
def card_icon(payment_method):
    if isinstance(payment_method, braintree.CreditCard):
        card_icons = {
            payment_method.CardType.Visa: 'fa-cc-visa',
            payment_method.CardType.MasterCard: 'fa-cc-mastercard',
            payment_method.CardType.AmEx: 'fa-cc-amex',
            payment_method.CardType.Discover: 'fa-cc-discover',
            payment_method.CardType.DinersClubInternational: 'fa-cc-diners-club',
            payment_method.CardType.JCB: 'fa-cc-jcb',
        }
        return card_icons.get(payment_method.card_type, 'fa-credit-card-alt')

    if isinstance(payment_method, braintree.PayPalAccount):
        return 'fa-paypal'

    return 'fa-credit-card-alt'
