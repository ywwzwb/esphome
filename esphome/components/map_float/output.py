import esphome.config_validation as cv
from esphome.components import output
import esphome.codegen as cg
from esphome.const import (
    CONF_OUTPUT,
    CONF_ID,
)

map_float_ns = cg.esphome_ns.namespace("map_float")
MapFloat = map_float_ns.class_("MapFloat", output.FloatOutput)

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(MapFloat),
        cv.Required(CONF_OUTPUT): cv.use_id(output.FloatOutput),
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)

    output_ = await cg.get_variable(config[CONF_OUTPUT])
    cg.add(var.set_output(output_))
