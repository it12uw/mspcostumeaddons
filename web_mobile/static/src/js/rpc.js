flectra.define('web_mobile.rpc', function () {
"use strict";

var available = typeof OdooDeviceUtility !== 'undefined';
var DeviceUtility;
var deferreds = {};
var methods = {};

if (available){
    DeviceUtility = OdooDeviceUtility;
    delete window.OdooDeviceUtility;
}

/**
 * Responsible for invoking native methods which called from JavaScript
 *
 * @param {String} name name of action want to perform in mobile
 * @param {Object} args extra arguments for mobile
 *
 * @returns Deferred Object
 */
function native_invoke(name, args) {
    if(_.isUndefined(args)){
        args = {};
    }
    var def = $.Deferred();
    var id = _.uniqueId();
    deferreds[id] = {
        successCallback: function (success) {
            def.resolve(success);
        },
        errorCallback: function (error) {
            def.reject(error);
        }
    };
    args = JSON.stringify(args);
    DeviceUtility.execute(name, args, id);
    return def;
}

/**
 * Manages deferred callback from initiate from native mobile
 *
 * @param {String} id callback id
 * @param {Object} result
 */
window.flectra.native_notify = function (id, result) {
    if (deferreds.hasOwnProperty(id)) {
        if (result.success) {
            deferreds[id].successCallback(result);
        } else {
            deferreds[id].errorCallback(result);
        }
    }
};

var plugins = available ? JSON.parse(DeviceUtility.list_plugins()) : [];
_.each(plugins, function (plugin) {
    methods[plugin.name] = function (args) {
        return native_invoke(plugin.action, args);
    };
});

return {'methods': methods};

});
