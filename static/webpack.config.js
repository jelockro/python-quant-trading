const webpack = require('webpack');

module.exports = {
	entry: __dirname + '/js/index.jsx',
	output: {
		path: __dirname + '/dist',
		filename: 'bundle.js'
	},
	resolve: {
		extensions: ['.js', '.jsx', '.css']
	},
	module: {
		rules: [
          {
          	test: /\.jsx?$/,  // Match both .js and .jsx files
          	exclude: /node_modules/,
          	loader: 'babel-loader'
          }
		]
	}
};
