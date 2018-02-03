    // Copyright (c) 2018, Ahmed Ragheb and contributors
    // For license information, please see license.txt

    frappe.ui.form.on('Booking details', {
        refresh: function(frm) {

        }
    });

    frappe.ui.form.on('Booking details', {
        airport: function(frm) {
            cur_frm.set_query("terminal", function() {
                return {
                    "filters": {
                        "parent": cur_frm.doc.airport
                    }
                };
            });
        },
        air_ways: function(frm) {

            cur_frm.set_query("flight_number", function() {
                return {
                    "filters": {
                        "parent": cur_frm.doc.air_ways
                    }
                };
            });

        }
    });