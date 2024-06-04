#pragma once

#include <set>

#include "esphome/components/output/float_output.h"

namespace esphome {
namespace map_float {

class MapFloat : public Component, output::FloatOutput {
 public:
  MapFloat() {}
  void dump_config() override;
  void set_output(output::FloatOutput *output) { this->output_ = output; }

 protected:
  void write_state(float state) override;
  output::FloatOutput *output_ = nullptr;
};

}  // namespace map_float
}  // namespace esphome
