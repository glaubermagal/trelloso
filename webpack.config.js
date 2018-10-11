const path = require('path');
const webpack = require('webpack');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = env => {
    return {
        entry: './src/index.js',
        mode: "none",
        output: {
            path: path.resolve('dist'),
            filename: 'index_bundle.js',
            publicPath: '/'
        },
        module: {
            rules: [
                {
                    test: /\.scss$/,
                    use: ExtractTextPlugin.extract({
                        fallback: 'style-loader',
                        use: ['css-loader', 'sass-loader']
                    })
                },
                {
                    test: /\.css$/,
                    use: ExtractTextPlugin.extract({
                        fallback: 'style-loader',
                        use: 'css-loader'
                    })
                },
                {
                    test: /\.(js|jsx)$/,
                    exclude: /node_modules/,
                    use: "babel-loader"
                },
                {
                    test: /\.(png|jpe?g|gif|svg)$/,
                    use: [{
                        loader: 'file-loader?limit=100000',
                        options: {
                            name: '[name].[ext]?[hash]',
                            outputPath: 'images/'
                        }
                    }]
                }
            ]
        },
        devServer: {
            historyApiFallback: true,
            host: '0.0.0.0',
        },
        plugins: [
            new ExtractTextPlugin('style.css')
        ]
    }
}
