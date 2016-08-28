/* Copyright 2016 LasLabs Inc.
 * License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl). */

odoo.define("web_app_drawer.Tour", function (require) {
    "use strict";

    var Core = require("web.core");
    var Tour = require("web.Tour");
    var _t = Core._t;

    Tour.register({
        id: "test_web_app_drawer",
        name: _t("Demonstrate functionality of App Drawer"),
        path: "/web",
        mode: "tutorial",
        steps: [
            {
                title: _t('Demonstrate App Drawer open'),
                element: ".app-drawer-toggle:first",
                content: _t("Click here or press ActionKey+A to open App Drawer"),
                waitFor: "body.drawer-open",
            },
            {
                title: _t('Demonstrate App Drawer navigate'),
                element: ".oe_menu_toggler:first",
                content: _t("Use the mouse or arrow keys to navigate Apps."),
                waitNot: ".oe_menu_toggler:first:focus",
            },
            {
                title: _t('Demonstrate App Drawer select'),
                element: ".oe_menu_toggler:focus",
                content: _t('Click or press Enter to select an App'),
            }
        ]
    });

});
