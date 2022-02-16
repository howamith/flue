const path = require("path");

module.exports = {
    configureWebpack: {
        performance: {
            hints: 'warning',

            // Allow an overall asset size of 1 MiB.
            maxAssetSize: 1024 * 1024,
            maxEntrypointSize: 1024 * 1024
        }
    },
    chainWebpack: config => {
        config
            .entry('app')
            .clear()
            .add('./src/main.js')
            .end();
        config.resolve.alias
            .set('@', path.join(__dirname, './client'));
    },
    pages: {
        app: {
            entry: './src/main.js',
            template: './public/index.html',
            filename: 'index.html',
            title: 'Flue'
        }
    },
    outputDir: path.resolve(__dirname, './www'),
    filenameHashing: false
}