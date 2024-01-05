/* @emdad-module */

import { Component } from "@emdad/owl";

export class SnailmailNotificationPopover extends Component {
    static template = "snailmail.SnailmailNotificationPopover";
    static props = ["message", "close?"];
}
