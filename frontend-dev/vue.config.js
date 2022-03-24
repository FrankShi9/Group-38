const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
    transpileDependencies: true,
    outputDir:'dist',
    assetsDir:'static',
    indexPath:'templates/index.html', // relative to outputDir!
    filenameHashing:false,
    runtimeCompiler:true,
    // devServer: {
    //     writeToDisk:true
    // }
})