odoo.define('pos_boleta_button.BoletaButton', function (require) {
    "use strict";

    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const Registries = require('point_of_sale.Registries');

    const BoletaButtonPaymentScreen = (PaymentScreen) =>
        class extends PaymentScreen {
            get boletaTotal() {
                return this.currentOrder ? this.currentOrder.get_total_with_tax() : 0;
            }

            onClickBoleta() {
                // Mostrar el popup con el monto total.
                this.showPopup('ConfirmPopup', {
                    title: 'Monto Total',
                    body: `El monto total a pagar es: S/ ${this.boletaTotal.toFixed(2)}`,
                });
            }
            get hasBoletaButton() {
                return true;
            }
        };

    Registries.Component.extend(PaymentScreen, BoletaButtonPaymentScreen);

    return BoletaButtonPaymentScreen;
});
