var form = document.querySelector('#payment-form');
var paypalButton = document.querySelector('#paypal-button');
var submit = document.querySelector('#submit-card');

braintree.client.create({
    authorization: authorization
}, function (clientErr, clientInstance) {
    if (clientErr) {
        console.warn(clientErr);
        return;
    }
    braintree.hostedFields.create({
        client: clientInstance,
        styles: {
            'input': {
                'color': '#555'
            },
            'input.invalid': {
                'color': 'red'
            },
            'input.valid': {
                'color': 'green'
            }
        },
        fields: {
            number: {
                selector: '#card-number',
                placeholder: 'Valid Card Number'
            },
            cvv: {
                selector: '#security-code',
                placeholder: 'CVV'
            },
            expirationDate: {
                selector: '#expiration-date',
                placeholder: 'MM / YY'
            },
            postalCode: {
                selector: '#post-code',
                placeholder: 'Post Code'
            }
        }
    }, function (hostedFieldsErr, hostedFieldsInstance) {
        if (hostedFieldsErr) {
            console.warn(hostedFieldsErr);
            return;
        }

        submit.removeAttribute('disabled');

        form.addEventListener('submit', function (event) {
            event.preventDefault();

            if (!form.checkValidity()) {
                return;
            }

            hostedFieldsInstance.tokenize(function (tokenizeErr, payload) {
                if (tokenizeErr) {
                    console.error(tokenizeErr);
                    return;
                }

                $('#payment-method-nonce').val(payload.nonce);
                form.submit();
            });
        }, false);
    });

    braintree.paypal.create({
        client: clientInstance
    }, function (paypalErr, paypalInstance) {
        if (paypalErr) {
            console.error('Error creating PayPal:', paypalErr);
            return;
        }
        paypalButton.removeAttribute('disabled');
        paypalButton.addEventListener('click', function (event) {

            if (!form.checkValidity()) {
                return;
            }

            paypalInstance.tokenize({
                flow: 'vault'
            }, function (tokenizeErr, payload) {

                if (tokenizeErr) {
                    if (tokenizeErr.type !== 'CUSTOMER') {
                        console.error('Error tokenizing:', tokenizeErr);
                    }
                    return;
                }
                paypalButton.setAttribute('disabled', true);

                $('#payment-method-nonce').val(payload.nonce);
                form.submit();
            });

        }, false);
    });
});
