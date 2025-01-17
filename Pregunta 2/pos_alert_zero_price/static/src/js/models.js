odoo.define('pos_alert_zero_price.models', function (require) {
    "use strict";

    const models = require('point_of_sale.models');
    const PosComponent = require('point_of_sale.PosComponent');
    const { Gui } = require('point_of_sale.Gui');

    models.Orderline = models.Orderline.extend({
        initialize: function (attr, options) {
            this._super(attr, options);

            // Check if the product price is 0.0
            if (this.product && this.product.lst_price === 0) {
                Gui.showPopup('ConfirmPopup', {
                    title: 'Precio Cero Detectado',
                    body: `El producto "${this.product.display_name}" tiene un precio de S/ 0.0.`,
                });
            }
        },
    });
});
