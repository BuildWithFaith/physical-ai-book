const path = require('path');

module.exports = function (context, options) {
  return {
    name: 'docusaurus-plugin-chat-widget',

    getClientModules() {
      return [path.resolve(__dirname, './src/ChatWidgetInjector')];
    },

    configureWebpack(config, isServer, utils) {
      return {
        resolve: {
          alias: {
            '@site/src/components/ChatWidget': path.resolve(__dirname, '../../src/components/ChatWidget'),
          },
        },
      };
    },
  };
};