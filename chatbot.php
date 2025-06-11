<?php
/*
Plugin Name: Chatbot
Description: AI chatbot widget for your WordPress site.
Version: 1.0
Author: Tony
*/

function chatbot_widget_embed() {
    $embed_path = plugin_dir_path(__FILE__) . 'embed_script.html';
    if (file_exists($embed_path)) {
        echo file_get_contents($embed_path);
    } else {
        echo '<!-- Chatbot embed_script.html not found -->';
    }
}
add_action('wp_footer', 'chatbot_widget_embed');
