/** @emdad-module */

import { Component } from "@emdad/owl";

export class ChatterMessageCounter extends Component { }

ChatterMessageCounter.props = {
    count: Number,
};
ChatterMessageCounter.template = 'project.ChatterMessageCounter';
