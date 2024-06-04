import esphome.config_validation as cv
from esphome.components import output
import esphome.codegen as cg
from esphome.const import (
    CONF_OUTPUT,
    CONF_ID,
)

map_float_ns = cg.esphome_ns.namespace("map_float")
MapFloat = map_float_ns.class_("MapFloat", output.FloatOutput)
CONF_MAP_FLOAT_MIN = "map_min"
CONF_MAP_FLOAT_MAX = "map_max"

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(MapFloat),
        cv.Optional(CONF_MAP_FLOAT_MIN, default=0): cv.float_,
        cv.Optional(CONF_MAP_FLOAT_MAX, default=0): cv.float_,
        cv.Required(CONF_OUTPUT): cv.use_id(output.FloatOutput),
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)

    output_ = await cg.get_variable(config[CONF_OUTPUT])
    cg.add(var.set_output(output_))

    min_ = await cg.get_variable(config[CONF_MAP_FLOAT_MIN])
    cg.add(var.set_min(min_))
    max_ = await cg.get_variable(config[CONF_MAP_FLOAT_MAX])
    cg.add(var.set_max(max_))
