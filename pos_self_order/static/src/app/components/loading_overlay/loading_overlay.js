/** @emdad-module */

import { Component, onMounted, useState } from "@emdad/owl";

export class LoadingOverlay extends Component {
    static template = "pos_self_order.LoadingOverlay";

    setup() {
        this.state = useState({
            loading: false,
        });

        onMounted(() => {
            setTimeout(() => {
                this.state.loading = true;
            }, 200);
        });
    }
}
