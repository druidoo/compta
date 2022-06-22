/** @odoo-module **/

import KanbanController from 'web.KanbanController';
import KanbanRenderer from 'web.KanbanRenderer';
import KanbanView from 'web.KanbanView';
import KanbanColumn from 'web.KanbanColumn';
import KanbanRecord from 'web.KanbanRecord';
import KanbanModel from 'web.KanbanModel';
import viewRegistry from 'web.view_registry';
import { ProjectControlPanel } from '@project/js/project_control_panel';
import viewUtils from 'web.viewUtils';

// PROJECTS

const ProjectProjectKanbanRecordMeritis = KanbanRecord.extend({
    /**
     * @override
     * @private
     */
    _openRecord: function () {
        //const kanbanBoxesElement = this.el.querySelectorAll('.o_project_kanban_boxes a');
        const kanbanBoxesElement = this.el.querySelectorAll(".o_kanban_card_manage_settings a.dropdown-item");
        if (this.selectionMode !== true && kanbanBoxesElement.length) {
            kanbanBoxesElement[1].click();
        } else {
            this._super.apply(this, arguments);
        }
    },
    /**
     * @override
     * @private
     */
    _onManageTogglerClicked: function (event) {
        this._super.apply(this, arguments);
        const thisSettingToggle = this.el.querySelector('.o_kanban_manage_toggle_button');
        this.el.parentNode.querySelectorAll('.o_kanban_manage_toggle_button.show').forEach(el => {
            if (el !== thisSettingToggle) {
                el.classList.remove('show');
            }
        });
        thisSettingToggle.classList.toggle('show');
    },
});

const ProjectProjectKanbanRendererMeritis = KanbanRenderer.extend({
    config: _.extend({}, KanbanRenderer.prototype.config, {
        KanbanRecord: ProjectProjectKanbanRecordMeritis,
    }),
});

const ProjectProjectKanbanViewMeritis = KanbanView.extend({
    config: Object.assign({}, KanbanView.prototype.config, {
        Renderer: ProjectProjectKanbanRendererMeritis,
    })
});

viewRegistry.add('project_project_kanban_meritis', ProjectProjectKanbanViewMeritis);