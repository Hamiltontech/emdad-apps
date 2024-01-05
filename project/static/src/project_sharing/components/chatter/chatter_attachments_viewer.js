/** @emdad-module */

import { Component } from "@emdad/owl";

export class ChatterAttachmentsViewer extends Component {}

ChatterAttachmentsViewer.template = 'project.ChatterAttachmentsViewer';
ChatterAttachmentsViewer.props = {
    attachments: Array,
    canDelete: { type: Boolean, optional: true },
    delete: { type: Function, optional: true },
};
ChatterAttachmentsViewer.defaultProps = {
    delete: async () => {},
};
