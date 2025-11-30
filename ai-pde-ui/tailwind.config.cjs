/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Inter", "system-ui", "sans-serif"],
      },
      colors: {
        surface: {
          1: "#020617", // very dark
          2: "#020817",
          3: "#030712",
        },
        accent: {
          blue: "#3b82f6",
          blueSoft: "#1d4ed8",
          green: "#22c55e",
        },
      },
    },
  },
  plugins: [],
};
