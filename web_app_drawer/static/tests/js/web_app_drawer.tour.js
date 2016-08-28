/* Copyright 2016 LasLabs Inc.
 * License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl). */

odoo.define("web_app_drawer.TestTour", function (require) {
    "use strict";

    var Core = require("web.core");
    var Tour = require("web.Tour");
    var _t = Core._t;

    Tour.register({
        id: "test_web_app_drawer",
        name: _t("Test functionality of the App Drawer"),
        path: "/web",
        mode: "test",
        steps: [
            {
                title: _t("Click to open App Drawer"),
                element: ".app-drawer-toggle",
                wait: 1000,
                //waitFor: "body.drawer-open",
            },
            //{
            //    title: _t('Click settings'),
            //    element: 'a[data-menu-name="Settings"]',
            //    waitFor: 'div.o_web_settings_dashboard_header',
            //},
            //{
            //    title: _t("Click to open App Drawer"),
            //    element: ".app-drawer-toggle",
            //    waitFor: "body.drawer-open",
            //},
        ]
    });

});
