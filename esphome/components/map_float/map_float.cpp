#include "map_float.h"
#include "esphome/core/log.h"

namespace esphome {
namespace map_float {
static const char *const TAG = "map_float";
void MapFloat::dump_config() {
  ESP_LOGCONFIG(TAG, "map float:");
  LOG_FLOAT_OUTPUT(this);
}
void MapFloat::write_state(float state) {
  float mapped_state = state * (this->max_power_ - this->min_power_) + this->min_power_;
  if (this->zero_means_zero_ && state < 0.001) {
    mapped_state == 0;
  }
  this->output_->set_state(mapped_state);
  ESP_LOGD(TAG, "mapped state: %d", state);
}

}  // namespace map_float
}  // namespace esphome
