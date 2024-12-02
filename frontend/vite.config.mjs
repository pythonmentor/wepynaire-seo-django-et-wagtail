import { defineConfig } from "vite";

// Configuration entry point
export default defineConfig({
  plugins: [],
  base: "/static/",
  build: {
    manifest: "manifest.json",
    emptyOutDir: true,
    rollupOptions: {
      input: {
        app: "./src/index.js"
      }
    },
  },
});
