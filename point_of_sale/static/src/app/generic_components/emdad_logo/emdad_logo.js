/** @emdad-module */

import { Component } from "@emdad/owl";

export class emdadLogo extends Component {
    static template = "point_of_sale.emdadLogo";
    static props = {
        class: { type: String, optional: true },
        style: { type: String, optional: true },
        monochrome: { type: Boolean, optional: true },
    };
    static defaultProps = {
        class: "",
        style: "",
        monochrome: false,
    };
}
