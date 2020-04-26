const CompressionPlugin = require('compression-webpack-plugin');

module.exports = function override(config, env) {

  config.optimization = {
    splitChunks: {
      // chunks: 'all',
      // name: false,
      cacheGroups: {
        default: false
      }
    },
    runtimeChunk: false
  }

  if (env === 'production') {
    config.devtool = false;
  }

  // Move runtime into bundle instead of separate file
  config.output.filename = 'static/js/main.js';

  config.plugins[5].options.filename = 'static/css/main.css';

  const plugins = [];

  config.plugins.forEach(plugin => {
    // Remove some plugins 
    if (
      // plugin.constructor.name === "HtmlWebpackPlugin" ||
      // plugin.constructor.name === "InlineChunkHtmlPlugin" ||
      // plugin.constructor.name === "InterpolateHtmlPlugin" ||
      // plugin.constructor.name === "ModuleNotFoundPlugin" ||
      // plugin.constructor.name === "DefinePlugin" ||
      // plugin.constructor.name === "MiniCssExtractPlugin" ||
      plugin.constructor.name === "ManifestPlugin" ||
      // plugin.constructor.name === "IgnorePlugin" ||
      plugin.constructor.name === "GenerateSW"
    ) {
      return;
    }
    plugins.push(plugin)
  });


  plugins.push(new CompressionPlugin({
    algorithm: "gzip",
    deleteOriginalAssets: true,
    test: /\.js$|\.css$|\.html|\.svg|\.png|\.jpg|\.jpeg$/
  }))

  
  config.plugins = plugins;
  return config
}