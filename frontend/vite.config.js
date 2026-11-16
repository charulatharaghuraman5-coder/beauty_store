import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

export default defineConfig({
  plugins: [react()],
  base: './',
  server: {
    host: '0.0.0.0',
    port: 8000,
    strictPort: false,
    allowedHosts: [
      'fyoyp1eigmstsgr.studio.us-east-1.sagemaker.aws',
      'localhost',
      '.sagemaker.aws',
      '.amazonaws.com'
    ],
    hmr: {
      clientPort: 8000
    },
    proxy: {
      '/api': {
        target: 'http://localhost:8001',
        changeOrigin: true,
        secure: false,
        ws: true
      }
    }
  },
  build: {
    outDir: 'dist'
  }
})