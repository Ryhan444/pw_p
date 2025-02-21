/** @odoo-module */
import { patch } from "@web/core/utils/patch";
import { NumberPopup } from "@point_of_sale/app/utils/input_popups/number_popup";
import { TicketScreen } from "@point_of_sale/app/screens/ticket_screen/ticket_screen";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";
import { _t } from "@web/core/l10n/translation";

patch(TicketScreen.prototype, {
 async onDoRefund() {
    const userPin = this.env.services.pos.config.refund_security;
    if (userPin){
        this.dialog.add(NumberPopup, {
            startingValue: 0,
            title: _t('Enter PIN'),
            formatDisplayedValue: (input) => input.replace(/./g, "•"),
            getPayload: (payload) => {
                console.log(payload);
                if (payload) {
                    console.log(userPin);
                    if (payload != userPin) {
                        console.log(userPin);
                        this.dialog.add(AlertDialog, {
                            title: _t("Incorrect PIN"),
                            body: _t("Please enter the correct PIN."),
                        });
                    } else {
                        this.dialog.closeAll();
                        return super.onDoRefund(...arguments);
                    }
                }
            },
        });
    }else{
        return super.onDoRefund(...arguments);
    }

    },
})
