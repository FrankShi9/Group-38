const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
    transpileDependencies: true,
    outputDir: '../Area_38/static/',
    indexPath: '../Area_38/templates/index.html', // relative to outputDir!
    // baseUrl: IS_PRODUCTION
    // ? 'http://cdn123.com'
    // : '/',
    // For Production, replace set baseUrl to CDN
    // And set the CDN origin to `yourdomain.com/static`
    // Whitenoise will serve once to CDN which will then cache
    // and distribute
    devServer: {
        proxy: {
            '/api*': {
                // Forward frontend dev server request for /api to django dev server
                target: 'http://localhost:8000/',
            }
        }
    }
})