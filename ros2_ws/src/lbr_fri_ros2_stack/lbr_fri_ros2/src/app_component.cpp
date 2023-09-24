#include "app_component.hpp"

namespace lbr_fri_ros2 {
AppComponent::AppComponent(const rclcpp::NodeOptions &options) {
  app_node_ = std::make_shared<rclcpp::Node>("app", options);
  app_ = std::make_unique<lbr_fri_ros2::App>(app_node_);
}

rclcpp::node_interfaces::NodeBaseInterface::SharedPtr
AppComponent::get_node_base_interface() const {
  return app_node_->get_node_base_interface();
}
} // end of namespace lbr_fri_ros2

#include "rclcpp_components/register_node_macro.hpp"

RCLCPP_COMPONENTS_REGISTER_NODE(lbr_fri_ros2::AppComponent)
