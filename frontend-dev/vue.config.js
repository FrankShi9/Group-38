const { defineConfig } = require('@vue/cli-service')
const path = require('path')
module.exports = defineConfig({
    outputDir: 'dist',
    assetsDir: 'static',
    indexPath: "templates/index.html",
    filenameHashing: false, // Django will hash file names, not webpack
    runtimeCompiler: true, // See: https://vuejs.org/v2/guide/installation.html#Runtime-Compiler-vs-Runtime-only
    devServer: {
        writeToDisk: true, // Write files to disk in dev mode, so Django can serve the assets
    },
    // Paths
    // publicPath: '/',
    // outputDir: '../Area_38/dist/static',
    // indexPath: '../index.html', // relative to outputDir!
})